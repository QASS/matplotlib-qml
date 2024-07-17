# Scalar Mappable
from PySide2.QtCore import QObject, Property, Signal
import numpy as np

from .event import EventTypes
from .utils import numpy_compatibility

class ScalarMappable:
    """This class is the wrapper for matplotlib.cm.ScalarMappable. It uses a `_plot_obj` attribute which 
    must be instantiated before calling the constructor"""
    def __init__(self):
        self._array = [] # the array A for an image
        self._cmap = "viridis"
        self._norm = None
        self._vmin = None
        self._vmax = None
        self._colorbar = None

        self._ax = None

    def init(self, ax):
        self._ax = ax
        if self._colorbar is not None:
            self._colorbar.set_event_handler(self._event_handler)
            self._colorbar.init(ax, self._plot_obj)

    @property
    def kwargs(self):
        kwargs = {
            "cmap": self._cmap,
        }
        return kwargs

    def get_array(self):
        return self._array
    
    def set_array(self, A):
        self._array = A
        if self._plot_obj is not None:
            self._plot_obj.set_array(np.array(A))

    def get_cmap(self):
        if self._plot_obj is None:
            return self._cmap
        return self._plot_obj.get_cmap()

    def set_cmap(self, cmap):
        self._cmap = cmap
        if self._plot_obj is not None:
            self._plot_obj.set_cmap(cmap)
            self._event_handler.schedule(EventTypes.PLOT_DATA_CHANGED)
            self.cMapChanged.emit()

    def get_norm(self):
        if self._plot_obj is None:
            return self._norm
        return self._plot_obj.get_norm()

    def set_norm(self, norm):
        if self._plot_obj is not None:
            self._plot_obj.set_norm(norm)            

    @numpy_compatibility
    def get_vmin(self):
        return self._vmin

    def set_vmin(self, vmin):
        self._vmin = vmin
        if self._plot_obj is not None:
            self._plot_obj.set_clim(self._vmin, self._vmax)
            self._colorbar.draw_all()
            self._event_handler.schedule(EventTypes.PLOT_DATA_CHANGED)
            self.vMinChanged.emit()

    @numpy_compatibility
    def get_vmax(self):
        return self._vmax

    def set_vmax(self, vmax):
        self._vmax = vmax
        if self._plot_obj is not None:
            self._plot_obj.set_clim(self._vmin, self._vmax)
            self._colorbar.draw_all()
            self._event_handler.schedule(EventTypes.PLOT_DATA_CHANGED)
            self.vMaxChanged.emit()

    def get_colorbar(self):
        return self._colorbar

    def set_colorbar(self, colorbar):
        self._colorbar = colorbar
        if self._plot_obj is not None:
            self._event_handler.schedule(EventTypes.PLOT_DATA_CHANGED)
            self.colorbarChanged.emit()

    cMapChanged = Signal()
    vMinChanged = Signal()
    vMaxChanged = Signal()
    colorbarChanged = Signal()

    cMap = Property(str, get_cmap, set_cmap)
    vMin = Property(float, get_vmin, set_vmin)
    vMax = Property(float, get_vmax, set_vmax)
    colorbar = Property(QObject, get_colorbar, set_colorbar)
