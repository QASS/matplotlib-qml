from PySide2.QtQuick import QQuickItem
from PySide2.QtCore import QObject, Signal, Slot, Property
from copy import copy

import numpy as np

from .plot_objects import Base, Figure, Axis
from .event import EventTypes, EventHandler



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
            "label" : self._label,            
        }
        return attributes

    def update():
        pass

    def get_label(self):
        return self._label

    def set_label(self, label):
        self._label = label
        if self._plot_obj is not None:
            self._plot_obj.set_label(self._label)
            self.labelChanged.emit()
            self._event_handler.schedule(EventTypes.PLOT_DATA_CHANGED)

    def get_alpha(self):
        return self._alpha

    def set_alpha(self, alpha):
        self._alpha = alpha
        if self._plot_obj is not None:
            self._plot_obj.set_alpha(self._alpha)
            self.alphaChanged.emit()
            self._event_handler.schedule(EventTypes.PLOT_DATA_CHANGED)

    def get_color(self):
        return self._color

    def set_color(self, color):
        self._color = color
        if self._plot_obj is not None:
            self._plot_obj.set_color(self._color)
            self.colorChanged.emit()
            self._event_handler.schedule(EventTypes.PLOT_DATA_CHANGED)

    

    def init(self, ax):
        raise NotImplementedError("This method needs to be implemented by the programmer!")

    alphaChanged = Signal()
    colorChanged = Signal()
    labelChanged = Signal()

    alpha = Property(float, get_alpha, set_alpha)
    color = Property(str, get_color, set_color)
    label = Property(str, get_label, set_label)
    

