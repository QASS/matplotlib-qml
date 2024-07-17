from PySide2.QtCore import QObject, Signal, Slot, Property

from matplotlib_qml.event import EventHandler, EventTypes
from matplotlib_qml.plot_objects import Base
from matplotlib_qml.utils import numpy_compatibility

class Bar(Base):
    """ Wrapper for matplotlib.axes.Axes.bar
    
    the bar method returns a BarContainer which contains an errorbar container and an array of patches.
    This creates the need to recreate the whole  container whenever a property changes which causes a lot of overhead.
     """

    def __init__(self, parent = None):
        super().__init__(parent) # TODO vmin vmax
        self._x = []
        self._height = []
        self._widths = None
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
        self._label = None

        self._plot_obj = None
        self._ax = None
        self._bar_event_handler = EventHandler()

    def init(self, ax):
        self._ax = ax
        self._create_plot_obj(ax)
        self._bar_event_handler.register(EventTypes.PLOT_DATA_CHANGED, self.redraw)

    def _create_plot_obj(self, ax):
        kwargs = {
            "width": self._widths if self.widths is not None else self._width, 
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
            "alpha": self._alpha,
            "label": self._label
        }
        self._plot_obj = ax.bar(self._x, self._height, **kwargs)

    def redraw(self):
        """Delete the plot object and reinstantiate it"""
        if self._plot_obj is not None:
            if self._plot_obj.errorbar is not None:
                self._plot_obj.errorbar.remove()
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
                    self._bar_event_handler.schedule(EventTypes.PLOT_DATA_CHANGED)
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

    @numpy_compatibility
    def get_x(self):
            return self._x

    @reinstantiate(emit_signal = "xChanged")
    def set_x(self, x):
        self._x = x

    @numpy_compatibility
    def get_height(self):
        return self._height

    @reinstantiate(emit_signal = "heightChanged")
    def set_height(self, height):
        self._height = height

    @numpy_compatibility
    def get_widths(self):
        return self._widths

    @reinstantiate(emit_signal = "widthsChanged")
    def set_widths(self, widths):
        self._widths = widths

    @numpy_compatibility
    def get_width(self):
        return self._width

    @reinstantiate(emit_signal = "widthChanged")
    def set_width(self, width):
        self._width = width

    @numpy_compatibility
    def get_bottoms(self):
        return self._bottoms

    @reinstantiate(emit_signal = "bottomsChanged")
    def set_bottoms(self, bottoms):
        self._bottoms = bottoms

    @numpy_compatibility
    def get_bottom(self):
        return self._bottom

    @reinstantiate(emit_signal = "bottomChanged")
    def set_bottom(self, bottom):
        self._bottom = bottom

    def get_align(self):
        return self._align

    @reinstantiate(emit_signal = "alignChanged")
    def set_align(self, align):
        self._align = align

    @numpy_compatibility
    def get_colors(self):
        return self._colors

    @reinstantiate(emit_signal = "colorsChanged")
    def set_colors(self, colors):
        self._colors = colors

    @numpy_compatibility
    def get_color(self):
        return self._color

    @reinstantiate(emit_signal = "colorChanged")
    def set_color(self, color):
        self._color = color

    @numpy_compatibility
    def get_edgecolors(self):
        return self._edgecolors

    @reinstantiate(emit_signal = "edgecolorsChanged")
    def set_edgecolors(self, edgecolors):
        self._edgecolors = edgecolors

    @numpy_compatibility
    def get_edgecolor(self):
        return self._edgecolor

    @reinstantiate(emit_signal = "edgecolorChanged")
    def set_edgecolor(self, edgecolor):
        self._edgecolor = edgecolor

    @numpy_compatibility
    def get_linewidths(self):
        return self._linewidths

    @reinstantiate(emit_signal = "linewidthsChanged")
    def set_linewidths(self, linewidths):
        self._linewidths = linewidths

    @numpy_compatibility
    def get_linewidth(self):
        return self._linewidth

    @reinstantiate(emit_signal = "linewidthChanged")
    def set_linewidth(self, linewidth):
        self._linewidth = linewidth

    def get_tick_label(self):
        return self._tick_label

    @reinstantiate(emit_signal = "tickLabelsChanged")
    def set_tick_label(self, tick_label):
        self._tick_label = tick_label

    @numpy_compatibility
    def get_xerr(self):
        return self._xerr

    @reinstantiate(emit_signal = "xerrChanged")
    def set_xerr(self, xerr):
        self._xerr = xerr

    @numpy_compatibility
    def get_yerr(self):
        return self._yerr

    @reinstantiate(emit_signal = "yerrChanged")
    def set_yerr(self, yerr):
        self._yerr = yerr

    def get_ecolors(self):
        return self._ecolors

    @reinstantiate(emit_signal = None)
    def set_ecolors(self, ecolors):
        self._ecolors = ecolors

    def get_ecolor(self):
        return self._ecolor

    @reinstantiate(emit_signal = "ecolorChanged")
    def set_ecolor(self, ecolor):
        self._ecolor = ecolor

    @numpy_compatibility
    def get_capsize(self):
        return self._capsize

    @reinstantiate(emit_signal = "capsizeChanged")
    def set_capsize(self, capsize):
        self._capsize = capsize

    def get_error_kw(self):
        return self._error_kw

    @reinstantiate(emit_signal = "error_kwChanged")
    def set_error_kw(self, error_kw):
        self._error_kw = error_kw

    def get_log(self):
        return self._log

    @reinstantiate(emit_signal = None)
    def set_log(self, log):
        self._log = log

    @numpy_compatibility
    def get_alpha(self):
        return self._alpha

    @reinstantiate(emit_signal = "alphaChanged")
    def set_alpha(self, alpha):
        self._alpha = alpha

    def get_label(self):
        return self._label

    @reinstantiate(emit_signal = "labelChanged")
    def set_label(self, label):
        self._label = label

    xChanged = Signal()
    heightChanged = Signal()
    widthsChanged = Signal()
    widthChanged = Signal()
    bottomsChanged = Signal()
    bottomChanged = Signal()
    alignChanged = Signal()
    colorsChanged = Signal()
    colorChanged = Signal()
    edgecolorsChanged = Signal()
    edgecolorChanged = Signal()
    linewidthsChanged = Signal()
    linewidthChanged = Signal()
    tickLabelsChanged = Signal()
    xerrChanged = Signal()
    yerrChanged = Signal()
    ecolorChanged = Signal()
    capsizeChanged = Signal()
    error_kwChanged = Signal()
    alphaChanged = Signal()
    labelChanged = Signal()

    x = Property("QVariantList", get_x, set_x)
    height = Property("QVariantList", get_height, set_height)
    widths = Property("QVariantList", get_widths, set_widths)
    width = Property(float, get_width, set_width)
    bottoms = Property("QVariantList", get_bottoms, set_bottoms)
    bottom = Property(float, get_bottom, set_bottom)
    align = Property(str, get_align, set_align)
    colors = Property("QVariantList", get_colors, set_colors)
    color = Property(str, get_color, set_color)
    edgecolors = Property("QVariantList", get_edgecolors, set_edgecolors)
    edgecolor = Property(str, get_edgecolor, set_edgecolor)
    linewidths = Property("QVariantList", get_linewidths, set_linewidths)
    linewidth = Property(float, get_linewidth, set_linewidth)
    tickLabels = Property("QVariantList", get_tick_label, set_tick_label)
    xerr = Property("QVariantList", get_xerr, set_xerr)
    yerr = Property("QVariantList", get_yerr, set_yerr)
    # ecolors = Property("QVariantList", get_ecolors, set_ecolors) # TODO colors would need to be provided as a list of RGB tuples
    ecolor = Property(str, get_ecolor, set_ecolor)
    capsize = Property(float, get_capsize, set_capsize)
    error_kw = Property("QVariantMap", get_error_kw, set_error_kw)
    # log = Property(bool, get_log, set_log) # TODO causes anomalies on the axis when changed
    alpha = Property(float, get_alpha, set_alpha)
    label = Property(str, get_label, set_label)

def init(factory):
    factory.register(Bar, "Matplotlib")
