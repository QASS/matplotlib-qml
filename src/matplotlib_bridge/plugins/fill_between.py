from copy import copy
from PySide2.QtCore import QObject, Signal, Slot, Property
from matplotlib_bridge.graphs_2d import PlotObject2D
from matplotlib_bridge.plot_objects import Axis
from matplotlib_bridge.event import EventHandler, EventTypes

# https://matplotlib.org/3.5.1/api/_as_gen/matplotlib.axes.Axes.fill_between.html
class FillBetween(PlotObject2D):
    STEPS = ("pre", "post", "mid")

    def __init__(self, parent=None):
        super().__init__(parent)
        self._x = []
        self._y1 = []
        self._y2 = 0 #If provided via property this must be an array as the matplotlib documentation states
        self._where = None # boolean array
        self._interpolate = False
        self._step = None

        self._linestyle = "solid"
        self._linewidth = 1.0

        self._ax = None # reference to matplotlib axis

        self._fill_between_event_handler = EventHandler() # private event handler to reinstantiate

    def init(self, ax):
        self._ax = ax
        self._create_plot_obj(ax)

        self._fill_between_event_handler.register(EventTypes.PLOT_DATA_CHANGED, self.redraw)

    def _create_plot_obj(self, ax):
        self._plot_obj = ax.fill_between(self._x, self._y1, y2 = self._y2, where = self._where,
                                        interpolate = self._interpolate, step = self._step,
                                        linestyle = self._linestyle, linewidth = self._linewidth,
                                        **self.matplotlib_2d_kwargs)
    
    
    def redraw(self):
        """Delete the plot object and reinstantiate it"""
        if self._plot_obj is not None:
            self._plot_obj.remove()
            self._plot_obj = None
        self._create_plot_obj(self._ax)
        self._event_handler.schedule(EventTypes.PLOT_DATA_CHANGED)

    def get_x(self):
        return self._x

    def set_x(self, x):
        self._x = x
        if self._plot_obj is not None:
            pass

    def get_y1(self):
        return self._y1

    def set_y1(self, y1):
        self._y1 = y1
        if self._plot_obj is not None:
            self._fill_between_event_handler.schedule(EventTypes.PLOT_DATA_CHANGED)

    def get_y2(self):
        return self._y2

    def set_y2(self, y2):
        self._y2 = y2
        if self._plot_obj is not None:
            self._fill_between_event_handler.schedule(EventTypes.PLOT_DATA_CHANGED)

    def get_where(self):
        return self._where

    def set_where(self, where):
        self._where = where
        if self._plot_obj is not None:
            self._fill_between_event_handler.schedule(EventTypes.PLOT_DATA_CHANGED)

    def get_interpolate(self):
        return self._interpolate

    def set_interpolate(self, interpolate):
        self._interpolate = interpolate
        if self._plot_obj is not None:
            self._fill_between_event_handler.schedule(EventTypes.PLOT_DATA_CHANGED)

    def get_step(self):
        return self._step

    def set_step(self, step):
        self._step = step
        if self._plot_obj is not None:
            self._fill_between_event_handler.schedule(EventTypes.PLOT_DATA_CHANGED)

    def get_linestyle(self):
        return self._linestyle

    def set_linestyle(self, linestyle):
        self._linestyle = linestyle
        if self._plot_obj is not None:
            self._fill_between_event_handler.schedule(EventTypes.PLOT_DATA_CHANGED)
            #self._plot_obj.set_linestyle(self._linestyle)
            #self._event_handler.schedule(EventTypes.PLOT_DATA_CHANGED)


    def get_linewidth(self):
        return self._linewidth

    def set_linewidth(self, linewidth: float):
        self._linewidth = linewidth
        if self._plot_obj is not None:
            self._fill_between_event_handler.schedule(EventTypes.PLOT_DATA_CHANGED)
            # self._plot_obj.set_linewidth(self._linewidth)
            # self._event_handler.schedule(EventTypes.PLOT_DATA_CHANGED)

    x = Property("QVariantList", get_x, set_x)
    y1 = Property("QVariantList", get_y1, set_y1)
    y2 = Property("QVariantList", get_y2, set_y2)
    where = Property("QVariantList", get_where, set_where)
    interpolate = Property(str, get_interpolate, set_interpolate)
    step = Property(str, get_step, set_step)
    linestyle = Property(str, get_linestyle, set_linestyle)
    linewidth = Property(float, get_linewidth, set_linewidth)

def init(factory):
    factory.register(FillBetween, "Matplotlib")