from PySide2.QtCore import QObject, Signal, Slot, Property
import numpy as np

from matplotlib_bridge.collections import PolyCollection
from matplotlib_bridge.event import EventHandler, EventTypes


# https://matplotlib.org/3.5.1/api/_as_gen/matplotlib.axes.Axes.fill_between.html
class FillBetween(PolyCollection):
    """ Wrapper class for matplotlib.axes.Axes.fill_between 
    This class has not been optimized yet. The Properties implemented by this class can't be modified efficiently at runtime.
    Instead the whole object is being deleted and recreated each time a property change is made. Properties implemented by parent classes
    are modifying the object directly without recreating it though.
    """

    def __init__(self, parent = None):
        super().__init__(parent)
        self._x = []
        self._y1 = []
        self._y2 = 0
        self._where = None
        self._interpolate = False
        self._step = None

        self._ax = None
        self._fill_between_event_handler = EventHandler() # private event handler to reinstantiate

    def init(self, ax):
        self._ax = ax        
        self._create_plot_obj(ax)
        self._fill_between_event_handler.register(EventTypes.PLOT_DATA_CHANGED, self.redraw)


    def _create_plot_obj(self, ax):
        kwargs = super().kwargs
        self._plot_obj = ax.fill_between(self._x, self._y1, y2 = self._y2, where = self._where,
                                        interpolate = self._interpolate, step = self._step, **kwargs)

    def redraw(self):
        """Delete the plot object and reinstantiate it"""
        if self._plot_obj is not None:
            self._plot_obj.remove()
            self._plot_obj = None
        self._create_plot_obj(self._ax)
        self._event_handler.schedule(EventTypes.PLOT_DATA_CHANGED)

    def _recalculate_polys(self):
        # TODO if "where" changed we might need to create more Polys, if it doesn't we can modify the existing ones
         pass

    def get_x(self):
        if self._plot_obj is None:
            return self._x
        return self._plot_obj.get_x()

    def set_x(self, x):
        self._x = x
        if self._plot_obj is not None:
            #self._plot_obj.set_x(self._x)
            self._fill_between_event_handler.schedule(EventTypes.PLOT_DATA_CHANGED)

    def get_y1(self):
        if self._plot_obj is None:
            return self._y1
        return self._plot_obj.get_y1()

    def set_y1(self, y1):
        self._y1 = y1
        if self._plot_obj is not None:
            #self._plot_obj.set_y1(self._y1)
            self._fill_between_event_handler.schedule(EventTypes.PLOT_DATA_CHANGED)

    def get_y2(self):
        if self._plot_obj is None:
            return self._y2
        return self._plot_obj.get_y2()

    def set_y2(self, y2):
        self._y2 = y2
        if self._plot_obj is not None:
            #self._plot_obj.set_y2(self._y2)
            self._fill_between_event_handler.schedule(EventTypes.PLOT_DATA_CHANGED)

    def get_where(self):
        if self._plot_obj is None:
            return self._where
        return self._plot_obj.get_where()

    def set_where(self, where):
        self._where = where
        if self._plot_obj is not None:
            #self._plot_obj.set_where(self._where)
            self._fill_between_event_handler.schedule(EventTypes.PLOT_DATA_CHANGED)

    def get_interpolate(self):
        if self._plot_obj is None:
            return self._interpolate
        return self._plot_obj.get_interpolate()

    def set_interpolate(self, interpolate):
        self._interpolate = interpolate
        if self._plot_obj is not None:
            #self._plot_obj.set_interpolate(self._interpolate)
            self._fill_between_event_handler.schedule(EventTypes.PLOT_DATA_CHANGED)

    def get_step(self):
        if self._plot_obj is None:
            return self._step
        return self._plot_obj.get_step()

    def set_step(self, step):
        self._step = step
        if self._plot_obj is not None:
            #self._plot_obj.set_step(self._step)
            self._fill_between_event_handler.schedule(EventTypes.PLOT_DATA_CHANGED)

    x = Property("QVariantList", get_x, set_x)
    y1 = Property("QVariantList", get_y1, set_y1)
    y2 = Property("QVariantList", get_y2, set_y2)
    where = Property("QVariantList", get_where, set_where)
    interpolate = Property(bool, get_interpolate, set_interpolate)
    step = Property(str, get_step, set_step)

def init(factory):
    factory.register(FillBetween, "Matplotlib")