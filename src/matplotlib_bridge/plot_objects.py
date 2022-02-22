
import sys

from PySide2.QtQuick import QQuickItem
from PySide2.QtCore import QObject, Signal, Slot, Property, QTimer

from matplotlib_backend_qtquick.backend_qtquickagg import (
    FigureCanvasQtQuickAgg)
from matplotlib.ticker import AutoLocator

from matplotlib_bridge.event import EventHandler, EventTypes
from copy import copy

from matplotlib_backend_qtquick.backend_qtquick import NavigationToolbar2QtQuick

class Base(QObject):
    def __init__(self, parent = None):
        super().__init__(parent)
        self._event_handler = None
        self._plot_obj = None
        self._visible = True

    @property
    def plot_object(self):
        return self._plot_obj

    def set_event_handler(self, event_handler):
        self._event_handler = event_handler

    def get_visible(self):
        return self._visible

    def set_visible(self, visible):
        self._visible = visible
        if self._plot_obj is not None:
            self._plot_obj.set_visible(self._visible)
            self._event_handler.schedule(EventTypes.PLOT_DATA_CHANGED)

    visible = Property(bool, get_visible, set_visible)


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

    figure_events = ['resize_event', 
          'draw_event', 
          'key_press_event', 
          'key_release_event', 
          'button_press_event', 
          'button_release_event', 
          'scroll_event', 
          'motion_notify_event', 
          'pick_event', 
          'idle_event', 
          'figure_enter_event', 
          'figure_leave_event', 
          'axes_enter_event', 
          'axes_leave_event', 
          'close_event']

    def __init__(self, parent = None):
        super().__init__(parent)
        self._facecolor = "white"
        self._rows = 1
        self._columns = 1
        self._short_timer_interval = 20
        self._long_timer_interval = 100
        self._event_handler = None
        self._toolbar = NavigationToolbar2QtQuick(canvas = self.figure.canvas)
        self._coordinates = [0, 0]
        self._coordinates_timer_refresh_rate = 50

        self._coordinates_timer = QTimer()
        self._coordinates_timer.timeout.connect(self._emit_coordinates)
        self._coordinates_timer.setInterval(self._coordinates_timer_refresh_rate)
        self._coordinates_timer.setSingleShot(True)

    @Slot()
    def init(self):
        """Clears the whole figure and iterates over every child that is of instance :class:`Plot`.
        On each child the `init` function will be called providing the axis instance and the event_handler of the figure.
        This function should be called in When the Figure Component is Completed in QML.
        """
        self.figure.clear()
        self._event_handler = EventHandler(short_timer_interval = self._short_timer_interval, long_timer_interval = self._long_timer_interval)
        for idx, child in enumerate(child for child in self.children() if isinstance(child, Plot)):
            ax = self.figure.add_subplot(self._rows, self._columns, idx + 1)
            ax.set_autoscale_on(True)
            ax.autoscale_view(True,True,True)
            child.init(ax, self._event_handler)           
        
        # This must register in the end because otherwise the plot will be drawn
        # before the axis can rescale 
        self._event_handler.register(EventTypes.PLOT_DATA_CHANGED, self.redraw)
        self._event_handler.register(EventTypes.AXIS_DATA_CHANGED, self.redraw)
        self._event_handler.register(EventTypes.FIGURE_DATA_CHANGED, self.redraw)

        # connect the figure events
        self.figure.canvas.mpl_connect("motion_notify_event", self._on_motion)
        self.figure.canvas.mpl_connect("pick_event", self._on_pick)
        self.figure.canvas.mpl_connect("button_press_event", self._on_click)

    @Slot()
    def registerToolbar(self):
        """It might be beneficial to be able to register a custom Toolbar""" 
        raise NotImplementedError("This has not been implemented yet")        

    @Slot()
    def home(self, *args):
        self._toolbar.home(*args)

    @Slot()
    def back(self, *args):
        self._toolbar.back(*args)

    @Slot()
    def forward(self, *args):
        self._toolbar.forward(*args)

    @Slot()
    def pan(self, *args):
        """Activate the pan tool."""
        self._toolbar.pan(*args)

    @Slot()
    def zoom(self, *args):
        """activate zoom tool."""
        self._toolbar.zoom(*args)        

    @Slot("QVariantMap")
    def tightLayout(self, kwargs = {}):
        """Calling the tight_layout method on the figure

        kwargs can contain the following Keywords arguments
        pad = 1.08, h_pad=None, w_pad=None, rect=None
        """
        self.figure.tight_layout(**kwargs)
        if self._event_handler is not None:
            self._event_handler.schedule(EventTypes.FIGURE_DATA_CHANGED)

    def _on_motion(self, event):
        """This is a handler registered on the ' motion_notify_event' to refresh the mouse coordinates
        This event gets fired a lot and it is not necessary to emit all those events because that clogs
        up the event loop. Start a timer thatz will refresh the coordinates every 50ms (20 times/s)
        """
        # TODO this might need to move on the axis if we want to have per axis coords
        if self._coordinates_timer.isActive():
            return
        if event.ydata is None or event.xdata is None:
            return
        self._coordinates_timer.start()
        self._coordinates = [float(event.xdata), float(event.ydata)]
        self.coordinatesChanged.emit(self._coordinates)

    def _emit_coordinates(self):
        self.coordinatesChanged.emit(self._coordinates)
    
    def _on_pick(self, event):
        print(event)

    def _on_click(self, event):
        """Emits the clicked event that can be subscribed via 'onClicked' in QML providing
        The x and y coordinates of the mouse event"""
        mouse_click = {
            "x" : event.xdata,
            "y" : event.ydata
        }
        self.clicked.emit(mouse_click)

    def get_matplotlib_figure_object(self):
        """The supported way of retrieving the wrapped Matplotlib figure object"""
        return self.figure

    def redraw(self):
        self.figure.canvas.draw()

    def set_facecolor(self, color: str):
        self.figure.set_facecolor(color)
        if self._event_handler is not None:
            self._event_handler.schedule(EventTypes.FIGURE_DATA_CHANGED)

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

    def get_short_timer_interval(self):
        return self._short_timer_interval

    def set_short_timer_interval(self, interval):
        self._short_timer_interval = interval
        if self._event_handler is not None:
            self._event_handler.set_short_timer_interval(self._short_timer_interval)

    def get_long_timer_interval(self):
        return self._long_timer_interval

    def set_long_timer_interval(self, interval):
        self._long_timer_interval = interval
        if self._event_handler is not None:
            self._event_handler.set_long_timer_interval(self._long_timer_interval)

    def get_coordinates(self):
        return self._coordinates

    def get_coordinates_refresh_rate(self):
        return self._coordinates_timer_refresh_rate

    def set_coordinates_refresh_rate(self, refresh_rate):
        self._coordinates_timer_refresh_rate = refresh_rate
        self._coordinates_timer.setInterval(self._coordinates_timer_refresh_rate)


    faceColorChanged = Signal(str)
    coordinatesChanged = Signal("QVariantMap")
    clicked = Signal("QVariantMap")

    faceColor = Property(str, get_facecolor, set_facecolor, notify = faceColorChanged)
    rows = Property(int, get_rows, set_rows)
    columns = Property(int, get_columns, set_columns)
    shortTimerInterval = Property(int, get_short_timer_interval, set_short_timer_interval)
    longTimerInterval = Property(int, get_long_timer_interval, set_long_timer_interval)
    coordinates = Property("QVariantList", get_coordinates, notify = coordinatesChanged)
    coordinatesRefreshRate = Property(int, get_coordinates_refresh_rate, set_coordinates_refresh_rate)

