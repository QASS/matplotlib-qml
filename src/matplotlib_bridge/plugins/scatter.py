from copy import copy
from PySide2.QtCore import QObject, Signal, Slot, Property
from matplotlib.markers import MarkerStyle
import numpy as np

from matplotlib_bridge.collections import PathCollection
from matplotlib_bridge.cm import ScalarMappable
from matplotlib_bridge.event import EventHandler



class ScatterCollection(PathCollection):
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
        A Collection can't exist outside of an axes because it requires the transform data"""
    
    OFFSET_CHANGED = "OFFSET_CHANGED"

    def __init__(self, parent=None):
        super().__init__(parent)
        self._x = []
        self._y = []
        self._marker = "o"
        self._ax = None
        self._scatter_event_handler = EventHandler()

    def init(self, ax):       
        self._ax = ax
        self._create_plot_obj(ax)
        # initialize the ScalarMappable to enable the colorbar
        ScalarMappable.init(self, ax)
        self._scatter_event_handler.register(self.OFFSET_CHANGED, self._adjust_offset)

    def _create_plot_obj(self, ax):
        """First check whether there are lists of properties otherwise fall back to the defaults or single properties"""
        edgecolors = self._edgecolors if self._edgecolors is not None else self._edgecolor
        colors = self._facecolors if self._facecolors is not None else self._facecolor
        linewidths = self._linewidths if self._linewidths is not None else self._linewidth
        sizes = self._sizes if self._sizes is not None else self._size
        self._plot_obj = ax.scatter(self._x, self._y, c = colors, s = sizes, marker = self._marker, cmap = self._cmap, 
                                    norm = None, vmin = self._vmin, vmax = self._vmax, alpha = self._alpha, 
                                    linewidths = linewidths, edgecolors = edgecolors, hatch = self._hatch)

    def _adjust_offset(self):
        """The offsets is a 2D array, telling the collection where each scatter point is located relative to the origin"""
        x = np.array(self._x).reshape(len(self._x), 1)
        y = np.array(self._y).reshape(len(self._y), 1)

        offsets = np.hstack((x, y))
        self._plot_obj.set_offsets(offsets)
    
    def get_x(self):
        if isinstance(self._x, np.ndarray):
            return self._x.tolist()
        return self._x

    def set_x(self, x):
        self._x = x
        if self._plot_obj is not None:
            if len(self._x ) == len(self._y):
                self._adjust_offset()
                self.xChanged.emit()
                self.xDataChanged.emit()
                self.schedule_plot_update()

    def get_y(self):
        if isinstance(self._y, np.ndarray):
            return self._y.tolist()
        return self._y

    def set_y(self, y):
        self._y = y
        if self._plot_obj is not None:
            if len(self._x ) == len(self._y):
                self._adjust_offset()
                self.yChanged.emit()
                self.yDataChanged.emit()
                self.schedule_plot_update()

    def get_marker(self):
        return self._marker

    def set_marker(self, marker):
        """Fetch the marker style and the current applied transform of the marker style object"""
        self._marker = marker
        if self._plot_obj is not None:            
            marker_obj = MarkerStyle(marker)
            marker_path = marker_obj.get_path().transformed(marker_obj.get_transform())
            self.set_paths((marker_path,))
            self.schedule_plot_update()


    xChanged = Signal()
    yChanged = Signal()
    xDataChanged = xChanged
    yDataChanged = yChanged

    x = Property("QVariantList", get_x, set_x, notify = xChanged)
    xData = x
    y = Property("QVariantList", get_y, set_y, notify = yChanged)
    yData = y
    marker = Property(str, get_marker, set_marker)


def init(factory):
    factory.register(ScatterCollection, "Matplotlib")