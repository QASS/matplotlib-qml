
from matplotlib_bridge.plot_objects import Figure, Axis, Plot
from matplotlib_bridge.colorbar import Colorbar
from matplotlib_bridge.factory import module_items
from matplotlib_bridge import factory
from matplotlib_bridge import plugin_loader
# from matplotlib_bridge.image import Imshow

def init():
    factory.register(Figure, "Matplotlib")
    factory.register(Axis, "Matplotlib")
    factory.register(Plot, "Matplotlib")
    # factory.register(Imshow, "Matplotlib")
    factory.register(Colorbar, "Matplotlib")


    plugins = plugin_loader.get_plugins()
    plugin_loader.load_plugins(plugins)

    factory.register_at_qml(module_items)
