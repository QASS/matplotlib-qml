from matplotlib import rcParams
from PySide2.QtCore import Property

from matplotlib_bridge.artist import Artist
from matplotlib_bridge.event import EventTypes


class Line2D(Artist):
    def __init__(self, parent=None):
        super().__init__(parent)

        FILLSTYLES = {'full', 'left', 'right', 'bottom', 'top', 'none'}
        
        self._linewidth = rcParams['lines.linewidth']  # all Nones default to rc
        self._linestyle = rcParams['lines.linestyle']
        self._color = rcParams['lines.color']
        self._marker = rcParams['lines.marker']
        self._markersize = rcParams['lines.markersize']
        self._markeredgewidth = None
        self._markeredgecolor = rcParams['lines.markeredgecolor']
        self._markerfacecolor = rcParams['lines.markerfacecolor']
        self._markerfacecoloralt = 'none'
        self._fillstyle = None
        self._antialiased = rcParams['lines.antialiased']
        self._dash_capstyle = rcParams['lines.dash_capstyle']
        self._solid_capstyle = rcParams['lines.solid_capstyle']
        self._dash_joinstyle = rcParams['lines.dash_joinstyle']
        self._solid_joinstyle = rcParams['lines.solid_joinstyle']
        self._pickradius = 5
        self._drawstyle = 'default'
        self._markevery = None
        self._xdata = []
        self._ydata = []


    def init(self, ax):
        kwargs = {
            "linewidth": self._linewidth,
            "linestyle": self._linestyle,
            "c": self._color,
            "marker": self._marker,
            "markersize": self._markersize,
            "markeredgewidth": self._markeredgewidth,
            "markeredgecolor": self._markeredgecolor,
            "markerfacecolor": self._markerfacecolor,
            "markerfacecoloralt": self._markerfacecoloralt,
            "fillstyle": self._fillstyle,
            "antialiased": self._antialiased,
            "dash_capstyle": self._dash_capstyle,
            "solid_capstyle": self._solid_capstyle,
            "dash_joinstyle": self._dash_joinstyle,
            "solid_joinstyle": self._solid_joinstyle,
            "pickradius": self._pickradius,
            "drawstyle": self._drawstyle,
            "markevery": self._markevery,
            "alpha": self._alpha,
            "label": self._label
        }
        self._plot_obj = ax.plot(self._xdata, self._ydata, **kwargs)

    def get_linewidth(self):
        return self._linewidth # or self._plot_obj.get_linewidth()

    def set_linewidth(self, linewidth):
        self._linewidth = linewidth
        if self._plot_obj is not None:
            self._plot_obj.set_linewidth(self._linewidth)

    def get_linestyle(self):
        return self._linestyle # or self._plot_obj.get_linestyle()

    def set_linestyle(self, linestyle):
        self._linestyle = linestyle
        if self._plot_obj is not None:
            self._plot_obj.set_linestyle(self._linestyle)

    def get_color(self):
        return self._color # or self._plot_obj.get_color()

    def set_color(self, color):
        self._color = color
        if self._plot_obj is not None:
            self._plot_obj.set_color(self._color)
    
    def get_marker(self):
        return self._marker # or self._plot_obj.get_marker # TODO check if thats true

    def set_marker(self, marker):
        self._marker = marker
        if self._plot_obj is not None:
            self._plot_obj.set_marker(self._marker)

    def get_markersize(self):
        return self._markersize

    def set_markersize(self, markersize):
        self._markersize = markersize   # or self._plot_obj.get_markersize # TODO check if true

    def get_markeredgewidth(self):
        return self._markeredgewidth # or self._plot_obj.get_markeredgewidth # TODO check if true

    def set_markeredgewidth(self, markeredgewidth):
        self._markeredgewidth = markeredgewidth
        if self._plot_obj is not None:
            self._plot_obj.set_markeredgewidth(self._markeredgewidth)

    def get_markeredgecolor(self):
        return self._markeredgecolor # or self._plot_obj.get_markeredgecolor()

    def set_markeredgecolor(self, markeredgecolor):
        self._markeredgecolor = markeredgecolor
        if self._plot_obj is not None:
            self._plot_obj.set_markeredgecolor(self._markeredgecolor)

    def get_markerfacecolor(self):
        return self._markerfacecolor # or self._plot_obj.get_markerfacecolor # TODO check if true

    def set_markerfacecolor(self, markerfacecolor):
        self._markerfacecolor = markerfacecolor
        if self._plot_obj is not None:
            self._plot_obj.set_markerfacecolor(self._markerfacecolor)

    def get_markerfacecoloralt(self):
        return self._markerfacecoloralt

    def set_markerfacecoloralt(self, markerfacecoloralt):
        self._markerfacecoloralt = markerfacecoloralt
        if self._plot_obj is not None:
            self._plot_obj.set_markerfacecoloralt(self._markerfacecoloralt)

    def get_fillstyle(self):
        return self._fillstyle # or self._plot_obj.get_fillstyle # TODO check if true

    def set_fillstyle(self, fillstyle):
        self._fillstyle = fillstyle
        if self._plot_obj is not None:
            self._plot_obj.set_fillstyle(self._fillstyle)

    def get_antialiased(self):
        return self._antialiased # or self._plot_obj.get_antialiased

    def set_antialised(self, antialiased):
        self._antialiased = antialiased
        if self._plot_obj is not None:
            self._plot_obj.set_antialiased(self._antialiased)

    def get_dash_capstyle(self):
        return self._dash_capstyle # or self._plot_obj.get_dash_capstyle()

    def set_dash_capstyle(self, dash_capstyle):
        self._dash_capstyle = dash_capstyle
        if self._plot_obj is not None:
            self._plot_obj.set_dash_capstyle(self._dash_capstyle)

    def get_solid_capstyle(self):
        return self._solid_capstyle # or self._plot_obj.get_solid_capstyle()

    def set_solid_capstyle(self, solid_capstyle):
        self._solid_capstyle = solid_capstyle
        if self._plot_obj is not None:
            self._plot_obj.set_solid_capstyle(self._solid_capstyle)

    def get_dash_joinstyle(self):
        return self._dash_joinstyle # or self._plot_obj.get_dash_joinstyle()

    def set_dash_joinstyle(self, dash_joinstyle):
        self._dash_joinstyle = dash_joinstyle
        if self._plot_obj is not None:
            self._plot_obj.set_dash_joinstyle(self._dash_joinstyle)

    def get_solid_joinstyle(self):
        return self._solid_joinstyle # or self._plot_obj.get_solid_joinstyle

    def set_solid_joinstyle(self, solid_joinstyle):
        self._solid_capstyle = solid_joinstyle

    def get_pickradius(self):
        return self._pickradius # or self._plot_obj.get_pickradius

    def set_pickradius(self, pickradius):
        self._pickradius = pickradius
        if self._plot_obj is not None:
            self._plot_obj.set_pickradius(self._pickradius)

    def get_drawstyle(self):
        return self._drawstyle # or self._plot_obj.get_drawstyle()

    def set_drawstyle(self, drawstyle):
        self._drawstyle = drawstyle
        if self._plot_obj is not None:
            self._plot_obj.set_drawstyle(self._drawstyle)

    def get_markevery(self):
        return self._markevery # or self._plot_obj.get_markevery()

    def set_markevery(self, markevery):
        self._markevery = markevery
        if self._plot_obj is not None:
            self._plot_obj.set_markevery(self._markevery)

    def get_xdata(self):
        return self._xdata # # or self._plot_obj.get_xdata()

    def set_xdata(self, xdata):
        self._xdata = xdata
        if self._plot_obj is not None:
            self._plot_obj.set_xdata(self._xdata)

    def get_ydata(self):
        return self._ydata # or self._plot_obj.get_ydata()

    def set_ydata(self, ydata):
        self._ydata = ydata
        if self._plot_obj is not None:
            self._plot_obj.set_ydata(self._ydata)

    linewidth = Property(float, get_linewidth, set_linewidth)
    linestyle = Property(str, get_linestyle, set_linestyle)
    color = Property(str, get_color, set_color)
    c = color
    marker = Property(str, get_marker, set_marker)
    markersize = Property(float, get_markersize, set_markersize)
    markeredgewidth = Property(float, get_markeredgewidth, set_markeredgewidth)
    markeredgecolor = Property(str, get_markeredgecolor, set_markeredgecolor)
    markerfacecolor = Property(str, get_markerfacecolor, set_markerfacecolor)
    markerfacecoloralt = Property(str, get_markerfacecoloralt, set_markerfacecoloralt)
    fillstyle = Property(str, get_fillstyle, set_fillstyle)
    antialiased = Property(bool, get_antialiased, set_antialised)
    dashCapstyle = Property(str, get_dash_capstyle, set_dash_capstyle)
    solidCapstyle = Property(str, get_solid_capstyle, set_solid_capstyle)
    dashJoinstyle = Property(str, get_dash_joinstyle, set_dash_joinstyle)
    solidJoinstyle = Property(str, get_solid_joinstyle, set_solid_joinstyle)
    pickradius = Property(float, get_pickradius, set_pickradius)
    drawstyle = Property(str, get_drawstyle, set_drawstyle)
    markevery = Property(int, get_markevery, set_markevery)
    xData = Property("QVariantList", get_xdata, set_xdata)
    yData = Property("QVariantList", get_ydata, set_ydata)


