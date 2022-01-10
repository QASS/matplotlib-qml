

from PySide2.QtCore import Signal, Slot, Property
from PySide2.QtQuick import QQuickItem
from matplotlib_backend_qtquick.backend_qtquick import NavigationToolbar2QtQuick


class Toolbar(QQuickItem):

    def __init__(self, parent = None):
        super().__init__(parent)
        self._figure = None
        self._toolbar = None
        self._coordinates = (0, 0)
        self._event_handler = None # populated by figure


    def init(self, figure):
        self._figure = figure
        self._toolbar = NavigationToolbar2QtQuick(canvas = figure.canvas)

        self._figure.canvas.mpl_connect("motion_notify_event", self._on_motion)

    def _on_motion(self, event):
        self._coordinates = (event.xdata, event.ydata)

    @Slot()
    def home(self, *args):
        self._toolbar.home(*args)

    @Slot()
    def back(self, *args):
        self._toolbar.back(*args)

    @Slot()
    def forward(self, *args):
        self._toolbar.forward(*args)

    @Slot()
    def pan(self, *args):
        """Activate the pan tool."""
        self._toolbar.pan(*args)

    @Slot()
    def zoom(self, *args):
        """activate zoom tool."""
        self._toolbar.zoom(*args)

    def get_coordinates(self):
        return str(self._coordinates)

    coordinatesChanged = Signal()

    coordinates = Property(str, get_coordinates, notify = coordinatesChanged)


def init(factory):
    factory.register(Toolbar, "Matplotlib")