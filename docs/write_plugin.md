On application start the `plugin_loader` will attempt to load all modules in the `/plugins/` directory. Each modules needs to implement a `init` function that registers the plugin to the program. The init function receives a `factory` as an argument which must receive the `class` and the QML module name to register the class in:
```python
class MyClass(Base):
	# Code here

def init(factory):
	factory.register(MyClass, "QMLModuleName")
```

The factory register function allows to set the following arguments:

| Argument		  | Value	   		| Required      | Description 						   	|
| --------------- |:---------------:|:-------------:|--------------------------------------:|
| class_reference | Class      		| True          | reference to the class definition		|
| QMLModuleName	  | String      	| True          | The Module name in QML (for imports)	|
| version		  | Int      		| False         | Main version number (default = 1)		|
| subversion	  | Int      		| False         | Subversion number (default = 0)		|
| QMLComponentName| String     		| False         | Component name in QML default = \_\_name\_\_ From the Python class		|

In QML the component is then used like:
```javascript
import QMLModuleName 1.0

QMLComponentName {

}
```

The Plugin Class must implement the method `init` that receives a `matplotlib.axis.Axis` object as an argument. It must inherit one of the base classes like `matplotlib_qml.plot_objects.Base`, `matplotlib_qml.artist.Artist`. Each object inheriting these classes will receive an Event Handler from the axes which is handed down from the figure `self._event_handler`. The Event Handler is available after `matplotlib_qml.plot_objects.Figure.init`is called. You can use this Event Handler to emit or schedule Events whenever the data lying in the plot object changes:
```py
self._event_handler.emit(EventTypes.PLOT_DATA_CHANGED) # emit events directly
self._event_handler.schedule(EventTypes.PLOT_DATA_CHANGED) # schedule events for next cycle
```
The `Artist` class implements a shorthand method `schedule_plot_update` which schedules a `PLOT_DATA_CHANGED` event.
Available Events can be found in the `matplotlib_qml.event.EventTypes` class which contains all the constants.

You can also register methods to be executed whenever an event is emitted from other components. To do that you need to register the method to the event handler (best to do during `init`:
```py
def init(self, ax):
    self._plot_obj = ax.plot(self._x_values)
    # more logic here
    self._event_handler.register(Eventtypes.PLOT_DATA_CHANGED, self.my_method)
```

This will result in `my_method` being executed whenever the event is emitted. You can also create an internal event handler if you need to create events independent to other components or the figure. Note that the figure needs to receive an event in order to rerender after your changes.

## Register a component without using the plugin folder

In order to use the bridge you need to call the `matplotlib_qml.init` method. This method registers all the internal components and plugins to QML. You can register your own components before calling this method:
```py
from matplotlib_qml import factory, init
from custom_qml_component import CustomQMLComponent

factory.register(CustomQMLComponent, "MyModuleName", qml_component_name = "CustomComponent")
init()
```

!!! warning "Register component multiple times"

    Registering the same QML component name twice will result in the first one being erased.
    The `qml_component_name` is optional. If it is not provided the `Class.__name__` attribute is used.

