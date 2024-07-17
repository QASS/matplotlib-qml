# matplotlib.image
from PySide2.QtCore import Signal, Slot, Property
import numpy as np

from .artist import Artist
from .cm import ScalarMappable
from .event import EventTypes

class _ImageBase(Artist, ScalarMappable):
    """Every image needs to have an axis it can sit on so we need to keep track of the internal state in the wrapper
    object to apply the initial QML properties once the component has been initialized"""
    def __init__(self, parent=None):
        self._plot_obj = None
        Artist.__init__(self, parent)
        ScalarMappable.__init__(self)
        self._x = []
        self._interpolation = "antialiased"
        self._origin = "upper"
        self._filternorm = True
        self._filterrad = 4.0
        self._resample = False
        self._interpolation_stage = "data"

    @property
    def x(self):
        """Property to return the original array in case a numpy array was provided.
        `get_x` would return a python list because numpy arrays can't be used in QML"""
        return self._x

    def get_x(self):
        if isinstance(self._x, np.ndarray):
            return self._x.tolist()
        return self._x

    def set_x(self, X):
        self._x = X
        if self._plot_obj is not None:
            self._plot_obj.set_data(self._x)
            self.schedule_plot_update()
            self.xChanged.emit()

    def get_interpolation(self):
        if self._plot_obj is None:
            return self._interpolation
        return self._plot_obj.get_interpolation()

    def set_interpolation(self, interpolation):
        self._interpolation = interpolation
        if self._plot_obj is not None:
            self._plot_obj.set_interpolation(self._interpolation)
            self.schedule_plot_update()
            self.interpolationChanged.emit()

    def get_origin(self):
        return self._origin

    def set_origin(self, origin): # TODO check how to set it during runtime
        self._origin = origin
        # self.originChanged.emit()

    def get_resample(self):
        if self._plot_obj is None:
            return self._resample
        return self._plot_obj.get_resample()

    def set_resample(self, resample):
        self._resample = resample
        if self._plot_obj is not None:
            self._plot_obj.set_resample(self._resample)
            self.schedule_plot_update()
            self.resampleChanged.emit()

    def get_filternorm(self):
        if self._plot_obj is None:
            return self._filternorm
        return self._plot_obj.get_filternorm()

    def set_filternorm(self, filternorm):
        self._filternorm = filternorm
        if self._plot_obj is not None:
            self._plot_obj.set_filternorm(filternorm)
            self.schedule_plot_update()
            self.filternormChanged.emit()

    def get_filterrad(self):
        if self._plot_obj is None:
            return self._filterrad
        self._plot_obj.get_filterrad()

    def set_filterrad(self, filterrad):
        self._filterrad = filterrad
        if self._plot_obj is not None:
            self._plot_obj.set_filterrad(self._filterrad)
            self.schedule_plot_update()
            self.filterradChanged.emit()

    def get_interpolation_stage(self):
        return self._interpolation_stage

    def set_interpolation_stage(self, interpolation_stage):
        self._interpolation_stage = interpolation_stage
        if self._plot_obj is not None:
            self._plot_obj.set_interpolation_stage(self._interpolation_stage)
            self.schedule_plot_update()
            self.interpolationChanged.emit()

    xChanged = Signal()
    interpolationChanged = Signal()
    originChanged = Signal()
    resampleChanged = Signal()
    filternormChanged = Signal()
    filterradChanged = Signal()

    x = Property("QVariantList", get_x, set_x)
    interpolation = Property(str, get_interpolation, set_interpolation)
    origin = Property(str, get_origin, set_origin)
    resample = Property(bool, get_resample, set_resample)
    filternorm = Property(bool, get_filternorm, set_filternorm)
    filterrad = Property(float, get_filterrad, set_filterrad)

class AxesImage(_ImageBase):
    
    def __init__(self, parent=None):
        super().__init__(parent)
        self._extent = None

    def get_extent(self):
        """if self._extent = None (unset) this will return the proeprty value of the wrapped image object
        and calculate the extent based on the origin and the number of rows and columns"""
        if self._plot_obj is None:
            return self._extent
        return self._plot_obj.get_extent()

    def set_extent(self, extent):
        """
        :param extent: 4-tuple of float. The position and size of the image as tuple
            ``(left, right, bottom, top)`` in data coordinates.
        """
        self._extent = extent
        if self._plot_obj is not None:
            self._plot_obj.set_extent(self._extent)
            self._event_handler.schedule(EventTypes.PLOT_DATA_CHANGED)
            self.extentChanged.emit()

    extentChanged = Signal()

    extent = Property("QVariantList", get_extent, set_extent)
