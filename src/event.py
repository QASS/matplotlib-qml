from collections import defaultdict
from PySide2.QtCore import QTimer, QObject


class EventTypes:
	PLOT_DATA_CHANGED = "PLOT_DATA_CHANGED"
	AXIS_DATA_CHANGED = "AXIS_DATA_CHANGED"
	FIGURE_DATA_CHANGED = "FIGURE_DATA_CHANGED"

class EventHandler:
	"""This class handles all the events that can be emitted when changing the configuratio
	or content of the plot or anything in general. You can subscribe to a specific event
	with a function and the Event Handler will execute that function whenever the event
	gets emitted."""
	def __init__(self):
		self._subscribers = defaultdict(list) 
		self._event_schedule = set()
		self._fast_timer, self._interval_timer = QTimer(), QTimer()
		self._interval_timer.timeout.connect(self._emit_events)
		self._interval_timer.start(5000)

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
		for event in self._event_schedule:
			self.emit(event)
		self._event_schedule.clear()

	def schedule(self, event_type):
		self._event_schedule.add(event_type)
