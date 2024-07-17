from PySide2.QtCore import QObject, Signal, Slot, Property
import numpy as np
from matplotlib_qml.patches import Polygon
from matplotlib_qml.utils import numpy_compatibility

class SpanBase(Polygon):
    """Base class for the HSpan and VSpan which implements the Polygon behaviour"""
    def __init__(self, parent=None):
        super().__init__(parent)
        self._ymin = 0
        self._ymax = 0
        self._xmin = 0
        self._xmax = 0

    def _get_polygon_coordinates(self):
        xy = np.array([self._xmin, self._ymin, self._xmin, self._ymax, self._xmax, self._ymax, self._xmax, self._ymin])
        return xy.reshape((4, 2))

    @numpy_compatibility
    def get_ymin(self):
        return self._ymin

    def set_ymin(self, ymin):
        """Updates the polygon data of the span object
        """
        self._ymin = float(ymin)
        if self._plot_obj is not None:
            # Modify the reference of xy which also modifies the property xy
            xy = self._plot_obj.get_xy()
            if xy.shape != (4, 2):
                xy = self._get_polygon_coordinates()
            else:
                xy[0][1] = self._ymin
                xy[3][1] = self._ymin
            # if self._plot_obj.get_closed():
            #     xy[4][1] = self._ymin
            self._plot_obj.set_xy(xy)
            self.schedule_plot_update()
            self.yMinChanged.emit()

    @numpy_compatibility
    def get_ymax(self):
        return self._ymax

    def set_ymax(self, ymax):
        """Modifys the ymax coords from the xy Property of the Polygon"""
        self._ymax = float(ymax)
        if self._plot_obj is not None:
            # Modify the reference of xy which also modifies the property xy
            xy = self._plot_obj.get_xy()
            if xy.shape != (4, 2):
                xy = self._get_polygon_coordinates()
            else:
                xy[1][1] = self._ymax
                xy[2][1] = self._ymax
            self._plot_obj.set_xy(xy)
            self.schedule_plot_update()
            self.yMaxChanged.emit()

    @numpy_compatibility
    def get_xmin(self):
        return self._xmin

    def set_xmin(self, xmin):
        self._xmin = float(xmin)
        if self._plot_obj is not None:
            # Modify the reference of xy which also modifies the property xy
            xy = self._plot_obj.get_xy()
            if xy.shape != (4, 2):
                xy = self._get_polygon_coordinates()
            else:
                xy[0][0] = self._xmin
                xy[1][0] = self._xmin
            # if self._plot_obj.get_closed():
            #     xy[4][0] = self._xmin
            self._plot_obj.set_xy(xy)
            self.schedule_plot_update()
            self.xMinChanged.emit()

    @numpy_compatibility
    def get_xmax(self):
        return self._xmax

    def set_xmax(self, xmax):
        self._xmax = float(xmax)
        if self._plot_obj is not None:
            # Modify the reference of xy which also modifies the property xy
            xy = self._plot_obj.get_xy()
            if xy.shape != (4, 2):
                xy = self._get_polygon_coordinates()
            else:
                xy[2][0] = self._xmax
                xy[3][0] = self._xmax
            #self._plot_obj.set_xy(xy)
            self.schedule_plot_update()
            self.xMaxChanged.emit()

    yMinChanged = Signal()
    yMaxChanged = Signal()
    xMinChanged = Signal()
    xMaxChanged = Signal()

    yMin = Property(float, get_ymin, set_ymin)
    yMax = Property(float, get_ymax, set_ymax)
    xMin = Property(float, get_xmin, set_xmin)
    xMax = Property(float, get_xmax, set_xmax)

class HSpan(SpanBase):
    def __init__(self, parent=None):
        self._plot_obj = None
        super().__init__(parent)
        self._ymin = 0
        self._ymax = 1
        self._xmin = 0.0
        self._xmax = 1.0

        self._ax = None
   
    def init(self, ax):
        self._ax = ax
        self._plot_obj = self._ax.axhspan(self._ymin, self._ymax, self._xmin, self._xmax, **self.kwargs)

    
class VSpan(SpanBase):
    def __init__(self, parent=None):
        self._plot_obj = None
        super().__init__(parent)
        self._xmin = 0
        self._xmax = 0
        self._ymin = 0.0
        self._ymax = 1.0

        self._ax = None

    def init(self, ax):
        self._ax = ax
        self._plot_obj = self._ax.axvspan( self._xmin, self._xmax, self._ymin, self._ymax, **self.kwargs)


def init(factory):
    factory.register(HSpan, "Matplotlib")
    factory.register(VSpan, "Matplotlib")
