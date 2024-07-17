from matplotlib import rcParams
from PySide2.QtCore import Property, Signal
from matplotlib.lines import Line2D as MatplotlibLine2D

from matplotlib_qml.artist import Artist
from matplotlib_qml.event import EventTypes
from matplotlib_qml.utils import numpy_compatibility


class Line2D(Artist):
    def __init__(self, parent=None):
        self._plot_obj = MatplotlibLine2D([], [])
        super().__init__(parent)        
        # THIS SPACE COULD BE USED FOR THEMES

    def init(self, ax):
        """Connect the floating plot object to an ax object to be able to display it on the figure"""
        ax.add_line(self._plot_obj)
        self._event_handler.schedule(EventTypes.PLOT_DATA_CHANGED)

    def get_linewidth(self):
        return self._plot_obj.get_linewidth() # or self._plot_obj.get_linewidth()

    def set_linewidth(self, linewidth):
        self._plot_obj.set_linewidth(linewidth)
        self.schedule_plot_update()
        self.linewidthChanged.emit()

    def get_linestyle(self):
        return self._plot_obj.get_linestyle() # or self._plot_obj.get_linestyle()

    def set_linestyle(self, linestyle):
        self._plot_obj.set_linestyle(linestyle)
        self.schedule_plot_update()
        self.linestyleChanged.emit()

    def get_color(self):
        return self._plot_obj.get_color()

    def set_color(self, color):
        self._plot_obj.set_color(color)
        self.schedule_plot_update()
        self.colorChanged.emit()
        self.cChanged.emit()
    
    def get_marker(self):
        return self._plot_obj.get_marker() # or self._plot_obj.get_marker # TODO check if thats true

    def set_marker(self, marker):
        self._plot_obj.set_marker(marker)
        self.schedule_plot_update()
        self.markerChanged.emit()

    def get_markersize(self):
        return self._plot_obj.get_markersize()

    def set_markersize(self, markersize):
        self._plot_obj.set_markersize(markersize)
        self.schedule_plot_update()
        self.markerSizeChanged.emit()
        self.markersizeChanged.emit()

    def get_markeredgewidth(self):
        return self._plot_obj.get_markeredgewidth() # or self._plot_obj.get_markeredgewidth # TODO check if true

    def set_markeredgewidth(self, markeredgewidth):
        self._plot_obj.set_markeredgewidth(markeredgewidth)
        self.schedule_plot_update()
        self.markerEdgeWidthChanged.emit()
        self.markeredgewidthChanged.emit()

    def get_markeredgecolor(self):
        return self._plot_obj.get_markeredgecolor() # or self._plot_obj.get_markeredgecolor()

    def set_markeredgecolor(self, markeredgecolor):
        self._plot_obj.set_markeredgecolor(markeredgecolor)
        self.schedule_plot_update()
        self.markerEdgeColorChanged.emit()
        self.markeredgecolorChanged.emit()

    def get_markerfacecolor(self):
        return self._plot_obj.get_markerfacecolor() # or self._plot_obj.get_markerfacecolor # TODO check if true

    def set_markerfacecolor(self, markerfacecolor):
        self._plot_obj.set_markerfacecolor(markerfacecolor)
        self.schedule_plot_update()
        self.markerFaceColorChanged.emit()
        self.markerfacecolorChanged.emit()

    def get_markerfacecoloralt(self):
        return self._plot_obj.get_markerfacecoloralt()

    def set_markerfacecoloralt(self, markerfacecoloralt):
        self._plot_obj.set_markerfacecoloralt(markerfacecoloralt)
        self.schedule_plot_update()
        self.markerFaceColorAltChanged.emit()
        self.markerfacecoloraltChanged.emit()

    def get_fillstyle(self):
        return self._plot_obj.get_fillstyle() # or self._plot_obj.get_fillstyle # TODO check if true

    def set_fillstyle(self, fillstyle):
        self._plot_obj.set_fillstyle(fillstyle)
        self.schedule_plot_update()
        self.fillstyleChanged.emit()

    def get_antialiased(self):
        return self._plot_obj.get_antialiased

    def set_antialised(self, antialiased):
        self._plot_obj.set_antialiased(antialiased)
        self.schedule_plot_update()
        self.antialiasedChanged.emit()

    def get_dash_capstyle(self):
        return self._plot_obj.get_dash_capstyle()

    def set_dash_capstyle(self, dash_capstyle):
        self._plot_obj.set_dash_capstyle(dash_capstyle)
        self.schedule_plot_update()
        self.dashCapstyleChanged.emit()

    def get_solid_capstyle(self):
        return self._plot_obj.get_solid_capstyle()

    def set_solid_capstyle(self, solid_capstyle):
        self._plot_obj.set_solid_capstyle(solid_capstyle)
        self.schedule_plot_update()
        self.solidCapstyleChanged.emit()
        self.solidcapstyleChanged.emit()

    def get_dash_joinstyle(self):
        return self._plot_obj.get_dash_joinstlye()

    def set_dash_joinstyle(self, dash_joinstyle):
        self._plot_obj.set_dash_joinstyle(dash_joinstyle)
        self.schedule_plot_update()
        self.dashJoinstyleChanged.emit()
        self.dashjoinstyleChanged.emit()

    def get_solid_joinstyle(self):
        return self._plot_obj.get_solid_joinstyle() # or self._plot_obj.get_solid_joinstyle

    def set_solid_joinstyle(self, solid_joinstyle):
        self._plot_obj.set_solid_joinstyle(solid_joinstyle)
        self.solidJoinstyleChanged.emit()
        self.solidjoinstyleChanged.emit()

    def get_pickradius(self):
        return self._plot_obj.get_pickradius # or self._plot_obj.get_pickradius

    def set_pickradius(self, pickradius):
        self._plot_obj.set_pickradius(pickradius)
        self.pickRadiusChanged.emit()
        self.pickradiusChanged.emit()

    def get_drawstyle(self):
        return self._plot_obj.get_drawstyle() # or self._plot_obj.get_drawstyle()

    def set_drawstyle(self, drawstyle):
        self._plot_obj.set_drawstyle(drawstyle)
        self.schedule_plot_update()
        self.drawstyleChanged.emit()

    def get_markevery(self):
        return self._plot_obj.get_markevery() # or self._plot_obj.get_markevery()

    def set_markevery(self, markevery):
        self._plot_obj.set_markevery(markevery)
        self.schedule_plot_update()
        self.markeveryChanged.emit()

    @numpy_compatibility
    def get_xdata(self):
        return self._plot_obj.get_xdata() # # or self._plot_obj.get_xdata()

    def set_xdata(self, xdata):
        self._plot_obj.set_xdata(xdata)
        self.schedule_plot_update()
        self.xDataChanged.emit()

    @numpy_compatibility
    def get_ydata(self):
        return self._plot_obj.get_ydata() # or self._plot_obj.get_ydata()

    def set_ydata(self, ydata):
        self._plot_obj.set_ydata(ydata)
        self.schedule_plot_update()
        self.yDataChanged.emit()
        
    linewidthChanged = Signal()
    linestyleChanged = Signal()
    colorChanged = Signal()
    cChanged = Signal()
    markerChanged = Signal()
    markerSizeChanged = Signal()
    markerEdgeWidthChanged = Signal()
    markerEdgeColorChanged = Signal()
    markerFaceColorChanged = Signal()
    markerFaceColorAltChanged = Signal()
    fillstyleChanged = Signal()
    antialiasedChanged = Signal()
    dashCapstyleChanged = Signal()
    solidCapstyleChanged = Signal()
    dashJoinstyleChanged = Signal()
    solidJoinstyleChanged = Signal()
    pickRadiusChanged = Signal()
    drawstyleChanged = Signal()
    markeveryChanged = Signal()
    xDataChanged = Signal()
    yDataChanged = Signal()

    ### ALIAS ###
    markersizeChanged = Signal()
    markeredgewidthChanged = Signal()
    markeredgecolorChanged = Signal()
    markerfacecolorChanged = Signal()
    markerfacecoloraltChanged = Signal()
    solidcapstyleChanged = Signal()
    dashjoinstyleChanged = Signal()
    solidjoinstyleChanged = Signal()
    pickradiusChanged = Signal()


    linewidth = Property(float, get_linewidth, set_linewidth)
    linestyle = Property(str, get_linestyle, set_linestyle)
    color = Property(str, get_color, set_color)
    c = color
    marker = Property(str, get_marker, set_marker)
    markerSize = Property(float, get_markersize, set_markersize)
    markerEdgeWidth = Property(float, get_markeredgewidth, set_markeredgewidth)
    markerEdgeColor = Property(str, get_markeredgecolor, set_markeredgecolor)
    markerFaceColor = Property(str, get_markerfacecolor, set_markerfacecolor)
    markerFaceColorAlt = Property(str, get_markerfacecoloralt, set_markerfacecoloralt)
    fillstyle = Property(str, get_fillstyle, set_fillstyle)
    antialiased = Property(bool, get_antialiased, set_antialised)
    dashCapstyle = Property(str, get_dash_capstyle, set_dash_capstyle)
    solidCapstyle = Property(str, get_solid_capstyle, set_solid_capstyle)
    dashJoinstyle = Property(str, get_dash_joinstyle, set_dash_joinstyle)
    solidJoinstyle = Property(str, get_solid_joinstyle, set_solid_joinstyle)
    pickRadius = Property(float, get_pickradius, set_pickradius)
    drawstyle = Property(str, get_drawstyle, set_drawstyle)
    markevery = Property(int, get_markevery, set_markevery)
    xData = Property("QVariantList", get_xdata, set_xdata)
    yData = Property("QVariantList", get_ydata, set_ydata)

    ### ALIAS ###
    markersize = markerSize
    markeredgewidth = markerEdgeWidth
    markeredgecolor = markerEdgeColor
    markerfacecolor = markerFaceColor
    markerfacecoloralt = markerFaceColorAlt
    solidcapstyle = solidCapstyle
    dashjoinstyle = dashJoinstyle
    solidjoinstyle = solidJoinstyle
    pickradius = pickRadius


