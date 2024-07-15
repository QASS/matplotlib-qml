# Event system

The Matplotlib-Bridge Interfaces uses an `EventHandler` class which is always created with the `Figure`. This `EventHandler` is handed down to each children (The property naming is `self._event_handler`). Events are defined as string constants living inside of the `EventTypes` class. The event system is meant to provide a flexible way to execute functions after certain actions and group changes in the plot together to reduce overhead when rerendering. If the Figure needs to redraw too often it starts to flicker.
You can schedule an event like this:
```python
self._event_handler.schedule(EventTypes.PLOT_DATA_CHANGED)
```
or you can directly emit an event:
```python
self._event_handler.emit(EventTypes.PLOT_DATA_CHANGED)
```
Note that you create a lot of overhead if you emit events directly too often. The cycle length of each timer can be adjusted in the `Figure` Propertys `shortTimerInterval` and `longTimerInterval`. They will default to `shortTimerInterval = 20` and `longTimerInterval = 100` (values in ms) if not provided.