class Plot(QQuickItem):
    """Container to allow useful implementation of mutliple axis."""
    def __init__(self, parent = None):
        super().__init__(parent)
        self._facecolor = "white"
        self._ax = None

    def init(self, ax, event_handler):
        """Retrieves all children of type :class:`Axis` and calls the draw method on them
        If the Plot object has multiple children it will hand them their own axis object """
        self._ax = ax
        self._event_handler = event_handler
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
        if self._ax is not None:
            self._ax.set_facecolor(self._facecolor)
            self._event_handler.schedule(EventTypes.FIGURE_DATA_CHANGED)

    faceColor = Property(str, get_facecolor, set_facecolor)

class Axis(QQuickItem):
    """Wrapper for matplotlib.pyplot.Axes"""

    SCALE = {"linear" : "linear", "log" : "log", "symlog" : "symlog", "logit" : "logit"}

    def __init__(self, parent = None):
        super().__init__(parent)
        self._ax = None
        self._legend = None
        self._event_handler = None
        self._xscale = "linear"
        self._yscale = "linear"
        self._projection = "rectilinear"
        self._polar = False
        self._sharex = False
        self._sharey = False
        self._grid = False
        self._x_axis_label = ""
        self._x_axis_label_fontsize = 12
        self._x_axis_tick_color = "black"
        self._x_axis_major_ticks = None
        self._x_axis_minor_ticks = None
        self._x_axis_label_color = "black"
        self._y_axis_label = ""
        self._y_axis_label_fontsize = 12
        self._y_axis_tick_color = "black"
        self._y_axis_major_ticks = None
        self._y_axis_minor_ticks = None
        self._y_axis_label_color = "black"
        self._grid_color = "grey"
        self._grid_linestyle = "-"
        self._grid_linewidth = 1
        self._grid_alpha = 1.0
        # self._legend_visible = True

        self._autoscale = "both"
        self._xlim = [None, None] # left, right
        self._ylim = [None, None] # top, bottom

        self._qml_children = [] # References to all the wrapper objects


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
            # set the handler on the child
            child.set_event_handler(event_handler)
            child.init(ax)
            self._qml_children.append(child)

    def _apply_axis_settings(self):
        """Apply the axes settings. This usually only needs to happen when the plot initializes
        The first time since the axes object will be modified in the setters of the different Propertys
        or Slots."""
        if self._grid:
            self._ax.grid(color = self._grid_color, linestyle = self._grid_linestyle, 
            linewidth = self._grid_linewidth, alpha = self._grid_alpha)
        self._ax.set_xscale(self._xscale)
        self._ax.set_yscale(self._yscale)
        self._ax.set_axisbelow(True)
        self._ax.set_xlabel(self._x_axis_label, fontsize = self._x_axis_label_fontsize)
        self._ax.tick_params(axis = "x", colors = self._x_axis_tick_color)
        self._ax.xaxis.label.set_color(self._x_axis_label_color)
        self._ax.set_ylabel(self._y_axis_label, fontsize = self._y_axis_label_fontsize)
        self._ax.tick_params(axis = "y", colors = self._y_axis_tick_color)
        self._ax.yaxis.label.set_color(self._y_axis_label_color)
        self._ax.set_xlim(*self._xlim, emit = True)
        self._ax.set_ylim(*self._ylim, emit = True)
        self._apply_auto_scale(self._autoscale)
        if self._x_axis_major_ticks is not None: # TODO add AutoLocator to allow resetting of ticks
            self._ax.set_xticks(self._x_axis_major_ticks, minor = False)
        if self._x_axis_minor_ticks is not None:
            self._ax.set_xticks(self._x_axis_minor_ticks, minor = True)
        if self._y_axis_major_ticks is not None:
            self._ax.set_yticks(self._y_axis_major_ticks, minor = False)
        if self._y_axis_minor_ticks is not None:
            self._ax.set_yticks(self._y_axis_minor_ticks, minor = True)

    def _refresh(self):
        """Rescales the axis to fit the current data lying on the axis. This is meant to be called by
        an EventHandler.
        The autoscaling is driven by the property "autoscale".
        """
        self._ax.relim()
        self._ax.autoscale_view()
        handles, labels = self._ax.get_legend_handles_labels()
        if labels: #and self._legend_visible:
            self._ax.legend()

    def _apply_auto_scale(self, autoscale):
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

    @property
    def ax(self):
        return self._ax

    def get_matplotlib_ax_object(self):
        """The supported way of retrieving the wrapped matplotlib axis
        
        :return: Matplotlib Axis object
        """
        return self._ax

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
        # get all children plot objects
        qml_plot_objects = [qml_child.plot_object for qml_child in self._qml_children]
        # check containers
        for container in copy(self._ax.containers):
            if container in qml_plot_objects:
                continue
            container.remove()
        # check images
        for image in copy(self._ax.images):
            if image in qml_plot_objects:
                continue
            image.remove()
        # check lines
        for line in copy(self._ax.lines):
            if line in qml_plot_objects:
                continue
            line.remove()
        self._event_handler.schedule(EventTypes.PLOT_DATA_CHANGED)

    @Slot("QVariantList", "QVariantList")
    @Slot("QVariantList", "QVariantList", "QVariantMap")
    def plot(self, x, y, kwargs = {}):
        """JS Interface for matpltolib.pyplot.axes.Axes.plot"""
        self._ax.plot(x, y, **kwargs)
        self._event_handler.schedule(EventTypes.PLOT_DATA_CHANGED)

    @Slot("QVariantList", "QVariantList")
    @Slot("QVariantList", "QVariantList", "QVariantMap")
    def scatter(self, x, y, kwargs = {}):
        """JS Interface for matpltolib.pyplot.axes.Axes.scatter
        Scatter is faked by using the plot method with markers, without a linestyle"""
        if not "marker" in kwargs:
            kwargs["marker"] = "o"
        self._ax.plot(x, y, linestyle = " ", **kwargs)
        self._event_handler.schedule(EventTypes.PLOT_DATA_CHANGED)

    @Slot(float)
    @Slot(float, "QVariantMap")
    def hline(self, y, kwargs = {}):
        self._ax.axhline(y, **kwargs)
        self._event_handler.schedule(EventTypes.PLOT_DATA_CHANGED)

    @Slot(float)
    @Slot(float, "QVariantMap")
    def vline(self, x, kwargs = {}):
        self._ax.axvline(x, **kwargs)
        self._event_handler.schedule(EventTypes.PLOT_DATA_CHANGED)

    @Slot(float, float)
    @Slot(float, float, "QVariantMap")
    def hspan(self, y_min, y_max, kwargs = {}):
        self._ax.axhspan(y_min, y_max, **kwargs)
        self._event_handler.schedule(EventTypes.PLOT_DATA_CHANGED)

    @Slot(float, float)
    @Slot(float, float, "QVariantMap")
    def vspan(self, x_min, x_max, kwargs = {}):
        self._ax.axvspan(x_min, x_max, **kwargs)
        self._event_handler.schedule(EventTypes.PLOT_DATA_CHANGED)

    @Slot(str, "QVariantMap")
    def tick_params(self, axis, kwargs):
        """setter for everything regarding the tick params of the axis. This will also 
        modify the corresponding propertys.
        
        :param axis: A string that identifies the axes to operate on
        :type axis: str
        :param kwargs: A dictionary (JS Object) with all the kwargs from the Axes.tick_params implementation from Matplotlib
        :type kwargs: dict | JS Object
        """
        self._ax.tick_params(axis = axis, **kwargs)
        # Update the Property variables so they are not lost
        # I'm using conditional assignments here to reduce code size
        # in principle a value is only assigned if the axis was set and if there is a value in kwargs
        self._x_axis_tick_color = kwargs.get("color", self._x_axis_tick_color) if axis == "both" or axis == "x" else self._x_axis_tick_color
        self._y_axis_tick_color = kwargs.get("color", self._y_axis_tick_color) if axis == "both" or axis == "y" else self._y_axis_tick_color
        self._x_axis_label_fontsize = kwargs.get("labelsize", self._x_axis_label_fontsize) if axis == "both" or axis == "x" else self._x_axis_label_fontsize
        self._y_axis_label_fontsize = kwargs.get("labelsize", self._y_axis_label_fontsize) if axis == "both" or axis == "y" else self._y_axis_label_fontsize
        self._x_axis_label_color = kwargs.get("labelcolor", self._x_axis_label_color) if axis == "both" or axis == "x" else self._x_axis_label_color
        self._y_axis_label_color = kwargs.get("labelcolor", self._y_axis_label_color) if axis == "both" or axis == "y" else self._y_axis_label_color
        self._x_axis_tick_color = kwargs.get("colors", self._x_axis_tick_color) if axis == "both" or axis == "x" else self._x_axis_tick_color
        self._y_axis_tick_color = kwargs.get("colors", self._y_axis_tick_color) if axis == "both" or axis == "y" else self._y_axis_tick_color
        self._x_axis_label_color = kwargs.get("colors", self._x_axis_label_color) if axis == "both" or axis == "x" else self._x_axis_label_color
        self._y_axis_label_color = kwargs.get("colors", self._y_axis_label_color) if axis == "both" or axis == "y" else self._y_axis_label_color
        self._grid_color = kwargs.get("grid_color", self._grid_color)
        self._grid_alpha = kwargs.get("grid_alpha", self._grid_alpha)
        self._grid_linewidth = kwargs.get("grid_linewidth", self._grid_linewidth)
        self._grid_linestyle = kwargs.get("grid_linestyle", self._grid_linestyle)
        
        # Emit the rerender event
        self._event_handler.schedule(EventTypes.AXIS_DATA_CHANGED)

    @Slot()
    def reset_x_ticks(self):
        """Sets all the ticks on the x axis to the AutoLocator.
        It will also reset the propertys xAxisMajorTicks and xAxisMinorTicks to None.
        resulting in them not influencing the axis"""
        self._ax.xaxis.set_major_locator(AutoLocator())
        self._ax.xaxis.set_minor_locator(AutoLocator())
        self._x_axis_major_ticks = None
        self._x_axis_minor_ticks = None
        self._event_handler.schedule(EventTypes.AXIS_DATA_CHANGED)

    @Slot()
    def reset_y_ticks(self):
        """Sets all the ticks on the x axis to the AutoLocator.
        It will also reset the propertys yAxisMajorTicks and yAxisMinorTicks to None.
        resulting in them not influencing the axis"""
        self._ax.yaxis.set_major_locator(AutoLocator())
        self._ax.yaxis.set_minor_locator(AutoLocator())
        self._y_axis_major_ticks = None
        self._y_axis_minor_ticks = None
        self._event_handler.schedule(EventTypes.AXIS_DATA_CHANGED)

    def get_xscale(self):
        return self._scale

    def set_xscale(self, xscale):
        """Check if the provided scale is valid and provide linear as fallback if necessary"""
        self._xscale = self.SCALE.get(xscale, "linear")
        if self._ax is not None:
            self._event_handler.schedule(EventTypes.AXIS_DATA_CHANGED)

    def get_yscale(self):
        return self._scale

    def set_yscale(self, yscale):
        """Check if the provided scale is valid and provide linear as fallback if necessary"""
        self._yscale = self.SCALE.get(yscale, "linear")
        if self._ax is not None:
            self._event_handler.schedule(EventTypes.AXIS_DATA_CHANGED)

    def get_projection(self):
        return self._projection

    def set_projection(self, projection):
        self._projection = projection
        if self._ax is not None:
            self._event_handler.schedule(EventTypes.AXIS_DATA_CHANGED)

    def get_polar(self):
        return self._polar

    def set_polar(self, polar):
        self._polar = polar
        if self._ax is not None:
            self._event_handler.schedule(EventTypes.AXIS_DATA_CHANGED)

    def get_sharex(self):
        return self._sharex

    def set_sharex(self, sharex):
        self._sharex = sharex
        if self._ax is not None:
            self._event_handler.schedule(EventTypes.AXIS_DATA_CHANGED)

    def get_sharey(self):
        return self._sharey

    def set_sharey(self, sharey):
        self._sharey = sharey
        if self._ax is not None:
            self._event_handler.schedule(EventTypes.AXIS_DATA_CHANGED)

    def get_grid(self):
        return self._grid

    def set_grid(self, grid):
        self._grid = grid
        if self._ax is not None:
            self._event_handler.schedule(EventTypes.AXIS_DATA_CHANGED)

    def get_x_axis_tick_color(self):
        return self._x_axis_tick_color

    def set_x_axis_tick_color(self, color):
        self._x_axis_tick_color = color
        if self._ax is not None:
            self._event_handler.schedule(EventTypes.AXIS_DATA_CHANGED)

    def get_x_axis_major_ticks(self):
        return self._x_axis_major_ticks

    def set_x_axis_major_ticks(self, xticks):
        self._x_axis_major_ticks = xticks
        if self._ax is not None:
            self._event_handler.schedule(EventTypes.AXIS_DATA_CHANGED)

    def get_x_axis_minor_ticks(self):
        return self._x_axis_minor_ticks

    def set_x_axis_minor_ticks(self, xticks):
        self._x_axis_minor_ticks = xticks
        if self._ax is not None:
            self._event_handler.schedule(EventTypes.AXIS_DATA_CHANGED)

    def get_x_axis_label_color(self):
        return self._x_axis_label_color

    def set_x_axis_label_color(self, color):
        self._x_axis_label_color = color
        if self._ax is not None:
            self._event_handler.schedule(EventTypes.AXIS_DATA_CHANGED)

    def get_x_axis_label(self):
        return self._x_axis_label

    def set_x_axis_label(self, color):
        self._x_axis_label = color
        if self._ax is not None:
            self._event_handler.schedule(EventTypes.AXIS_DATA_CHANGED)

    def get_x_axis_label_fontsize(self):
        return self._x_axis_label_fontsize

    def set_x_axis_label_fontsize(self, fontsize):
        self._x_axis_label_fontsize = fontsize
        if self._ax is not None:
            self._ax.set_xlabel(self._x_axis_label, fontsize = self._x_axis_label_fontsize)
            self._event_handler.schedule(EventTypes.AXIS_DATA_CHANGED)

    def get_y_axis_tick_color(self):
        return self._y_axis_tick_color

    def set_y_axis_tick_color(self, color):
        self._y_axis_tick_color = color
        if self._ax is not None:
            self._event_handler.schedule(EventTypes.AXIS_DATA_CHANGED)

    def get_y_axis_major_ticks(self):
        return self._y_axis_major_ticks

    def set_y_axis_major_ticks(self, yticks):
        self._y_axis_major_ticks = yticks
        if self._ax is not None:
            self._event_handler.schedule(EventTypes.AXIS_DATA_CHANGED)

    def get_y_axis_minor_ticks(self):
        return self._y_axis_minor_ticks

    def set_y_axis_minor_ticks(self, yticks):
        self._y_axis_minor_ticks = yticks
        if self._ax is not None:
            self._event_handler.schedule(EventTypes.AXIS_DATA_CHANGED)

    def get_y_axis_label_color(self):
        return self._y_axis_label_color

    def set_y_axis_label_color(self, color):
        self._y_axis_label_color = color
        if self._ax is not None:
            self._event_handler.schedule(EventTypes.AXIS_DATA_CHANGED)

    def get_y_axis_label(self):
        return self._y_axis_label

    def set_y_axis_label(self, color):
        self._y_axis_label = color
        if self._ax is not None:
            self._event_handler.schedule(EventTypes.AXIS_DATA_CHANGED)

    def get_y_axis_label_fontsize(self):
        return self._y_axis_label_fontsize

    def set_y_axis_label_fontsize(self, fontsize):
        self._y_axis_label_fontsize = fontsize
        if self._ax is not None:
            self._ax.set_ylabel(self._y_axis_label, fontsize = self._y_axis_label_fontsize)
            self._event_handler.schedule(EventTypes.AXIS_DATA_CHANGED)

    def get_grid_color(self):
        return self._grid_color

    def set_grid_color(self, color):
        self._grid_color = color
        if self._ax is not None:
            self._event_handler.schedule(EventTypes.AXIS_DATA_CHANGED)

    def get_grid_linestyle(self):
        return self._grid_linestyle

    def set_grid_linestyle(self, linestyle):
        self._grid_linestyle = linestyle
        if self._ax is not None:
            self._event_handler.schedule(EventTypes.AXIS_DATA_CHANGED)

    def get_grid_linewidth(self):
        return self._grid_linewidth

    def set_grid_linewidth(self, linewidth):
        self._grid_linewidth = linewidth
        if self._ax is not None:
            self._event_handler.schedule(EventTypes.AXIS_DATA_CHANGED)

    def get_grid_alpha(self):
        return self._grid_alpha

    def set_grid_alpha(self, alpha):
        self._grid_alpha = alpha
        if self._ax is not None:
            self._event_handler.schedule(EventTypes.AXIS_DATA_CHANGED)

    def get_autoscale(self):
        return self._autoscale

    def set_autoscale(self, autoscale : str):
        """Takes care of organizing which dimension is to be autoscaled. Valid arguments are ("both", "x", "y", "")
        False will turn off auto scaling.
        The function will deactivate autoscaling for all axis before applying the new autoscaling 
        setting. The previous setting will ALWAYS be overwritten!
        """
        self._apply_auto_scale(autoscale)           
        if self._event_handler is not None:     
            self._event_handler.schedule(EventTypes.AXIS_DATA_CHANGED)

    def get_xmin(self):
        xmin, xmax = self._xlim
        return xmin

    def set_xmin(self, xmin: float):
        self._xlim[0] = xmin
        if self._ax is not None:
            self._ax.set_xlim(*self._xlim, auto = None)
            self._event_handler.schedule(EventTypes.AXIS_DATA_CHANGED)

    def get_xmax(self):
        xmin, xmax = self._xlim
        return xmax

    def set_xmax(self, xmax: float):
        self._xlim[1] = xmax
        if self._ax is not None:
            self._ax.set_xlim(*self._xlim, auto = None)
            self._event_handler.schedule(EventTypes.AXIS_DATA_CHANGED)

    def get_ymin(self):
        ymin, ymax = self._ylim
        return ymin

    def set_ymin(self, ymin: float):
        """Sets the lower (bottom) y limit of the axes object"""
        self._ylim[0] = ymin
        if self._ax is not None:
            self._ax.set_xlim(*self._ylim, auto = None)
            self._event_handler.schedule(EventTypes.AXIS_DATA_CHANGED)

    def get_ymax(self):
        ymin, ymax = self._ylim
        return ymax

    def set_ymax(self, ymax: float):
        """Sets the upper (top) y limit of the axes object"""
        self._ylim[1] = ymax
        if self._ax is not None:
            self._ax.set_ylim(*self._xlim, auto = None)
            self._event_handler.schedule(EventTypes.AXIS_DATA_CHANGED)

    # def get_legend_visible(self):
    #     return self._legend_visible

    # def set_legend_visible(self, visible):
    #     self._legend_visible = visible
    #     # fetch the legend if there is one
    #     self._legend = self._ax.get_legend()
    #     if self._event_handler is not None and self._legend is not None:
    #         self._legend.set_visible(self._legend_visible)
    #         self._event_handler.schedule(EventTypes.AXIS_DATA_CHANGED)

    xScale = Property(str, get_xscale, set_xscale)
    yScale = Property(str, get_yscale, set_yscale)
    projection = Property(str, get_projection, set_projection) 
    polar = Property(bool, get_polar, set_polar)
    sharex = Property(bool, get_sharex, set_sharex)
    sharey = Property(bool, get_sharey, set_sharey)
    grid = Property(bool, get_grid, set_grid)
    xAxisLabel = Property(str, get_x_axis_label, set_x_axis_label)
    xAxisLabelFontSize = Property(int, get_x_axis_label_fontsize, set_x_axis_label_fontsize)
    xAxisMajorTicks = Property("QVariantList", get_x_axis_major_ticks, set_x_axis_major_ticks)
    xAxisMinorTicks = Property("QVariantList", get_x_axis_minor_ticks, set_x_axis_minor_ticks)
    xAxisTickColor = Property(str, get_x_axis_tick_color, set_x_axis_tick_color)
    xAxisLabelColor = Property(str, get_x_axis_label_color, set_x_axis_label_color)
    yAxisLabel = Property(str, get_y_axis_label, set_y_axis_label)
    yAxisLabelFontSize = Property(int, get_y_axis_label_fontsize, set_y_axis_label_fontsize)
    yAxisTickColor = Property(str, get_y_axis_tick_color, set_y_axis_tick_color)
    yAxisMajorTicks = Property("QVariantList", get_y_axis_major_ticks, set_y_axis_major_ticks)
    yAxisMinorTicks = Property("QVariantList", get_y_axis_minor_ticks, set_y_axis_minor_ticks)
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
    #legend = Property(bool, get_legend_visible, set_legend_visible)