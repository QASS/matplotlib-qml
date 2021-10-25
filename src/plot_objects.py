
import sys

from PySide2.QtQuick import QQuickItem
from PySide2.QtCore import QObject, Signal, Slot, Property

from matplotlib_backend_qtquick.backend_qtquick import (
    NavigationToolbar2QtQuick)
from matplotlib_backend_qtquick.backend_qtquickagg import (
    FigureCanvasQtQuickAgg)
from event import EventHandler, EventTypes

class Base(QObject):
    def __init__(self, parent = None):
        super().__init__(parent)
        self._event_handler = None
        self._plot_obj = None

    def add_event_handler(self, event_handler):
        self._event_handler = event_handler

    # def __setattr__(self, name: str, value):
    #     """Overwrite the setattr behaviour to redraw the whole figure
    #     every time a property is changed.
    #     """
    #     # is_property = False
    #     # if hasattr(self, name):
    #     #     is_property = isinstance(getattr(self, name), Property)

    #     if hasattr(self, "_initialized") and name != "initialized" and name != "_initialized":
    #         if hasattr(self, "figure_reference") and self._initialized:
    #             super().__setattr__(name, value)
    #             self.figure_reference.redraw()
    #         elif self._initialized:
    #             figure = self._find_figure()
    #             super().__setattr__("figure_reference", figure)
    #             super().__setattr__(name, value)
    #             figure.redraw()

    #     return super().__setattr__(name, value)

    # def _find_figure(self):
    #     """Search the figure which is supposed to always be the root of each
    #     Matplotlib QML Plot and return a reference to it's figure object"""
    #     def search(obj):
    #         if isinstance(obj, Figure):
    #             return obj
    #         if obj.parent() is None:
    #             raise LookupError("A Figure instance is supposed to be the root object of each plot")
    #         return search(obj.parent())

    #     return search(self)


class Figure(FigureCanvasQtQuickAgg):    
    """Root object for all QML matplotlib objects. Every other object that is a wrapper for
    Matplotlib must have a child relationship to an object of this class.
    The Figure and all of it's component can be customized with code from the Figure level. 
    The first time something on those components can be called is in the onCompleted Event of the Figure instance.
    
    In order to make sure the Figure is drawn, the onCOmpleted event must call Figure.init()::
        Figure {
            //Components here
            Component.onCompleted: {
                init()
            }
        }
    """
    def __init__(self, parent = None):
        super().__init__(parent)
        self._facecolor = "white"
        self._rows = 1
        self._columns = 1
        self._tight_layout = False
        self._event_handler = EventHandler()
    
    @Slot()
    def init(self):
        """Clears the whole figure and iterates over every child that is of instance :class:`Plot`.
        On each child the `init` function will be called providing the axis instance and the event_handler of the figure.
        This function should be called in When the Figure Component is Completed in QML.
        """
        self.figure.clear()
        for idx, child in enumerate(child for child in self.children() if isinstance(child, Plot)):
            ax = self.figure.add_subplot(self._rows, self._columns, idx + 1) 
            ax.set_autoscale_on(True)
            ax.autoscale_view(True,True,True)
            child.init(ax, self._event_handler)
        # call tight_layout function to prevent axis label clipping
        if self._tight_layout:
            self.figure.tight_layout()
        # This must register in the end because otherwise the plot will be drawn
        # before the axis can rescale
        self._event_handler.register(EventTypes.PLOT_DATA_CHANGED, self.redraw)
        self._event_handler.register(EventTypes.AXIS_DATA_CHANGED, self.redraw)
        self._event_handler.register(EventTypes.FIGURE_DATA_CHANGED, self.redraw)

    def redraw(self):
        self.figure.canvas.draw()

    def set_facecolor(self, color: str):
        self.figure.set_facecolor(color)

    def get_facecolor(self):
        return self._facecolor

    def get_rows(self):
        return self._rows

    def set_rows(self, rows):
        self._rows = rows

    def get_columns(self):
        return self._columns

    def set_columns(self, columns):
        self._columns = columns
        
    def get_tight_layout(self):
        return self._tight_layout
    
    def set_tight_layout(self, tight_layout):
        self._tight_layout = tight_layout
        if self._event_handler:
            self._event_handler.emit(EventTypes.FIGURE_DATA_CHANGED)


    faceColorChanged = Signal(str)

    faceColor = Property(str, get_facecolor, set_facecolor, notify=faceColorChanged)
    rows = Property(int, get_rows, set_rows)
    columns = Property(int, get_columns, set_columns)
    tightLayout = Property(bool, get_tight_layout, set_tight_layout)

