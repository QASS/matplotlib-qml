from PySide2.QtQuick import QQuickItem
from PySide2.QtCore import QObject, Signal, Slot, Property
from copy import copy

from plot_objects import Base, Figure
from event import EventTypes



class PlotObject2D(Base):
    """Implements all Propertys from 2D Plot objects that live within an axis"""
    def __init__(self, parent = None):
        super().__init__(parent)
        self._alpha = 1.0
        self._color = None
        self._label = ""
        

    @property
    def matplotlib_2d_kwargs(self):
        attributes = {
            "alpha" : self._alpha,
            "color" : self._color,
            "label" : self._label
        }
        return attributes

    def update():
        pass

    def get_label(self):
        return self._label

    def set_label(self, label):
        self._label = label

    def get_alpha(self):
        return self._alpha

    def set_alpha(self, alpha):
        self._alpha = alpha

    def get_color(self):
        return self._color

    def set_color(self, color):
        self._color = color

    def init(self, ax):
        raise NotImplementedError("This method needs to be implemented by the programmer!")

    
    alpha = Property(float, get_alpha, set_alpha)
    color = Property(str, get_color, set_color)
    label = Property(str, get_label, set_label)


class GraphObject2D(PlotObject2D):
    """Implements Propertys from 2D Graph objects like scatters, lines, spans"""
    def __init__(self, parent = None):
        super().__init__(parent)
        self._xdata = []
        self._ydata = []
        # The plot object is the object being wrapped (i.e. the matplotlib object)

    @property
    def xData(self):
        return self._xdata

    @property
    def yData(self):
        return self._ydata

    @Slot(int)
    @Slot(int, float)
    def randomData(self, length, upper_limit = 1.0):
        from numpy import random, arange
        self.set_ydata(random.rand(length) * upper_limit)
        self.set_xdata(arange(len(self._ydata)))
        self._event_handler.schedule(EventTypes.PLOT_DATA_CHANGED)
        # self._plot_obj.figure.canvas.draw()
        # TODO update the plot objects here

    def set_xdata(self, xdata: list):
        self._xdata = copy(xdata)
        if self._plot_obj is not None:
            self._plot_obj.set_xdata(self._xdata)
            # only emit the event if both shapes are correct
            if len(self._xdata) == len(self._ydata):
                self._event_handler.schedule(EventTypes.PLOT_DATA_CHANGED)


    def get_xdata(self):
        return self._xdata

    def set_ydata(self, ydata: list):
        self._ydata = copy(ydata)
        if self._plot_obj is not None:
            self._plot_obj.set_ydata(self._ydata)
            # only emit the event if both shapes are correct
            if len(self._xdata) == len(self._ydata):
                self._event_handler.schedule(EventTypes.PLOT_DATA_CHANGED)

    def get_ydata(self):
        return self._ydata

    xData = Property("QVariantList", get_xdata, set_xdata)
    yData = Property("QVariantList", get_ydata, set_ydata)

class LineObject2D(GraphObject2D):
    """Implements Propertys from any Line item"""
    def __init__(self, parent = None):
        super().__init__(parent)
        self._linestyle = None
        self._linewidth = 1.0

    @property
    def matplotlib_2d_kwargs(self):
        attributes = super().matplotlib_2d_kwargs
        attributes["linestyle"] = self._linestyle 
        attributes["linewidth"] = self._linewidth
        return attributes
    
    def get_linestyle(self):
        return self._linestyle

    def set_linestyle(self, linestyle):
        self._linestyle = linestyle

    def get_linewidth(self):
        return self._linewidth

    def set_linewidth(self, linewidth: float):
        self._linewidth = linewidth

    linestyle = Property(str, get_linestyle, set_linestyle)
    linewidth = Property(float, get_linewidth, set_linewidth)

class Line(LineObject2D):
    """wrapper for matplotlib.pyplot.plot"""
    def __init__(self, parent = None):
        super().__init__(parent)

    def init(self, ax):
        self._plot_obj, = ax.plot(self._xdata, self._ydata, **self.matplotlib_2d_kwargs)

class Scatter(GraphObject2D):
    """wrapper for matplotlib.pyplot.scatter"""
    def __init__(self, parent = None):
        super().__init__(parent)
        self._marker = None

    def init(self, ax):
        self._plot_obj, = ax.plot(self._xdata, self._ydata, **self.matplotlib_2d_kwargs,
            marker = self._marker, linestyle = " ")

    def get_marker(self):
        return self._marker

    def set_marker(self, marker):
        self._marker = marker

    marker = Property(str, get_marker, set_marker)