Line = Line2D

class Scatter(Line2D):
    """Shorthand for an efficient Scatter plot that is implemented via a Line2D object (much faster than a collection)"""
    def __init__(self, parent=None):
        super().__init__(parent)
        self.set_marker("o")
        self.set_linestyle(" ")


class HLine(Line2D):
    """ wrapper for matplotlib.axes.Axes.axhline """

    def __init__(self, parent = None):
        super().__init__(parent)
        self._y = 0
        self._xmin = 0
        self._xmax = 1
        
        # In case the properties aren't being set, set them here
        self.set_y(self._y)
        self.set_xmin(self._xmin)
        self.set_xmax(self._xmax)

    def init(self, ax):
        """Apply the yaxis transform to the Line2D object in order to stick it to the axis edges"""
        transform = ax.get_yaxis_transform(which='grid')
        self._plot_obj.set_transform(transform)
        super().init(ax)

    @numpy_compatibility
    def get_y(self):
        ydata = self.get_ydata()
        if len(ydata) > 0:
            return self._y
        return ydata[0]

    def set_y(self, y):
        self._y = y
        self.set_ydata([self._y, self._y])
        self.yChanged.emit()

    @numpy_compatibility
    def get_xmin(self):
        xdata = self.get_xdata()
        if len(xdata) > 0:
            return self._xmin
        return xdata[0]

    def set_xmin(self, xmin):
        self._xmin = xmin
        self.set_xdata([self._xmin, self._xmax])
        self.xMinChanged.emit()

    @numpy_compatibility
    def get_xmax(self):
        xdata = self.get_xdata()
        if len(xdata) > 0:
            return self._xmax
        return xdata[1]

    def set_xmax(self, xmax):
        self._xmax = xmax
        self.set_xdata([self._xmin, self._xmax])
        self.xMaxChanged.emit()

    yChanged = Signal()
    xMinChanged = Signal()
    xMaxChanged = Signal()

    y = Property(float, get_y, set_y)
    xMin = Property(float, get_xmin, set_xmin)
    xMax = Property(float, get_xmax, set_xmax)