class Plot(QQuickItem):
    """Container to allow useful implementation of mutliple axis."""
    def __init__(self, parent = None):
        super().__init__(parent)
        self._facecolor = "white"

    def init(self, ax, event_handler):
        """Retrieves all children of type :class:`Axis` and calls the draw method on them
        If the Plot object has multiple children it will hand them their own axis object """
        ax.set_facecolor(self._facecolor)
        axis_ = (child for child in self.children() if isinstance(child, Axis))
        for idx, axis in enumerate(axis_):
            # The first axis defines the main attributes of the plot and thus needs to be handled differently
            if idx == 0:
                axis.init(ax, event_handler)
                # check wether the axis object contains any labels to display
                handles, labels = ax.get_legend_handles_labels()
                if labels:
                    ax.legend()
                continue
            new_ax = ax.twinx()
            axis.init(new_ax, event_handler)
            # need to check the new axis as well
            # TODO this can be done with less code
            handles, labels = new_ax.get_legend_handles_labels()
            if labels:
                new_ax.legend()

    def get_facecolor(self):
        return self._facecolor

    def set_facecolor(self, color):
        self._facecolor = color

    faceColor = Property(str, get_facecolor, set_facecolor)

class Axis(QQuickItem):
    """Wrapper for matplotlib.pyplot.Axes"""
    def __init__(self, parent = None):
        super().__init__(parent)
        self._ax = None
        self._projection = "rectilinear"
        self._polar = False
        self._sharex = False
        self._sharey = False
        self._grid = False
        self._x_axis_label = ""
        self._x_axis_tick_color = "black"
        self._x_axis_label_color = "black"
        self._y_axis_label = ""
        self._y_axis_tick_color = "black"
        self._y_axis_label_color = "black"
        self._grid_color = "grey"
        self._grid_linestyle = "-"
        self._grid_linewidth = 1
        self._grid_alpha = 1.0

        self._autoscale = "both"
        self._xlim = [None, None] # left, right
        self._ylim = [None, None] # top, bottom


    def init(self, ax, event_handler):
        """Iterate over every children and call the plot method on those children
        The children define how they are plotted and are provided with an axis object
        they can modify. The QML children will be plotted first.
        
        :param ax: A Matplotlib axis object
        :type ax: Matplotlib.pyplot.Axes
        """
        self._event_handler = event_handler
        # Register for data change event and rescale the axis
        self._event_handler.register(EventTypes.PLOT_DATA_CHANGED, self._refresh)
        # Register for changes to the axis object
        self._event_handler.register(EventTypes.AXIS_DATA_CHANGED, self._apply_axis_settings)
        self._ax = ax
        # plot all children
        self._init_children(ax, event_handler)
        
        # apply all the axis settings
        self._apply_axis_settings()
        

    def _init_children(self, ax, event_handler):
        children = (child for child in self.children() if isinstance(child, Base)) # TODO change to PlotBase
        for child in children:
            # add the handler to the child
            child.add_event_handler(event_handler)
            child.init(ax)

    def _apply_axis_settings(self):
        if self._grid:
            self._ax.grid(color = self._grid_color, linestyle = self._grid_linestyle, 
            linewidth = self._grid_linewidth, alpha = self._grid_alpha)
        self._ax.set_axisbelow(True)
        self._ax.set_xlabel(self._x_axis_label)
        self._ax.tick_params(axis = "x", colors = self._x_axis_tick_color)
        self._ax.xaxis.label.set_color(self._x_axis_label_color)
        self._ax.set_ylabel(self._y_axis_label)
        self._ax.tick_params(axis = "y", colors = self._y_axis_tick_color)
        self._ax.yaxis.label.set_color(self._y_axis_label_color)
        self._ax.set_xlim(*self._xlim, emit = True)
        self._ax.set_ylim(*self._ylim, emit = True)
        self.set_autoscale(self._autoscale)

    def _refresh(self):
        """Rescales the axis to fit the current data lying on the axis. This is meant to be called by
        an EventHandler.
        The autoscaling is driven by the property "autoscale".
        """
        autoscale_behaviour = {
            "" : {"scalex" : False, "scaley" : False},
            "x" : {"scalex" : True, "scaley" : False},
            "y" : {"scalex" : False, "scaley" : True},
            "both" : {"scalex" : True, "scaley" : True},
        }
        # print(autoscale_behaviour[self._autoscale])
        self._ax.relim()        
        self._ax.autoscale_view(**autoscale_behaviour[self._autoscale])
        handles, labels = self._ax.get_legend_handles_labels()
        if labels:
            self._ax.legend()


    @Slot(float, float, bool, bool)
    @Slot(float, float)
    def set_xlim(self, xmin=None, xmax=None, emit=True, auto=False):
        self._ax.set_xlim(xmin, xmax, emit, auto)
        
    @Slot(float, float, bool, bool)
    @Slot(float, float)
    def set_ylim(self, ymin=None, ymax=None, emit=True, auto=False):
        self._ax.set_ylim(ymin, ymax, emit, auto)

    @Slot()
    def reset(self):
        """Resets an axis. This will reset only the graphs added by the interface and redraw the 
        Plot objects defined as children of the Axis in QML"""
        self._ax.clear()
        self.init(self._ax, self._event_handler)
        self._event_handler.emit(EventTypes.AXIS_DATA_CHANGED)

    @Slot("QVariantList", "QVariantList")
    @Slot("QVariantList", "QVariantList", "QVariantMap")
    def plot(self, x, y, kwargs = {}):
        """JS Interface for matpltolib.pyplot.axes.Axes.plot"""
        self._ax.plot(x, y, **kwargs)
        self._event_handler.emit(EventTypes.PLOT_DATA_CHANGED)

    @Slot("QVariantList", "QVariantList")
    @Slot("QVariantList", "QVariantList", "QVariantMap")
    def scatter(self, x, y, kwargs = {}):
        """JS Interface for matpltolib.pyplot.axes.Axes.scatter
        Scatter is faked by using the plot method with markers, without a linestyle"""
        if not "marker" in kwargs:
            kwargs["marker"] = "o"
        self._ax.plot(x, y, linestyle = " ", **kwargs)
        self._event_handler.emit(EventTypes.PLOT_DATA_CHANGED)

    @Slot(float)
    @Slot(float, "QVariantMap")
    def hline(self, y, kwargs = {}):
        self._ax.axhline(y, **kwargs)
        self._event_handler.emit(EventTypes.PLOT_DATA_CHANGED)

    @Slot(float)
    @Slot(float, "QVariantMap")
    def vline(self, x, kwargs = {}):
        self._ax.axvline(x, **kwargs)
        self._event_handler.emit(EventTypes.PLOT_DATA_CHANGED)

    @Slot(float, float)
    @Slot(float, float, "QVariantMap")
    def hspan(self, y_min, y_max, kwargs = {}):
        self._ax.axhspan(y_min, y_max, **kwargs)
        self._event_handler.emit(EventTypes.PLOT_DATA_CHANGED)

    @Slot(float, float)
    @Slot(float, float, "QVariantMap")
    def vspan(self, x_min, x_max, kwargs = {}):
        self._ax.axvspan(x_min, x_max, **kwargs)
        self._event_handler.emit(EventTypes.PLOT_DATA_CHANGED)


    def get_projection(self):
        return self._projection

    def set_projection(self, projection):
        self._projection = projection
        if self._ax is not None:
            self._event_handler.emit(EventTypes.AXIS_DATA_CHANGED)

    def get_polar(self):
        return self._polar

    def set_polar(self, polar):
        self._polar = polar
        if self._ax is not None:
            self._event_handler.emit(EventTypes.AXIS_DATA_CHANGED)

    def get_sharex(self):
        return self._sharex

    def set_sharex(self, sharex):
        self._sharex = sharex
        if self._ax is not None:
            self._event_handler.emit(EventTypes.AXIS_DATA_CHANGED)

    def get_sharey(self):
        return self._sharey

    def set_sharey(self, sharey):
        self._sharey = sharey
        if self._ax is not None:
            self._event_handler.emit(EventTypes.AXIS_DATA_CHANGED)

    def get_grid(self):
        return self._grid

    def set_grid(self, grid):
        self._grid = grid
        if self._ax is not None:
            self._event_handler.emit(EventTypes.AXIS_DATA_CHANGED)

    def get_x_axis_tick_color(self):
        return self._x_axis_tick_color

    def set_x_axis_tick_color(self, color):
        self._x_axis_tick_color = color
        if self._ax is not None:
            self._event_handler.emit(EventTypes.AXIS_DATA_CHANGED)

    def get_x_axis_label_color(self):
        return self._x_axis_label_color

    def set_x_axis_label_color(self, color):
        self._x_axis_label_color = color
        if self._ax is not None:
            self._event_handler.emit(EventTypes.AXIS_DATA_CHANGED)

    def get_x_axis_label(self):
        return self._x_axis_label

    def set_x_axis_label(self, color):
        self._x_axis_label = color
        if self._ax is not None:
            self._event_handler.emit(EventTypes.AXIS_DATA_CHANGED)

    def get_y_axis_tick_color(self):
        return self._y_axis_tick_color

    def set_y_axis_tick_color(self, color):
        self._y_axis_tick_color = color
        if self._ax is not None:
            self._event_handler.emit(EventTypes.AXIS_DATA_CHANGED)

    def get_y_axis_label_color(self):
        return self._y_axis_label_color

    def set_y_axis_label_color(self, color):
        self._y_axis_label_color = color
        if self._ax is not None:
            self._event_handler.emit(EventTypes.AXIS_DATA_CHANGED)

    def get_y_axis_label(self):
        return self._y_axis_label

    def set_y_axis_label(self, color):
        self._y_axis_label = color
        if self._ax is not None:
            self._event_handler.emit(EventTypes.AXIS_DATA_CHANGED)

    def get_grid_color(self):
        return self._grid_color

    def set_grid_color(self, color):
        self._grid_color = color
        if self._ax is not None:
            self._event_handler.emit(EventTypes.AXIS_DATA_CHANGED)

    def get_grid_linestyle(self):
        return self._grid_linestyle

    def set_grid_linestyle(self, linestyle):
        self._grid_linestyle = linestyle
        if self._ax is not None:
            self._event_handler.emit(EventTypes.AXIS_DATA_CHANGED)

    def get_grid_linewidth(self):
        return self._grid_linewidth

    def set_grid_linewidth(self, linewidth):
        self._grid_linewidth = linewidth
        if self._ax is not None:
            self._event_handler.emit(EventTypes.AXIS_DATA_CHANGED)

    def get_grid_alpha(self):
        return self._grid_alpha

    def set_grid_alpha(self, alpha):
        self._grid_alpha = alpha
        if self._ax is not None:
            self._event_handler.emit(EventTypes.AXIS_DATA_CHANGED)

    def get_autoscale(self):
        return self._autoscale

    def set_autoscale(self, autoscale : str):
        """Takes care of organizing which dimension is to be autoscaled. Valid arguments are ("both", "x", "y", "")
        False will turn off auto scaling.
        The function will deactivate autoscaling for all axis before applying the new autoscaling 
        setting. The previous setting will ALWAYS be overwritten!
        """
        if autoscale not in ("both", "x", "y", ""):
            raise ValueError("Autoscale can only be either 'both', 'x', 'y' or an empty string!")
        self._autoscale = autoscale
        if self._ax is not None:
            # First deactivate autoscaling on both axis
            self._ax.autoscale(enable = False)
            # If autoscale is false we deactivated autoscaling already and we can return 
            if self._autoscale == "":
                return
            # Now turn autoscaling on for the desired axis
            self._ax.autoscale(enable = True, axis = self._autoscale)

    def get_xmin(self):
        xmin, xmax = self._xlim
        return xmin

    def set_xmin(self, xmin: float):
        self._xlim[0] = xmin
        if self._ax is not None:
            self._ax.set_xlim(*self._xlim, auto = None)
            self._event_handler.emit(EventTypes.AXIS_DATA_CHANGED)

    def get_xmax(self):
        xmin, xmax = self._xlim
        return xmax

    def set_xmax(self, xmax: float):
        self._xlim[1] = xmax
        if self._ax is not None:
            self._ax.set_xlim(*self._xlim, auto = None)
            self._event_handler.emit(EventTypes.AXIS_DATA_CHANGED)

    def get_ymin(self):
        ymin, ymax = self._ylim
        return ymin

    def set_ymin(self, ymin: float):
        self._ylim[0] = ymin
        if self._ax is not None:
            self._ax.set_xlim(*self._ylim, auto = None)
            self._event_handler.emit(EventTypes.AXIS_DATA_CHANGED)

    def get_ymax(self):
        ymin, ymax = self._ylim
        return ymax

    def set_ymax(self, ymax: float):
        self._ylim[1] = ymax
        if self._ax is not None:
            self._ax.set_ylim(*self._xlim, auto = None)
            self._event_handler.emit(EventTypes.AXIS_DATA_CHANGED)

    projection = Property(str, get_projection, set_projection) 
    polar = Property(bool, get_polar, set_polar)
    sharex = Property(bool, get_sharex, set_sharex)
    sharey = Property(bool, get_sharey, set_sharey)
    grid = Property(bool, get_grid, set_grid)
    xAxisLabel = Property(str, get_x_axis_label, set_x_axis_label)
    xAxisTickColor = Property(str, get_x_axis_tick_color, set_x_axis_tick_color)
    xAxisLabelColor = Property(str, get_x_axis_label_color, set_x_axis_label_color)
    yAxisLabel = Property(str, get_y_axis_label, set_y_axis_label)
    yAxisTickColor = Property(str, get_y_axis_tick_color, set_y_axis_tick_color)
    yAxisLabelColor = Property(str, get_y_axis_label_color, set_y_axis_label_color)
    gridColor = Property(str, get_grid_color, set_grid_color)
    gridLinestyle = Property(str, get_grid_linestyle, set_grid_linestyle)
    gridLinewidth = Property(int, get_grid_linewidth, set_grid_linewidth)
    gridAlpha = Property(float, get_grid_alpha, set_grid_alpha)
    autoscale = Property(str, get_autoscale, set_autoscale)
    xMin = Property(float, get_xmin, set_xmin)
    xMax = Property(float, get_xmax, set_xmax)
    yMin = Property(float, get_ymin, set_ymin)
    yMax = Property(float, get_ymax, set_ymax)
