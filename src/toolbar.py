

from PySide2.QtCore import Signal, Slot, Property
from PySide2.QtQuick import QQuickItem
from matplotlib_backend_qtquick.backend_qtquick import NavigationToolbar2QtQuick

# doc: https://matplotlib.org/stable/api/backend_bases_api.html

class Toolbar(QQuickItem):
    events = ['resize_event', 
          'draw_event', 
          'key_press_event', 
          'key_release_event', 
          'button_press_event', 
          'button_release_event', 
          'scroll_event', 
          'motion_notify_event', 
          'pick_event', 
          'idle_event', 
          'figure_enter_event', 
          'figure_leave_event', 
          'axes_enter_event', 
          'axes_leave_event', 
          'close_event']

    def __init__(self, parent = None):
        super().__init__(parent)
        self._figure = None
        self._toolbar = None
        self._coordinates = (0, 0)
        self._event_handler = None # populated by figure


    def init(self, figure):
        self._figure = figure
        self._toolbar = NavigationToolbar2QtQuick(canvas = figure.canvas)

        # connect the events
        self._figure.canvas.mpl_connect("motion_notify_event", self._on_motion)
        self._figure.canvas.mpl_connect("pick_event", self._on_pick)

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

    def _on_pick(self, event):
        plot_object = event.artist
        index = event.ind
        print(index)

    def get_coordinates(self):
        return str(self._coordinates)

    coordinatesChanged = Signal()

    coordinates = Property(str, get_coordinates, notify = coordinatesChanged)


def init(factory):
    factory.register(Toolbar, "Matplotlib")