class HLine(LineObject2D):
    """wrapper for matplotlib.axes.Axes.axhline"""
    def __init__(self, parent = None):
        super().__init__(parent)
        self._y = 0
        self._xmin = 0.0
        self._xmax = 1.0
    
    def init(self, ax):
        """Initializes an object of type Line2D"""
        self._plot_obj = ax.axhline(self._y, **self.matplotlib_2d_kwargs, 
                xmin = self._xmin, xmax = self._xmax)

    def get_y(self):
        return self._y

    def set_y(self, y):
        self._y = y
        if self._plot_obj is not None:
            self._plot_obj.set_ydata([self._y] * 2)
            self._event_handler.schedule(EventTypes.PLOT_DATA_CHANGED)

    def get_xmin(self):
        return self._xmin

    def set_xmin(self, xmin):
        self._xmin = xmin
        if self._plot_obj is not None:
            xdata = self._plot_obj.get_xdata()
            xdata[0] = self._xmin
            self._plot_obj.set_xdata(xdata)
            self._event_handler.schedule(EventTypes.PLOT_DATA_CHANGED)

    def get_xmax(self):
        return self._xmax

    def set_xmax(self, xmax):
        self._xmax = xmax
        if self._plot_obj is not None:
            xdata = self._plot_obj.get_xdata()
            xdata[1] = self._xmax
            self._plot_obj.set_xdata(xdata)
            self._event_handler.schedule(EventTypes.PLOT_DATA_CHANGED)

    y = Property(float, get_y, set_y)
    xMin = Property(float, get_xmin, set_xmin)
    xMax = Property(float, get_xmax, set_xmax)


class SpanObject2D(GraphObject2D):
    """A SpanObject implements Propertys from hspan and vspan"""
    def __init__(self, parent = None):
        super().__init__(parent)
        self._facecolor = None
        self._edgecolor = None

    @property
    def matplotlib_2d_kwargs(self):
        attributes = super().matplotlib_2d_kwargs
        attributes["facecolor"] = self._facecolor
        attributes["edgecolor"] = self._edgecolor
        return attributes

    def get_facecolor(self):
        return self._facecolor

    def set_facecolor(self, facecolor: str):
        self._facecolor = facecolor

    def get_edgecolor(self):
        return self._edgecolor

    def set_edgecolor(self, edgecolor):
        self._edgecolor = edgecolor

    def get_ymin(self):
        return self._ymin

    def set_ymin(self, ymin):
        """Updates the polygon data of the span object
        """
        self._ymin = float(ymin)
        if self._plot_obj is not None:
            # Modify the reference of xy which also modifies the property xy
            xy = self._plot_obj.get_xy()
            xy[0][1] = self._ymin
            xy[3][1] = self._ymin
            #self._plot_obj.set_xy(xy)
            self._event_handler.schedule(EventTypes.PLOT_DATA_CHANGED)

    def get_ymax(self):
        return self._ymax

    def set_ymax(self, ymax):
        """Modifys the ymax coords from the xy Property of the Polygon"""
        self._ymax = float(ymax)
        if self._plot_obj is not None:
            # Modify the reference of xy which also modifies the property xy
            xy = self._plot_obj.get_xy()
            xy[1][1] = self._ymax
            xy[2][1] = self._ymax
            #self._plot_obj.set_xy(xy)
            self._event_handler.schedule(EventTypes.PLOT_DATA_CHANGED)

    def get_xmin(self):
        return self._xmin

    def set_xmin(self, xmin):
        self._xmin = float(xmin)
        if self._plot_obj is not None:
            # Modify the reference of xy which also modifies the property xy
            xy = self._plot_obj.get_xy()
            xy[0][0] = self._xmin
            xy[1][0] = self._xmin
            #self._plot_obj.set_xy(xy)
            self._event_handler.schedule(EventTypes.PLOT_DATA_CHANGED)

    def get_xmax(self):
        return self._xmax

    def set_xmax(self, xmax):
        self._xmax = float(xmax)
        if self._plot_obj is not None:
            # Modify the reference of xy which also modifies the property xy
            xy = self._plot_obj.get_xy()
            xy[2][0] = self._xmax
            xy[3][0] = self._xmax
            #self._plot_obj.set_xy(xy)
            self._event_handler.schedule(EventTypes.PLOT_DATA_CHANGED)

    yMin = Property(float, get_ymin, set_ymin)
    yMax = Property(float, get_ymax, set_ymax)
    xMin = Property(float, get_xmin, set_xmin)
    xMax = Property(float, get_xmax, set_xmax)

    faceColor = Property(str, get_facecolor, set_facecolor)
    edgeColor = Property(str, get_edgecolor, set_edgecolor)