Line = Line2D

from matplotlib.lines import Line2D as MatplotlibLine2D

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

    def get_linestyle(self):
        return self._plot_obj.get_linestyle() # or self._plot_obj.get_linestyle()

    def set_linestyle(self, linestyle):
        self._plot_obj.set_linestyle(linestyle)
        self.schedule_plot_update()

    def get_color(self):
        return self._color # or self._plot_obj.get_color()

    def set_color(self, color):
        self._plot_obj.set_color(color)
        self.schedule_plot_update()
    
    def get_marker(self):
        return self._plot_obj.get_marker() # or self._plot_obj.get_marker # TODO check if thats true

    def set_marker(self, marker):
        self._plot_obj.set_marker(marker)
        self.schedule_plot_update()

    def get_markersize(self):
        return self._plot_obj.get_markersize()

    def set_markersize(self, markersize):
        self._plot_obj.set_markersize(markersize)
        self.schedule_plot_update()

    def get_markeredgewidth(self):
        return self._plot_obj.get_markeredgewidth() # or self._plot_obj.get_markeredgewidth # TODO check if true

    def set_markeredgewidth(self, markeredgewidth):
        self._plot_obj.set_markeredgewidth(markeredgewidth)
        self.schedule_plot_update()

    def get_markeredgecolor(self):
        return self._plot_obj.get_markeredgecolor() # or self._plot_obj.get_markeredgecolor()

    def set_markeredgecolor(self, markeredgecolor):
        self._plot_obj.set_markeredgecolor(markeredgecolor)
        self.schedule_plot_update()

    def get_markerfacecolor(self):
        return self._plot_obj.get_markerfacecolor() # or self._plot_obj.get_markerfacecolor # TODO check if true

    def set_markerfacecolor(self, markerfacecolor):
        self._plot_obj.set_markerfacecolor(markerfacecolor)
        self.schedule_plot_update()

    def get_markerfacecoloralt(self):
        return self._plot_obj.get_markerfacecoloralt()

    def set_markerfacecoloralt(self, markerfacecoloralt):
        self._plot_obj.set_markerfacecoloralt(markerfacecoloralt)
        self.schedule_plot_update()

    def get_fillstyle(self):
        return self._plot_obj.get_fillstyle() # or self._plot_obj.get_fillstyle # TODO check if true

    def set_fillstyle(self, fillstyle):
        self._plot_obj.set_fillstyle(fillstyle)
        self.schedule_plot_update()

    def get_antialiased(self):
        return self._plot_obj.get_antialiased

    def set_antialised(self, antialiased):
        self._plot_obj.set_antialiased(antialiased)
        self.schedule_plot_update()

    def get_dash_capstyle(self):
        return self._plot_obj.get_dash_capstyle()

    def set_dash_capstyle(self, dash_capstyle):
        self._plot_obj.set_dash_capstyle(dash_capstyle)
        self.schedule_plot_update()

    def get_solid_capstyle(self):
        return self._plot_obj.get_solid_capstyle()

    def set_solid_capstyle(self, solid_capstyle):
        self._plot_obj.set_solid_capstyle(solid_capstyle)
        self.schedule_plot_update()

    def get_dash_joinstyle(self):
        return self._plot_obj.get_dash_joinstlye()

    def set_dash_joinstyle(self, dash_joinstyle):
        self._plot_obj.set_dash_joinstyle(dash_joinstyle)
        self.schedule_plot_update()

    def get_solid_joinstyle(self):
        return self._plot_obj.get_solid_joinstyle() # or self._plot_obj.get_solid_joinstyle

    def set_solid_joinstyle(self, solid_joinstyle):
        self._plot_obj.set_solid_joinstyle(solid_joinstyle)

    def get_pickradius(self):
        return self._plot_obj.get_pickradius # or self._plot_obj.get_pickradius

    def set_pickradius(self, pickradius):
        self._plot_obj.set_pickradius(self._pickradius)

    def get_drawstyle(self):
        return self._plot_obj.get_drawstyle() # or self._plot_obj.get_drawstyle()

    def set_drawstyle(self, drawstyle):
        self._plot_obj.set_drawstyle(drawstyle)
        self.schedule_plot_update()

    def get_markevery(self):
        return self._plot_obj.get_markevery() # or self._plot_obj.get_markevery()

    def set_markevery(self, markevery):
        self._plot_obj.set_markevery(markevery)
        self.schedule_plot_update()

    def get_xdata(self):
        return self._plot_obj.get_xdata() # # or self._plot_obj.get_xdata()

    def set_xdata(self, xdata):
        self._plot_obj.set_xdata(xdata)
        self.schedule_plot_update()

    def get_ydata(self):
        return self._plot_obj.get_ydata() # or self._plot_obj.get_ydata()

    def set_ydata(self, ydata):
        self._plot_obj.set_ydata(ydata)
        self.schedule_plot_update()
        


    linewidth = Property(float, get_linewidth, set_linewidth)
    linestyle = Property(str, get_linestyle, set_linestyle)
    color = Property(str, get_color, set_color)
    c = color
    marker = Property(str, get_marker, set_marker)
    markersize = Property(float, get_markersize, set_markersize)
    markeredgewidth = Property(float, get_markeredgewidth, set_markeredgewidth)
    markeredgecolor = Property(str, get_markeredgecolor, set_markeredgecolor)
    markerfacecolor = Property(str, get_markerfacecolor, set_markerfacecolor)
    markerfacecoloralt = Property(str, get_markerfacecoloralt, set_markerfacecoloralt)
    fillstyle = Property(str, get_fillstyle, set_fillstyle)
    antialiased = Property(bool, get_antialiased, set_antialised)
    dashCapstyle = Property(str, get_dash_capstyle, set_dash_capstyle)
    solidCapstyle = Property(str, get_solid_capstyle, set_solid_capstyle)
    dashJoinstyle = Property(str, get_dash_joinstyle, set_dash_joinstyle)
    solidJoinstyle = Property(str, get_solid_joinstyle, set_solid_joinstyle)
    pickradius = Property(float, get_pickradius, set_pickradius)
    drawstyle = Property(str, get_drawstyle, set_drawstyle)
    markevery = Property(int, get_markevery, set_markevery)
    xData = Property("QVariantList", get_xdata, set_xdata)
    yData = Property("QVariantList", get_ydata, set_ydata)


Line = Line2D



    