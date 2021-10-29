from collections import defaultdict
from PySide2.QtCore import QTimer, QObject


class EventTypes:
	PLOT_DATA_CHANGED = "PLOT_DATA_CHANGED"
	AXIS_DATA_CHANGED = "AXIS_DATA_CHANGED"
	FIGURE_DATA_CHANGED = "FIGURE_DATA_CHANGED"

class EventHandler:
	def __init__(self):
		# super().__init__(parent = None)
		self._subscribers = defaultdict(list) 
		self._event_schedule = set()
		self._fast_timer, self._interval_timer = QTimer(), QTimer()
		self._interval_timer.timeout.connect(self._emit_events)
		self._interval_timer.start(1000)

	def register(self, event_type, func):
		self._subscribers[event_type].append(func)

	def emit(self, event_type):
		for subscriber_function in self._subscribers.get(event_type, []):
			subscriber_function()

	def _emit_events(self):
		for event in self._event_schedule:
			for subscriber_function in self._subscribers.get(event, []):
				subscriber_function()
		self._event_schedule.clear()

	def schedule(self, event_type):
		self._event_schedule.add(event_type)
