# Contribution Guide

You want to contribute to the project?
That's great stuff! Currently I'm checking how tests could be integrated into gitlab to allow the CI/CD workflow we'd all love to have. But until then this will be compensated by code-reviews. 

## Workflow

The project uses a plugin architecture. The aim is to create separateable components that are independent of each other. Contributing with one of those is the easiest since they are standalone and can be even plugged in and out during runtime. 
The core structure is based on an inheritance tree of classes that mimic the structure of the matplotlib inheritance. If you want to write a plugin you should check out which class already implements some properties and inherit from it. Normally this should be the `Artist` or some other class that already inherits from `Artist`. If your class can't implement the properties of `Artist` you need to inherit from `Base`. These are the two superclasses that are recognized by the figure and included in the initialization flow.

```py
from matplotlib_qml.plot_objects import Base
from matplotlib_qml.artist import Artist
```

If you don't do that your component will be usable in QML (i.e. no error appears) but it won't be called by the `Figure` wrapper object and thus not initialize. If you 'just' want to write a plugin for yourself you can go to [Write a Plugin](./write_plugin.md).

If you want to write a plugin to integrate it into the project create a branch named `plugin/<name_of_your_plugin>` and create a merge request for me. Of course while the request is pending you can already use it as described above.


## Documentation

Whenever you want to contribute make sure your plugin/feature comes with sufficient documentation. The documentation is a Gitlab Wiki page and **must** include the following and obey the structure of the component pages:
- Docstrings under non-property methods (if they have a complicated data flow) in the [Sphinx](https://sphinx-rtd-tutorial.readthedocs.io/en/latest/docstrings.html) format
- At least one Example that can be copy pasted
- Description of the QML properties
- Description of the Python interface for the QML properties

This is to ensure that your code can be properly reviewed, debugged, tested and extended later on.