class VSpan(SpanObject2D):
    """wrapper for matplotlib.axes.Axes.axvspan"""
    def __init__(self, parent = None):
        super().__init__(parent)
        self._xmin = 0
        self._xmax = 0
        self._ymin = 0.0
        self._ymax = 1.0

    def init(self, ax):
        """initializes an object of type Polygon"""
        self._plot_obj = ax.axvspan(self._xmin, self._xmax, **self.matplotlib_2d_kwargs,
                ymin = self._ymin, ymax = self._ymax)
    

class HSpan(SpanObject2D):
    """wrapper for matplotlib.axes.Axes.axhspan
    A modification to the _plot_obj can be made with `set(setting = value)`"""
    def __init__(self, parent = None):
        super().__init__(parent)
        self._ymin = 0
        self._ymax = 1
        self._xmin = 0.0
        self._xmax = 1.0
        self._ax = None
        
    def init(self, ax):
        # This will be of type Polygon
        self._plot_obj = ax.axhspan(self._ymin, self._ymax, **self.matplotlib_2d_kwargs, 
                xmin = self._xmin, xmax = self._xmax)

class Imshow(Base):
    """wrapper for matplotlib.axes.Axes.imshow"""
    # changed should be called whenever the mappable is changed
    # set_data sets the image data
    def __init__(self, parent = None):
        super().__init__(parent)
        self._x = []  # 2D Array or PIL Image
        self._cmap = "viridis"
        self._aspect = "equal"
        self._interpolation = "antialiased"

    def init(self, ax):
        self._plot_obj = ax.imshow(self._x, cmap = self._cmap, aspect = self._aspect)
    
    def get_x(self):
        return self._x

    def set_x(self, x):
        self._x = x
        if self._plot_obj is not None:
            # this does not update the normalization
            self._plot_obj.set_data(self._x)
            self._event_handler.schedule(EventTypes.PLOT_DATA_CHANGED)

    def get_cmap(self):
        return self._cmap

    def set_cmap(self, cmap):
        self._cmap = cmap
        if self._plot_obj is not None:
            # this does not update the normalization
            self._plot_obj.set_cmap(self._cmap)
            self._event_handler.schedule(EventTypes.PLOT_DATA_CHANGED)

    def get_aspect(self):
        return self._aspect

    def set_aspect(self, aspect):
        self._aspect = aspect
        if self._plot_obj is not None:
            self._plot_obj.set_aspect(self._aspect)
            self._event_handler.schedule(EventTypes.PLOT_DATA_CHANGED)

    def get_interpolation(self):
        return self._interpolation

    def set_interpolation(self, interpolation):
        self._interpolation = interpolation
        if self._plot_obj is not None:
            self._plot_obj.set_interpolation(self._interpolation)
            self._event_handler.schedule(EventTypes.PLOT_DATA_CHANGED)

    x = Property("QVariantList", get_x, set_x)
    cMap = Property(str, get_cmap, set_cmap)
    aspect = Property(str, get_aspect, set_aspect)
    interpolation = Property(str, get_interpolation, set_interpolation)


class Bar(PlotObject2D):
    """Wrapper for matplotlib.axes.Axes.bar
    The Bar Plot renders as a BarContainer object which inherits from tuple. Every Bar is a 
    Rectangle Patch object which is living inside the BarContainer (which is a tuple)
    Since tuples are immutable we need to reinstantiate a new bar plot every time which results in
    performance loss"""
    def __init__(self, parent = None):
        super().__init__(parent)
        self._x = []
        self._height = []
        self._width = 0.8
        self._colors = [] # If bars should have different colors
        self._orientation = "vertical"

    def init(self, ax):
        # plot_obj will be of type BarContainer
        if self._colors:
            self._plot_obj = ax.bar(self.x, self._height, color = self._colors, width = self._width)
        else:
            self._plot_obj = ax.bar(self.x, self._height, color = self._color, width = self._width)
        
    def get_x(self):
        return self._x

    def set_x(self, x):
        self._x = x

    def get_height(self):
        return self._height

    def set_height(self, height):
        self._height = height

    def get_width(self):
        return self._width

    def set_width(self, width):
        self._width = width
        if self._plot_obj is not None:
            self._plot_obj.remove()  
    
    def get_colors(self):
        return self._colors

    def set_colors(self, colors):
        self._colors = colors

    x = Property("QVariantList", get_x, set_x)
    height = Property("QVariantList", get_height, set_height)
    width = Property(float, get_width, set_width)
    colors = Property("QVariantList", get_colors, set_colors)