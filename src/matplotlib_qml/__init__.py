from .plot_objects import Figure, Axis, Plot
from .colorbar import Colorbar
from .factory import module_items, register_at_qml, register
from .plugin_loader import get_plugins, load_plugins

def init():
    register(Figure, "Matplotlib")
    register(Axis, "Matplotlib")
    register(Axis, "Matplotlib", qml_component_name = "Axes")
    register(Plot, "Matplotlib")
    register(Colorbar, "Matplotlib")


    plugins = get_plugins()
    load_plugins(plugins)

    register_at_qml(module_items)