class Text(PlotObject2D):
    """Base class for all text related Types as in Matplotlib"""

    # constants for allowed arguments
    FONTFAMILIES = ('serif', 'sans-serif', 'cursive', 'fantasy', 'monospace')
    FONTSTYLES = ('normal', 'italic', 'oblique')
    FONTVARIANTS = ('normal', 'small-caps')
    FONTWEIGHTS = ('ultralight', 'light', 'normal', 'regular', 'book', 'medium', 'roman', 
        'semibold', 'demibold', 'demi', 'bold', 'heavy', 'extra bold', 'black')
    HORIZONTALALIGNMENTS = ('center', 'right', 'left')

    def __init__(self, parent=None):
        super().__init__(parent=parent)
        self._fontsize = 10.0
        #self._fontstretch = 1000
        self._fontstyle = "normal"
        # self._fontvariant = "normal"
        self._fontweight = "normal"
        self._fontfamily = "serif"
        self._linespacing = 1.0
        self._rotation = 0

    @property 
    def matplotlib_2d_kwargs(self):
        """Extends the typical kwargs dict witht he text types"""
        attributes = super().matplotlib_2d_kwargs
        attributes["fontsize"] = self._fontsize
        #attributes["fontstretch"] = self._fontstretch
        attributes["fontstyle"] = self._fontstyle
        # attributes["fontvariant"] = self._fontvariant
        attributes["fontweight"] = self._fontweight
        attributes["fontfamily"] = self._fontfamily
        # attributes["linespacing"] = self._linespacing
        attributes["rotation"] = self._rotation   
        return attributes

    def get_fontsize(self):
        return self._fontsize

    def set_fontsize(self, fontsize):
        self._fontsize = fontsize
        if self._plot_obj is not None:
            self._plot_obj.set_fontsize(self._fontsize)
            self.fontSizeChanged.emit()
            self._event_handler.schedule(EventTypes.PLOT_DATA_CHANGED)

    # TODO does nothing atm must be fixed
    # def get_fontstretch(self):
    #     return self._fontstretch

    # def set_fontstretch(self, fontstretch):
    #     self._fontstretch = fontstretch
    #     if self._plot_obj is not None:
    #         self._plot_obj.set_fontstretch(self._fontstretch)
    #         self._event_handler.schedule(EventTypes.PLOT_DATA_CHANGED)

    def get_fontstyle(self):
        return self._fontstyle

    def set_fontstyle(self, fontstyle):
        if not fontstyle in self.FONTSTYLES:
            raise ValueError("Unsupported font style")
        self._fontstyle = fontstyle
        if self._plot_obj is not None:
            self._plot_obj.set_fontstyle(self._fontstyle)
            self.fontStyleChanged.emit()
            self._event_handler.schedule(EventTypes.PLOT_DATA_CHANGED)

    # TODO doesn't do anything
    # def get_fontvariant(self):
    #     return self._fontvariant

    # def set_fontvariant(self, fontvariant):
    #     if not fontvariant in self.FONTVARIANTS:
    #         raise ValueError("Unsupported font style")
    #     self._fontvariant = fontvariant
    #     if self._plot_obj is not None:
    #         self._plot_obj.set_fontvariant(self._fontvariant)
    #         self._event_handler.schedule(EventTypes.PLOT_DATA_CHANGED)

    def get_fontweight(self):
        return self._fontweight

    def set_fontweight(self, fontweight):
        if not fontweight in self.FONTWEIGHTS:
            raise ValueError("Unsupported font weight")
        self._fontweight = fontweight
        if self._plot_obj is not None:
            self._plot_obj.set_fontweight(self._fontweight)
            self.fontWeightChanged.emit()
            self._event_handler.schedule(EventTypes.PLOT_DATA_CHANGED)

    def get_fontfamily(self):
        return self._fontfamily

    def set_fontfamily(self, fontfamily):
        if not fontfamily in self.FONTFAMILIES:
            print("Unsupported fontfamily, falling back to serif")
            fontfamily = "serif"
        self._fontfamily = fontfamily
        if self._plot_obj is not None:
            self._plot_obj.set_fontfamily(self._fontfamily)
            self.fontFamilyChanged.emit()
            self._event_handler.schedule(EventTypes.PLOT_DATA_CHANGED)

    # TODO doesn't do anything
    # def get_linespacing(self):
    #     return self._linespacing

    # def set_linespacing(self, linespacing):
    #     self._linespacing = linespacing
    #     if self._plot_obj is not None:
    #         self._plot_obj.set_linespacing(self._linespacing)
    #         self._event_handler.schedule(EventTypes.PLOT_DATA_CHANGED)

    def get_rotation(self):
        return self._rotation

    def set_rotation(self, rotation):
        self._rotation = rotation
        if self._plot_obj is not None:
            self._plot_obj.set_rotation(self._rotation)
            self._event_handler.schedule(EventTypes.PLOT_DATA_CHANGED)

    fontSizeChanged = Signal()
    fontStyleChanged = Signal()
    fontWeightChanged = Signal()
    fontFamilyChanged = Signal()
    rotationChanged = Signal()

    fontSize = Property(float, get_fontsize, set_fontsize)
    #fontStretch = Property(int, get_fontstretch, set_fontstretch)
    fontStyle = Property(str, get_fontstyle, set_fontstyle)
    # fontVariant = Property(str, get_fontvariant, set_fontvariant)
    fontWeight = Property(str, get_fontweight, set_fontweight)
    fontFamily = Property(str, get_fontfamily, set_fontfamily)
    # lineSpacing = Property(float, get_linespacing, set_linespacing)
    rotation = Property(float, get_rotation, set_rotation)


class GraphObject2D(PlotObject2D):
    """Implements Propertys from 2D Graph objects like scatters, lines, spans"""
    def __init__(self, parent = None):
        super().__init__(parent)
        self._xdata = []
        self._ydata = []
        # The plot object is the object being wrapped (i.e. the matplotlib object)

    @property
    def xdata(self):
        return self._xdata

    @property
    def ydata(self):
        return self._ydata

    @Slot(int)
    @Slot(int, float)
    def randomData(self, length, upper_limit = 1.0):
        from numpy import random, arange
        self.set_ydata(random.rand(length) * upper_limit)
        self.set_xdata(arange(len(self._ydata)))
        self._event_handler.schedule(EventTypes.PLOT_DATA_CHANGED)

    def set_xdata(self, xdata: list):
        self._xdata = copy(xdata)
        self.xDataChanged.emit()
        if self._plot_obj is not None:
            self._plot_obj.set_xdata(self._xdata)
            # only emit the event if both shapes are correct
            if len(self._xdata) == len(self._ydata):
                self._event_handler.schedule(EventTypes.PLOT_DATA_CHANGED)


    def get_xdata(self):
        """QML can't interpret numpy arrays thats why a conversion needs to take place 
        before it can be used in QML. In order to still modify the numpy array in Python
        the property `xdata` is provided """
        if isinstance(self._xdata, np.ndarray):
            return self._xdata.tolist()
        return self._xdata

    def set_ydata(self, ydata: list):
        self._ydata = copy(ydata)
        self.yDataChanged.emit()
        if self._plot_obj is not None:
            self._plot_obj.set_ydata(self._ydata)
            # only emit the event if both shapes are correct
            if len(self._xdata) == len(self._ydata):
                self._event_handler.schedule(EventTypes.PLOT_DATA_CHANGED)

    def get_ydata(self):
        """QML can't interpret numpy arrays thats why a conversion needs to take place 
        before it can be used in QML. In order to still modify the numpy array in Python
        the property `ydata` is provided """
        if isinstance(self._ydata, np.ndarray):
            return self._ydata.tolist()
        return self._ydata

    xDataChanged = Signal()
    yDataChanged = Signal() # ´Thos notify Signals must be emitted in the setter

    xData = Property("QVariantList", get_xdata, set_xdata, notify = xDataChanged)
    yData = Property("QVariantList", get_ydata, set_ydata, notify = yDataChanged)

