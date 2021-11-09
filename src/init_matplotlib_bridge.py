
from plot_objects import Figure, Axis, Plot
from graphs_2d import Line, Scatter, HLine, VSpan, HSpan, Imshow, Bar
import factory
from factory import module_items
import plugin_loader


def main():
    factory.register(Figure, "Matplotlib")
    factory.register(Line, "Matplotlib")
    factory.register(Scatter, "Matplotlib")
    factory.register(Axis, "Matplotlib")
    factory.register(Plot, "Matplotlib")
    factory.register(HLine, "Matplotlib")
    factory.register(VSpan, "Matplotlib")
    factory.register(HSpan, "Matplotlib")
    factory.register(Imshow, "Matplotlib")
    factory.register(Bar, "Matplotlib")

    plugins = plugin_loader.get_plugins()
    plugin_loader.load_plugins(plugins)

    factory.register_at_qml(module_items)

main()

#if __name__ == "__main__":
    #main()
