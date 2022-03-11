from matplotlib import rcParams
from PySide2.QtCore import Property
from matplotlib.lines import Line2D as MatplotlibLine2D

from matplotlib_bridge.artist import Artist
from matplotlib_bridge.event import EventTypes


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
        self._plot_obj.set_pickradius(pickradius)

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



    