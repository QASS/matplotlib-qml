from PySide2.QtCore import QObject, Signal, Slot, Property

from matplotlib_bridge.event import EventHandler, EventTypes
from matplotlib_bridge.plot_objects import Base


class Bar(Base):
    """ This is class has been auto generated. PLEASE PROVIDE DOCUMENTATION!!! """

    def __init__(self, parent = None):
        super().__init__(parent)
        self._x = []
        self._height = []
        self._whidths = None
        self._width = 0.8
        self._bottoms = None
        self._bottom = 0
        self._align = "center"
        self._colors = None
        self._color = None
        self._edgecolors = None
        self._edgecolor = None
        self._linewidths = None
        self._linewidth = None
        self._tick_label = None
        self._xerr = None
        self._yerr = None
        self._ecolors = None
        self._ecolor = "black"
        self._capsize = 0.0
        self._error_kw = dict()
        self._log = False
        self._alpha = None

        self._plot_obj = None
        self._ax = None
        self._bar_event_handler = EventHandler()

    def init(self, ax):
        self._ax = ax
        self._create_plot_obj(ax)
        self._bar_event_handler.register(EventTypes.PLOT_DATA_CHANGED, self.redraw)

    def _create_plot_obj(self, ax):
        kwargs = {
			"width": self._whidths if self.whidths is not None else self._width, 
			"bottom": self._bottoms if self._bottoms is not None else self._bottom,
			"align": self._align,			
			"color": self._colors if self._colors is not None else self.color,
			"edgecolor": self._edgecolors if self._edgecolors is not None else self._edgecolor,
			"linewidth": self._linewidths if self._linewidths is not None else self._linewidth,
			"tick_label": self._tick_label,
			"xerr": self._xerr,
			"yerr": self._xerr,
			"ecolor": self._ecolors if self._ecolors is not None else self._ecolor,
			"capsize": self._capsize,
			"error_kw": self._error_kw,
			"log": self._log,
			"alpha": self._alpha
        }
        self._plot_obj = ax.bar(self._x, self._height, **kwargs)

    def redraw(self):
        """Delete the plot object and reinstantiate it"""
        if self._plot_obj is not None:
            self._plot_obj.remove()
            self._plot_obj = None
        self._create_plot_obj(self._ax)
        self._event_handler.schedule(EventTypes.PLOT_DATA_CHANGED)

    def get_x(self):
        if self._plot_obj is None:
            return self._x
        return self._plot_obj.get_x()

    def set_x(self, x):
        self._x = x
        if self._plot_obj is not None:
            self._bar_event_handler.schedule(EventTypes.PLOT_DATA_CHANGED)

    def get_height(self):
        return self._height

    def set_height(self, height):
        self._height = height
        if self._plot_obj is not None:
            self._bar_event_handler.schedule(EventTypes.PLOT_DATA_CHANGED)

    def get_whidths(self):
        return self._whidths

    def set_whidths(self, whidths):
        self._whidths = whidths
        if self._plot_obj is not None:
            self._bar_event_handler.schedule(EventTypes.PLOT_DATA_CHANGED)

    def get_width(self):
        return self._width

    def set_width(self, width):
        self._width = width
        if self._plot_obj is not None:
            self._bar_event_handler.schedule(EventTypes.PLOT_DATA_CHANGED)

    def get_bottoms(self):
        return self._bottoms

    def set_bottoms(self, bottoms):
        self._bottoms = bottoms
        if self._plot_obj is not None:
            self._bar_event_handler.schedule(EventTypes.PLOT_DATA_CHANGED)

    def get_bottom(self):
        return self._bottom

    def set_bottom(self, bottom):
        self._bottom = bottom
        if self._plot_obj is not None:
            self._bar_event_handler.schedule(EventTypes.PLOT_DATA_CHANGED)

    def get_align(self):
        return self._align

    def set_align(self, align):
        self._align = align
        if self._plot_obj is not None:
            self._bar_event_handler.schedule(EventTypes.PLOT_DATA_CHANGED)

    def get_colors(self):
        return self._colors

    def set_colors(self, colors):
        self._colors = colors
        if self._plot_obj is not None:
            self._bar_event_handler.schedule(EventTypes.PLOT_DATA_CHANGED)

    def get_color(self):
        return self._color

    def set_color(self, color):
        self._color = color
        if self._plot_obj is not None:
            self._bar_event_handler.schedule(EventTypes.PLOT_DATA_CHANGED)

    def get_edgecolors(self):
        return self._edgecolors

    def set_edgecolors(self, edgecolors):
        self._edgecolors = edgecolors
        if self._plot_obj is not None:
            self._bar_event_handler.schedule(EventTypes.PLOT_DATA_CHANGED)

    def get_edgecolor(self):
        return self._edgecolor

    def set_edgecolor(self, edgecolor):
        self._edgecolor = edgecolor
        if self._plot_obj is not None:
            self._bar_event_handler.schedule(EventTypes.PLOT_DATA_CHANGED)

    def get_linewidths(self):
        return self._linewidths

    def set_linewidths(self, linewidths):
        self._linewidths = linewidths
        if self._plot_obj is not None:
            self._bar_event_handler.schedule(EventTypes.PLOT_DATA_CHANGED)

    def get_linewidth(self):
        return self._linewidth

    def set_linewidth(self, linewidth):
        self._linewidth = linewidth
        if self._plot_obj is not None:
            self._bar_event_handler.schedule(EventTypes.PLOT_DATA_CHANGED)

    def get_tick_label(self):
        return self._tick_label

    def set_tick_label(self, tick_label):
        self._tick_label = tick_label
        if self._plot_obj is not None:
            self._bar_event_handler.schedule(EventTypes.PLOT_DATA_CHANGED)

    def get_xerr(self):
        return self._xerr

    def set_xerr(self, xerr):
        self._xerr = xerr
        if self._plot_obj is not None:
            self._bar_event_handler.schedule(EventTypes.PLOT_DATA_CHANGED)

    def get_yerr(self):
        return self._yerr

    def set_yerr(self, yerr):
        self._yerr = yerr
        if self._plot_obj is not None:
            self._bar_event_handler.schedule(EventTypes.PLOT_DATA_CHANGED)

    def get_ecolors(self):
        return self._ecolors

    def set_ecolors(self, ecolors):
        self._ecolors = ecolors
        if self._plot_obj is not None:
            self._bar_event_handler.schedule(EventTypes.PLOT_DATA_CHANGED)

    def get_ecolor(self):
        return self._ecolor

    def set_ecolor(self, ecolor):
        self._ecolor = ecolor
        if self._plot_obj is not None:
            self._bar_event_handler.schedule(EventTypes.PLOT_DATA_CHANGED)

    def get_capsize(self):
        return self._capsize

    def set_capsize(self, capsize):
        self._capsize = capsize
        if self._plot_obj is not None:
            self._bar_event_handler.schedule(EventTypes.PLOT_DATA_CHANGED)

    def get_error_kw(self):
        return self._error_kw

    def set_error_kw(self, error_kw):
        self._error_kw = error_kw
        if self._plot_obj is not None:
            self._bar_event_handler.schedule(EventTypes.PLOT_DATA_CHANGED)

    def get_log(self):
        return self._log

    def set_log(self, log):
        self._log = log
        if self._plot_obj is not None:
            self._bar_event_handler.schedule(EventTypes.PLOT_DATA_CHANGED)

    def get_alpha(self):
        return self._alpha

    def set_alpha(self, alpha):
        self._alpha = alpha
        if self._plot_obj is not None:
            self._bar_event_handler.schedule(EventTypes.PLOT_DATA_CHANGED)

    x = Property("QVariantList", get_x, set_x)
    height = Property("QVariantList", get_height, set_height)
    whidths = Property("QVariantList", get_whidths, set_whidths)
    width = Property(float, get_width, set_width)
    bottoms = Property("QVariantList", get_bottoms, set_bottoms)
    bottom = Property(float, get_bottom, set_bottom)
    align = Property(str, get_align, set_align)
    colors = Property("QVariantList", get_colors, set_colors)
    color = Property(str, get_color, set_color)
    edgecolors = Property("QVariantList", get_edgecolors, set_edgecolors)
    edgecolor = Property(str, get_edgecolor, set_edgecolor)
    linewidths = Property("QVariantList", get_linewidths, set_linewidths)
    linewidth = Property(str, get_linewidth, set_linewidth)
    tick_label = Property("QVariantList", get_tick_label, set_tick_label)
    xerr = Property("QVariantList", get_xerr, set_xerr)
    yerr = Property("QVariantList", get_yerr, set_yerr)
    ecolors = Property("QVariantList", get_ecolors, set_ecolors)
    ecolor = Property(str, get_ecolor, set_ecolor)
    capsize = Property(float, get_capsize, set_capsize)
    error_kw = Property("QVariantMap", get_error_kw, set_error_kw)
    log = Property(bool, get_log, set_log)
    alpha = Property(float, get_alpha, set_alpha)

def init(factory):
    factory.register(Bar, "Matplotlib")