class LineObject2D(GraphObject2D):
    """Implements Propertys from any Line item"""
    def __init__(self, parent = None):
        super().__init__(parent)
        self._linestyle = None
        self._linewidth = 1.0
        self._marker = None
        self._markersize = None
        self._markeredgewidth = None
        self._markeredgecolor = None
        self._markerfacecolor = None        
        self._picker = False # Wether picking is enabled for an artist
        self._pickradius = 1

    @property
    def matplotlib_2d_kwargs(self):
        attributes = super().matplotlib_2d_kwargs
        attributes["linestyle"] = self._linestyle
        attributes["linewidth"] = self._linewidth
        attributes["marker"] = self._marker
        attributes["markersize"] = self._markersize
        attributes["markeredgewidth"] = self._markeredgewidth
        attributes["markeredgecolor"] = self._markeredgecolor
        attributes["markerfacecolor"] = self._markerfacecolor
        attributes["picker"] = self._picker
        attributes["pickradius"] = self._pickradius
        return attributes

    def get_linestyle(self):
        return self._linestyle

    def set_linestyle(self, linestyle):
        self._linestyle = linestyle
        if self._plot_obj is not None:
            self._plot_obj.set_linestyle(self._linestyle)
            self._event_handler.schedule(EventTypes.PLOT_DATA_CHANGED)


    def get_linewidth(self):
        return self._linewidth

    def set_linewidth(self, linewidth: float):
        self._linewidth = linewidth
        if self._plot_obj is not None:
            self._plot_obj.set_linewidth(self._linewidth)
            self._event_handler.schedule(EventTypes.PLOT_DATA_CHANGED)

    def get_marker(self):
        return self._marker

    def set_marker(self, marker):
        self._marker = marker
        if self._plot_obj is not None:
            self._plot_obj.set_marker(marker)
            self._event_handler.schedule(EventTypes.PLOT_DATA_CHANGED)

    def get_markersize(self):
        return self._markersize

    def set_markersize(self, markersize):
        self._markersize = markersize
        if self._plot_obj is not None:
            self._plot_obj.set_markersize(self._markersize)
            self._event_handler.schedule(EventTypes.PLOT_DATA_CHANGED)

    def get_markeredgewidth(self):
        return self._markeredgewidth

    def set_markeredgewidth(self, width):
        self._markeredgewidth = width
        if self._plot_obj is not None:
            self._plot_obj.set_markeredgewidth(self._markeredgewidth)
            self._event_handler.schedule(EventTypes.PLOT_DATA_CHANGED)

    def get_markeredgecolor(self):
        return self._markeredgecolor

    def set_markeredgecolor(self, color):
        self._markeredgecolor = color
        if self._plot_obj is not None:
            self._plot_obj.set_markeredgecolor(self._markeredgecolor)
            self._event_handler.schedule(EventTypes.PLOT_DATA_CHANGED)

    def get_markerfacecolor(self):
        return self._markerfacecolor

    def set_markerfacecolor(self, color):
        self._markerfacecolor = color
        if self._plot_obj is not None:
            self._plot_obj.set_markerfacecolor(self._markerfacecolor)
            self._event_handler.schedule(EventTypes.PLOT_DATA_CHANGED)

    def get_picker(self):
        return self._picker

    def set_picker(self, picker):
        self._picker = picker
        if self._plot_obj is not None:
            self._plot_obj.set_picker(self._picker)
            self._event_handler.schedule(EventTypes.PLOT_DATA_CHANGED)

    def get_pick_radius(self):
        return self._pickradius

    def set_pick_radius(self, pick_radius):
        self._pickradius = pick_radius
        if self._plot_obj is not None:
            self._plot_obj.set_pickradius(self._pickradius)
            self._event_handler.schedule(EventTypes.PLOT_DATA_CHANGED)
        

    linestyle = Property(str, get_linestyle, set_linestyle)
    linewidth = Property(float, get_linewidth, set_linewidth)
    marker = Property(str, get_marker, set_marker)
    markerSize = Property(float, get_markersize, set_markersize)
    markerEdgeWidth = Property(float, get_markeredgewidth, set_markeredgewidth)
    markerEdgeColor = Property(str, get_markeredgecolor, set_markeredgecolor)
    markerFaceColor = Property(str, get_markerfacecolor, set_markerfacecolor)
    picker = Property(bool, get_picker, set_picker)
    pickRadius = Property(int, get_pick_radius, set_pick_radius)

