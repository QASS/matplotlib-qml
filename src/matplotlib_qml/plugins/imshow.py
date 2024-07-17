from PySide2.QtCore import Property, Signal

from matplotlib_qml.image import AxesImage
from matplotlib_qml.cm import ScalarMappable

class Imshow(AxesImage):
    
    def __init__(self, parent=None):
        super().__init__(parent)
        self._aspect = "equal"


        self._ax = None

    def init(self, ax):
        self._ax = ax
        self._plot_obj = ax.imshow(self._x, cmap = self._cmap, aspect = self._aspect, 
                                vmin = self._vmin, vmax = self._vmax, origin = self._origin, 
                                extent = self._extent, filternorm = self._filternorm, 
                                filterrad = self._filterrad, resample = self._resample)
        ScalarMappable.init(self, ax)

    def get_aspect(self):
        if self._ax is None:
            return self._aspect
        return self._ax.get_aspect()

    def set_aspect(self, aspect):
        """The aspect property is originally from the axis so it might move there"""
        self._aspect = aspect
        if self._ax is not None:
            self._ax.set_aspect(self._aspect)
            self.schedule_plot_update()
            self.aspectChanged.emit()

    aspectChanged = Signal()

    aspect = Property(str, get_aspect, set_aspect)

def init(factory):
    factory.register(Imshow, "Matplotlib")
