import sys
sys.path.insert(1, "../")
from typing import Callable

from PySide2.QtQuick import QQuickItem
from PySide2.QtGui import QGuiApplication
from PySide2.QtQml import QQmlApplicationEngine, qmlRegisterType
from PySide2.QtCore import QUrl, QObject, Signal, Slot, Property


from src.plot_objects import Figure, Axis, Plot
from src.graphs_2d import PlotObject2D, Line, Scatter, HLine, VSpan, HSpan, Imshow
from src import factory
from src.factory import module_items
from src import plugin_loader

from pathlib import Path
CURRENT_DIRECTORY = Path(__file__).resolve().parent
print(CURRENT_DIRECTORY)


def main():
    app = QGuiApplication(sys.argv)
    engine = QQmlApplicationEngine()


    factory.register(Figure, "Matplotlib")
    factory.register(Line, "Matplotlib")
    factory.register(Scatter, "Matplotlib")
    factory.register(Axis, "Matplotlib")
    factory.register(Plot, "Matplotlib")
    factory.register(HLine, "Matplotlib")
    factory.register(VSpan, "Matplotlib")
    factory.register(HSpan, "Matplotlib")
    factory.register(Imshow, "Matplotlib")

    plugins = plugin_loader.get_plugins()
    plugin_loader.load_plugins(plugins)

    factory.register_at_qml(module_items)
    # qmlRegisterType(Figure, 'Matplotlib', 1, 0, Figure.__name__)
    # qmlRegisterType(Line, 'Matplotlib', 1, 0, Line.__name__)
    # qmlRegisterType(Scatter, 'Matplotlib', 1, 0, Scatter.__name__)
    # qmlRegisterType(Axis, 'Matplotlib', 1, 0, Axis.__name__)
    # qmlRegisterType(Plot, 'Matplotlib', 1, 0, Plot.__name__)


    
    engine.load(QUrl("./examples/main.qml"))
    
    if not engine.rootObjects():
        sys.exit(-1)
    
    sys.exit(app.exec_())


if __name__ == "__main__":
    sys.path.insert(1, "../")
    main()