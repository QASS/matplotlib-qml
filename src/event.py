from collections import defaultdict
from PySide2.QtCore import QTimer, QObject


class EventTypes:
	PLOT_DATA_CHANGED = "PLOT_DATA_CHANGED"
	AXIS_DATA_CHANGED = "AXIS_DATA_CHANGED"
	FIGURE_DATA_CHANGED = "FIGURE_DATA_CHANGED"
	BAR_PLOT_CHANGED = "BAR_PLOT_CHANGED"

class EventHandler:
	"""This class handles all the events that can be emitted when changing the configuratio
	or content of the plot or anything in general. You can subscribe to a specific event
	with a function and the Event Handler will execute that function whenever the event
	gets emitted.
	
	:param variable_timer_interval: This timer is being resetted every time an event comes in
	to prevent the plot from updating too often. This functionality will group events together
	but allow single events to be handled faster.
	:type variable_timer_interval: int, optional
	:param set_timer_interval: The set timer will handle all events after each timeout to 
	make sure the plot is updating even though a constant flow of events arrives and resets the 
	variable_timer each time.
	:type set_timer_interval: int, optional
	"""
	def __init__(self, short_timer_interval = 20, long_timer_interval = 100):
		self._subscribers = defaultdict(list) 
		self._event_schedule = set()
		self._short_timer_interval = short_timer_interval
		self._long_timer_interval = long_timer_interval
		self._short_timer, self._long_timer = QTimer(), QTimer()
		self._init_timers()
		
	def _init_timers(self):
		self._short_timer.timeout.connect(self._emit_events)
		self._long_timer.timeout.connect(self._emit_events)
		self._long_timer.start(self._long_timer_interval)
		

	def register(self, event_type, func):
		"""Register a function to the Event Handler. This function will be called whenever
		the corresponding event is emitted"""
		self._subscribers[event_type].append(func)

	def emit(self, event_type):
		"""Emit an event directly (synchronously) without waiting for the next update interval
		
		:param event_type: :class:`EventTypes` constant describing the type of Event
		:type event_type: str
		"""
		for subscriber_function in self._subscribers.get(event_type, []):
			subscriber_function()

	def _emit_events(self):
		events = self._event_schedule.copy()
		self._event_schedule.clear()
		for event in events:
			self.emit(event)
		# stop the variable timer after all events have been handled to reduce overhead
		self._short_timer.stop()

	def schedule(self, event_type):
		self._event_schedule.add(event_type)
		# Start the variable timer whenever an event comes in
		self._short_timer.start(self._short_timer_interval)
