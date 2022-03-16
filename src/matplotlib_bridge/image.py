# matplotlib.image
from PySide2.QtCore import Signal, Slot, Property

from matplotlib_bridge.artist import Artist
from matplotlib_bridge.cm import ScalarMappable
from matplotlib_bridge.event import EventHandler

class _ImageBase(Artist, ScalarMappable):
    """Every image needs to have an axis it can sit on so we need to keep track of the internal state in the wrapper
    object to apply the initial QML properties once the component has been initialized"""
    def __init__(self, parent=None):
        self._plot_obj = None
        Artist.__init__(self, parent)
        ScalarMappable.__init__(self)
        self._interpolation = "antialiased"
        self._origin = "upper"
        self._filternorm = True
        self._filterrad = 4.0
        self._resample = False
        self._interpolation_stage = "data"

    def get_interpolation(self):
        if self._plot_obj is None:
            return self._interpolation
        return self._plot_obj.get_interpolation()

    def set_interpolation(self, interpolation):
        self._interpolation = interpolation
        if self._plot_obj is not None:
            self._plot_obj.set_interpolation(self._interpolation)
            self.schedule_plot_update()

    def get_origin(self):
        return self._origin

    def set_origin(self, origin): # TODO check how to set it during runtime
        self._origin = origin

    def get_resample(self):
        if self._plot_obj is None:
            return self._resample
        return self._plot_obj.get_resample()

    def set_resample(self, resample):
        self._resample = resample
        if self._plot_obj is not None:
            self._plot_obj.set_resample(self._resample)
            self.schedule_plot_update()

    def get_filternorm(self):
        if self._plot_obj is None:
            return self._filternorm
        return self._plot_obj.get_filternorm()

    def set_filternorm(self, filternorm):
        self._filternorm = filternorm
        if self._plot_obj is not None:
            self._plot_obj.set_filternorm(filternorm)
            self.schedule_plot_update()

    def get_filterrad(self):
        if self._plot_obj is None:
            return self._filterrad
        self._plot_obj.get_filterrad()

    def set_filterrad(self, filterrad):
        self._filterrad = filterrad
        if self._plot_obj is not None:
            self._plot_obj.set_filterrad(self._filterrad)
            self.schedule_plot_update()

    def get_interpolation_stage(self):
        return self._interpolation_stage

    def set_interpolation_stage(self, interpolation_stage):
        self._interpolation_stage = interpolation_stage
        if self._plot_obj is not None:
            self._plot_obj.set_interpolation_stage(self._interpolation_stage)
            self.schedule_plot_update()

    interpolation = Property(str, get_interpolation, set_interpolation)
    origin = Property(str, get_origin, set_origin)
    resample = Property(bool, get_resample, set_resample)
    filternorm = Property(bool, get_filternorm, set_filternorm)
    filterrad = Property(float)

class AxesImage(_ImageBase):
    
    def __init__(self, parent=None):
        super().__init__(parent)


class Imshow(AxesImage):

    def __init__(self, parent=None):
        super().__init__(parent)


        self._ax = None

    def init(self, ax):
        self._ax = ax
        self._plot_obj = ax.imshow()