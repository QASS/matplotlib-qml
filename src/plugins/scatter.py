from copy import copy
from PySide2.QtCore import QObject, Signal, Slot, Property
from graphs_2d import PlotObject2D
from plot_objects import Axis
from event import EventHandler, EventTypes



class ScatterCollection(PlotObject2D):
    """wrapper for matplotlib.pyplot.scatter
    Note that this instantiates a PathCollection so you will have a lot of objects sticking around 
    if you have many scatter points. The scatter is reinstantiated every time a property changes as well which
    results in additional overhead.
    Example:
        ScatterCollection {
            x: [1,2,3]
            y: [1,2,3]
            c: [1,2,3]
            cMap: "gist_rainbow"
        }
    """
    def __init__(self, parent = None):
        super().__init__(parent)
        self._x = []
        self._y = []
        self._sizes = None # Array
        self._size = None # scalar marker size
        self._colors = None # Array
        self._marker = None
        self._cmap = None
        self._vmin = None
        self._vmax = None
        self._scatter_event_handler = EventHandler()
        self._ax = None # reference to the matplotlib wrapper axis
        self._colorbar = None

    def init(self, ax):
        # create the ScatterCollection
        self._create_plot_obj(ax)
        # create the colorbar if there is one
        if self._colorbar is not None:
            self._colorbar.set_event_handler(self._event_handler)
            self._colorbar.init(ax, self._plot_obj)            

        self._scatter_event_handler.register(EventTypes.PLOT_DATA_CHANGED, self.redraw)

        axis = self.parent()
        if isinstance(axis, Axis):
            self._ax = axis
        else:
            raise LookupError("Parent is not of type Axis")

    def _create_plot_obj(self, ax):
        if self._sizes is not None:
            self._plot_obj = ax.scatter(self._x, self._y, **self.matplotlib_2d_kwargs, s = self._sizes, c = self._colors, 
            marker = self._marker, cmap = self._cmap, vmin = self._vmin, vmax = self._vmax)
        else:
            self._plot_obj = ax.scatter(self._x, self._y, **self.matplotlib_2d_kwargs, s = self._size, c = self._colors, 
            marker = self._marker, cmap = self._cmap, vmin = self._vmin, vmax = self._vmax)

    def redraw(self):
        """Delete the current plot object and reinstantiate it with the new parameters"""
        if self._colorbar is not None:
            self._colorbar.remove()
        if self._plot_obj is not None:
            self._plot_obj.remove()
            self._plot_obj = None
        # get the axis parent object
        self._create_plot_obj(self._ax.get_matplotlib_ax_object())
        if self._colorbar is not None:
            self._colorbar.update_mappable(self._plot_obj)
        self._event_handler.schedule(EventTypes.PLOT_DATA_CHANGED)

    def get_x(self):
        return self._x

    def set_x(self, x):
        self._x = copy(x)
        self.xChanged.emit()
        if self._plot_obj is not None and len(self._x) == len(self._y):
            self._scatter_event_handler.schedule(EventTypes.PLOT_DATA_CHANGED)

    def get_y(self):
        return self._y

    def set_y(self, y):
        self._y = copy(y)
        self.yChanged.emit()
        if self._plot_obj is not None and len(self._x) == len(self._y):
            self._scatter_event_handler.schedule(EventTypes.PLOT_DATA_CHANGED)

    def get_sizes(self):
        return self._size

    def set_sizes(self, sizes):
        self._sizes = copy(sizes)
        if self._plot_obj is not None:
            self._scatter_event_handler.schedule(EventTypes.PLOT_DATA_CHANGED)

    def get_size(self):
        return self._size

    def set_size(self, size):
        self._size = size        
        if self._plot_obj is not None:
            self._scatter_event_handler.schedule(EventTypes.PLOT_DATA_CHANGED)

    def get_colors(self):
        return self._colors

    def set_colors(self, colors):
        self._colors = copy(colors)
        if self._plot_obj is not None:
            self._scatter_event_handler.schedule(EventTypes.PLOT_DATA_CHANGED)

    def get_marker(self):
        return self._marker

    def set_marker(self, marker):
        self._marker = marker
        if self._plot_obj is not None:
            self._scatter_event_handler.schedule(EventTypes.PLOT_DATA_CHANGED)

    def get_cmap(self):
        return self._cmap

    def set_cmap(self, cmap):
        self._cmap = cmap
        if self._plot_obj is not None:
            self._scatter_event_handler.schedule(EventTypes.PLOT_DATA_CHANGED)

    def get_vmin(self):
        return self._vmin

    def set_vmin(self, vmin):
        self._vmin = vmin
        if self._plot_obj is not None:
            self._scatter_event_handler.schedule(EventTypes.PLOT_DATA_CHANGED)

    def get_vmax(self):
        return self._vmax

    def set_vmax(self, vmax):
        self._vmax = vmax
        if self._plot_obj is not None:
            self._scatter_event_handler.schedule(EventTypes.PLOT_DATA_CHANGED)

    def get_colorbar(self):
        return self._colorbar

    def set_colorbar(self, colorbar):
        self._colorbar = colorbar
        

    xChanged = Signal()
    yChanged = Signal()

    x = Property("QVariantList", get_x, set_x, notify = xChanged)
    y = Property("QVariantList", get_y, set_y, notify = yChanged)
    s = Property("QVariantList", get_sizes, set_sizes)
    c = Property("QVariantList", get_colors, set_colors)
    marker = Property(str, get_marker, set_marker)
    cMap = Property(str, get_cmap, set_cmap)
    markerSize = Property(float, get_size, set_size)
    vMin = Property(float, get_vmin, set_vmin)
    vMax = Property(float, get_vmax, set_vmax)
    colorbar = Property(QObject, get_colorbar, set_colorbar)


def init(factory):
    factory.register(ScatterCollection, "Matplotlib")