class VLine(Line2D):
    """ wrapper for matplotlib.axes.Axes.axvline """

    def __init__(self, parent = None):
        super().__init__(parent)
        self._x = 0
        self._ymin = 0
        self._ymax = 1

        # In case the properties aren't being set, set them here
        self.set_x(self._x)
        self.set_ymin(self._ymin)
        self.set_ymax(self._ymax)

    def init(self, ax):
        """Apply the xaxis transform to the Line2D object in order to stick it to the axis edges"""
        transform = ax.get_xaxis_transform(which='grid')
        self._plot_obj.set_transform(transform)
        super().init(ax)

    @numpy_compatibility
    def get_x(self):
        xdata = self.get_xdata()
        if len(xdata) > 0:
            return self._y
        return xdata[0]

    def set_x(self, x):
        self._x = x
        self.set_xdata([self._x, self._x])
        self.xChanged.emit()

    @numpy_compatibility
    def get_ymin(self):
        ydata = self.get_ydata()
        if len(ydata) > 0:
            return self._xmin
        return ydata[0]

    def set_ymin(self, ymin):
        self._ymin = ymin
        self.set_ydata([self._ymin, self._ymax])
        self.yMinChanged.emit()

    @numpy_compatibility
    def get_ymax(self):
        ydata = self.get_ydata()
        if len(ydata) > 0:
            return self._ymax
        return ydata[1]

    def set_ymax(self, ymax):
        self._ymax = ymax
        self.set_ydata([self._ymin, self._ymax])
        self.yMaxChanged.emit()

    xChanged = Signal()
    yMinChanged = Signal()
    yMaxChanged = Signal()

    x = Property(float, get_x, set_x)
    yMin = Property(float, get_ymin, set_ymin)
    yMax = Property(float, get_ymax, set_ymax)


def init(factory):
    factory.register(Line2D, "Matplotlib", qml_component_name = "Line")
    factory.register(Scatter, "Matplotlib")
    factory.register(HLine, "Matplotlib")
    factory.register(VLine, "Matplotlib")