class Line(LineObject2D):
    """wrapper for matplotlib.pyplot.plot"""
    def __init__(self, parent = None):
        super().__init__(parent)

    def init(self, ax):
        self._plot_obj, = ax.plot(self._xdata, self._ydata, **self.matplotlib_2d_kwargs)

class Scatter(LineObject2D):
    """wrapper for matplotlib.pyplot.scatter"""
    def __init__(self, parent = None):
        super().__init__(parent)
        self._marker = "o"
        self._linestyle = " "

    def init(self, ax):
        self._plot_obj, = ax.plot(self._xdata, self._ydata, **self.matplotlib_2d_kwargs)


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
        if self._plot_obj is not None:
            self._plot_obj.set_facecolor(self._facecolor)
            self._event_handler.schedule(EventTypes.PLOT_DATA_CHANGED)

    def get_edgecolor(self):
        return self._edgecolor

    def set_edgecolor(self, edgecolor):
        self._edgecolor = edgecolor
        if self._plot_obj is not None:
            self._plot_obj.set_edgecolor(self._edgecolor)
            self._event_handler.schedule(EventTypes.PLOT_DATA_CHANGED)

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
        self._vmin = None
        self._vmax = None
        self._extent = None
        self._colorbar = None

    def init(self, ax):
        self._plot_obj = ax.imshow(self._x, cmap = self._cmap, aspect = self._aspect, 
            vmin = self._vmin, vmax = self._vmax, extent = self._extent)
        if self._colorbar is not None:
            self._colorbar.set_event_handler(self._event_handler)
            self._colorbar.init(ax, self._plot_obj)

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

    def get_vmin(self):
        return self._vmin

    def set_vmin(self, vmin):
        self._vmin = vmin
        if self._plot_obj is not None:
            self._plot_obj.set_clim(self._vmin, self._vmax)
            self._event_handler.schedule(EventTypes.PLOT_DATA_CHANGED)

    def get_vmax(self):
        return self._vmax

    def set_vmax(self, vmax):
        self._vmax = vmax
        if self._plot_obj is not None:
            self._plot_obj.set_clim(self._vmin, self._vmax)
            self._event_handler.schedule(EventTypes.PLOT_DATA_CHANGED)

    def get_extent(self):
        return self._extent

    def set_extent(self, extent):
        """
        he bounding box in data coordinates that the image will fill. The image is stretched individually along x and y to fill the box.
        The default extent is determined by the following conditions. Pixels have unit size in data coordinates. Their centers are on integer coordinates, and their center coordinates range from 0 to columns-1 horizontally and from 0 to rows-1 vertically.
        Note that the direction of the vertical axis and thus the default values for top and bottom depend on origin:
        For origin == 'upper' the default is (-0.5, numcols-0.5, numrows-0.5, -0.5).
        For origin == 'lower' the default is (-0.5, numcols-0.5, -0.5, numrows-0.5).
        See the origin and extent in imshow tutorial for examples and a more detailed description.
        """
        self._extent = extent
        if self._plot_obj is not None:
            self._plot_obj.set_extent(self._extent)
            self._event_handler.schedule(EventTypes.PLOT_DATA_CHANGED)

    def get_colorbar(self):
        return self._colorbar

    def set_colorbar(self, colorbar):
        self._colorbar = colorbar

    x = Property("QVariantList", get_x, set_x)
    cMap = Property(str, get_cmap, set_cmap)
    aspect = Property(str, get_aspect, set_aspect)
    interpolation = Property(str, get_interpolation, set_interpolation)
    vMin = Property(float, get_vmin, set_vmin)
    vMax = Property(float, get_vmax, set_vmax)
    extent = Property("QVariantList", get_extent, set_extent)
    colorbar = Property(QObject, get_colorbar, set_colorbar)


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
        self._tick_labels = None
        self._edgecolor = None
        self._bar_event_handler = EventHandler()

    def init(self, ax):
        """Subscribe for the Bar Plot Changed Event in order to schedule a new instance
        creation of a bar plot object and create a plot object on the axis"""
        self._bar_event_handler.register(EventTypes.BAR_PLOT_CHANGED, self._reinstantiate)
        self._create_plot_obj(ax)


    def _create_plot_obj(self, ax):
        """Creates a BarContainer Plot object which will be wrapped in this class
        since propertys can only have one distinct type there's a need to check different
        cases for some matplotlib arguments like color which can be a list or just a string."""
        if self._colors:
            self._plot_obj = ax.bar(self.x, self._height, color = self._colors,
            width = self._width, tick_label = self._tick_labels, edgecolor = self._edgecolor)
        else:
            self._plot_obj = ax.bar(self.x, self._height, color = self._color,
            width = self._width, tick_label = self._tick_labels, edgecolor = self._edgecolor)

    def _get_axis(self):
        """Retrieve the ax object from the axis parent

        :raises: ValueError if the parent has the wrong type
        """
        axis = self.parent()
        if isinstance(axis, Axis):
            return axis.ax
        raise TypeError(f"The parent should be of type Axis but was of type {type(axis)}")

    def _reinstantiate(self):
        """The Bar plot needs to be recreated each time we make a change. This method is called
        by the event_handler and will schedule a plot data change event to redraw the figure"""
        self._plot_obj.remove()  # remove the object from the axis
        self._create_plot_obj(self._get_axis())
        self._event_handler.schedule(EventTypes.PLOT_DATA_CHANGED)

    @Slot(int)
    @Slot(int, float)
    def randomData(self, length, upper_limit = 1.0):
        self.set_x(np.arange(length))
        self.set_height(np.random.rand(length) * upper_limit)

    def get_x(self):
        return self._x

    def set_x(self, x):
        self._x = x
        if self._plot_obj is not None:
            if len(self._x) == len(self._height):
                self._bar_event_handler.schedule(EventTypes.BAR_PLOT_CHANGED)

    def get_height(self):
        return self._height

    def set_height(self, height):
        self._height = height
        if self._plot_obj is not None:
            if len(self._x) == len(self._height):
                self._bar_event_handler.schedule(EventTypes.BAR_PLOT_CHANGED)

    def get_width(self):
        return self._width

    def set_width(self, width):
        self._width = width
        if self._plot_obj is not None:
            self._bar_event_handler.schedule(EventTypes.BAR_PLOT_CHANGED)

    def get_color(self):
        return self._color

    def set_color(self, color):
        self._color = color
        if self._plot_obj is not None:
            self._bar_event_handler.schedule(EventTypes.BAR_PLOT_CHANGED)

    def get_colors(self):
        return self._colors

    def set_colors(self, colors):
        self._colors = colors
        if self._plot_obj is not None:
            self._bar_event_handler.schedule(EventTypes.BAR_PLOT_CHANGED)

    def get_tick_labels(self):
        return self._tick_labels

    def set_tick_labels(self, tick_labels):
        """The tick labels need to be set to None if no tick labels are provided
        Otherwise this will cause a shape mismatch during object reinstantiation"""
        # TODO: reset the xticks with the axis
        if len(tick_labels) == 0:
            tick_labels = None
        self._tick_labels = tick_labels
        if self._plot_obj is not None:
            self._bar_event_handler.schedule(EventTypes.BAR_PLOT_CHANGED)

    x = Property("QVariantList", get_x, set_x)
    height = Property("QVariantList", get_height, set_height)
    width = Property(float, get_width, set_width)
    color = Property(str, get_color, set_color)
    colors = Property("QVariantList", get_colors, set_colors)
    tickLabels = Property("QVariantList", get_tick_labels, set_tick_labels)
