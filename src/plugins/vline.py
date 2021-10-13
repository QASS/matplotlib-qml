from graphs_2d import LineObject2D
from PySide2.QtCore import Signal, Slot, Property
from event import EventTypes

class VLine(LineObject2D):
    """wrapper for matplotlib.axes.Axes.axvline"""
    def __init__(self, parent = None):
        super().__init__(parent)
        self._x = 0
        self._ymin = 0
        self._ymax = 1
    
    def init(self, ax):
        self._plot_obj = ax.axvline(self._x, **self.matplotlib_2d_kwargs, 
                ymin = self._ymin, ymax = self._ymax)

    def get_x(self):
        return self._x

    def set_x(self, x):
        self._x = x
        if self._plot_obj is not None:
            self._plot_obj.set_xdata([self._x] * 2)
            self._event_handler.emit(EventTypes.PLOT_DATA_CHANGED)

    def get_ymin(self):
        return self._ymin

    def set_ymin(self, ymin):
        self._ymin = ymin
        if self._plot_obj is not None:
            ydata = self._plot_obj.get_ydata()
            ydata[0] = self._ymin
            self._plot_obj.set_ydata(ydata)
            self._event_handler.emit(EventTypes.PLOT_DATA_CHANGED)

    def get_ymax(self):
        return self._ymax

    def set_ymax(self, ymax):
        self._ymax = ymax
        if self._plot_obj is not None:
            ydata = self._plot_obj.get_ydata()
            ydata[1] = self._ymax
            self._plot_obj.set_ydata(ydata)
            self._event_handler.emit(EventTypes.PLOT_DATA_CHANGED)

    x = Property(float, get_x, set_x)
    yMin = Property(float, get_ymin, set_ymin)
    yMax = Property(float, get_ymax, set_ymax)

def init(factory):
    factory.register(VLine, "Matplotlib")