from PySide2.QtCore import QObject, Signal, Slot, Property
import numpy as np

from matplotlib_qml.collections import PolyCollection
from matplotlib_qml.event import EventHandler, EventTypes
from matplotlib_qml.utils import numpy_compatibility


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

    def reinstantiate(emit_signal = None):
        """Returns a function (decorator)
        
        :param emit_signal: The signal name that should be emitted after the reinstantiation has been triggered
        :type emit_signal: string
        """
        def _reinstantiate(func):
            """Basic decorator to trigger reinstantiation of the bar container"""
            def wrapper(self, *args, **kwargs):
                result = func(self, *args, **kwargs)
                if self._plot_obj is not None:
                    self._fill_between_event_handler.schedule(EventTypes.PLOT_DATA_CHANGED)
                    # now check if a signal should be emitted and fetch it from the object
                    if emit_signal is not None:
                        try:
                            signal = getattr(self, emit_signal)
                        except:
                            raise ValueError(f"Signal {emit_signal} doesn't exist")
                        signal.emit()
                return result
            return wrapper
        return _reinstantiate

    def _recalculate_polys(self):
        # TODO if "where" changed we might need to create more Polys, if it doesn't we can modify the existing ones
         pass

    @numpy_compatibility
    def get_x(self):
        return self._x

    @reinstantiate(emit_signal = "xChanged")
    def set_x(self, x):
        self._x = x

    @numpy_compatibility
    def get_y1(self):
        return self._y1

    @reinstantiate(emit_signal = "y1Changed")
    def set_y1(self, y1):
        self._y1 = y1

    @numpy_compatibility
    def get_y2(self):
        return self._y2

    @reinstantiate(emit_signal = "y2Changed")
    def set_y2(self, y2):
        self._y2 = y2

    @numpy_compatibility
    def get_where(self):
        return self._where

    @reinstantiate(emit_signal = "whereChanged")
    def set_where(self, where):
        self._where = where

    def get_interpolate(self):
        return self._interpolate

    @reinstantiate(emit_signal = "interpolateChanged")
    def set_interpolate(self, interpolate):
        self._interpolate = interpolate

    def get_step(self):
        return self._step

    @reinstantiate(emit_signal = "stepChanged")
    def set_step(self, step):
        self._step = step

    xChanged = Signal()
    y1Changed = Signal()
    y2Changed = Signal()
    whereChanged = Signal()
    interpolateChanged = Signal()
    stepChanged = Signal()

    x = Property("QVariantList", get_x, set_x)
    y1 = Property("QVariantList", get_y1, set_y1)
    y2 = Property("QVariantList", get_y2, set_y2)
    where = Property("QVariantList", get_where, set_where)
    interpolate = Property(bool, get_interpolate, set_interpolate)
    step = Property(str, get_step, set_step)

def init(factory):
    factory.register(FillBetween, "Matplotlib")
