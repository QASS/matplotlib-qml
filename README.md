# Matplotlib bridge
## A QML Bridge to Matplotlib

This helper library is a easy to use QML implementation of graph plotting based on the python library matplotlb.
The library is based on the QtQuick backend for matplotlib from jmitrevs:
https://github.com/jmitrevs/matplotlib_backend_qtquick

It allows to create and design matplotlib plots and figures from QML.
It is based on a PySide2 QObject implementation of a python object wrapper.
The Python object wrapper wraps a python instance and provides string based access to the PyObject's attributes and functions.

![QML matplotlib bridge](/images/Screenshot_QML_Matplotlib.png)

### How to use it

Install the python packages matplotlib-backend-qtquick:
```
pip install matplotlib-backend-qtquick --user
```

To use the Matplotlib Python bridge ensure that you have set the app_init.py as the init script in the Analyzer4D application.
app_init.py contains the wrapper's implementation and some simple ready to use classes such as SimpleGraph.

The script registers the types in the application's QML engine.

Try the examples to see how it can be used in QML GUIs.
The QML files in the src directory are the more flexible implementation whereas SimpleGraph is quite limited in its features.

### How to extend

A bridge element has to inherit from the class MatplotlibObjectWrapper.

Since the QML objects are created bottom to top and matplotlib objects are usually created in reversed order we have to first create all QML QOjects and then to setup the matplotlib instances. This can be done using the function onInitWrapper() {}.
To access the containing QML object simply use the _self.parent()_ python statement.

To call functions on the object simply use the method _call(funcname, [argumentlist], {keywordargs})_.

The wrapped PyObject can be accessed via _self.obj_

```
import Matplotlib 1.0
MatplotlibObjectWrapper {
    id: new_elem
    onInitWrapper() {
        wrapObj('self.parent().obj.plot([], [])[0]')
    }

    function changeColor(color) {
        call('self.obj', [color])
    }
}
```
