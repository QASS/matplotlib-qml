from collections import defaultdict


class EventTypes:
	PLOT_DATA_CHANGED = "PLOT_DATA_CHANGED"
	AXIS_DATA_CHANGED = "AXIS_DATA_CHANGED"
	FIGURE_DATA_CHANGED = "FIGURE_DATA_CHANGED"

class EventHandler:
	def __init__(self):
		self._subscribers = defaultdict(list) 

	def register(self, event_type, func):
		self._subscribers[event_type].append(func)

	def emit(self, event_type):
		for subscriber_function in self._subscribers.get(event_type, []):
			subscriber_function()
