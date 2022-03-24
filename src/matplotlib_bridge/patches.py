from PySide2.QtCore import Property
from matplotlib.patches import Polygon

from matplotlib_bridge.artist import Artist


class Patch(Artist): # TODO SPAN
    def __init__(self, parent=None):
        super().__init__(parent)
        self._antialiased = None
        self._edgecolor = None
        self._facecolor = None
        self._color = None
        self._linewidth = None
        self._linestyle = None
        self._hatch = None
        self._fill = True
        self._capstyle = None
        self._joinstyle = None

    @property
    def kwargs(self):
        kwargs = super().kwargs
        kwargs["antialiased"] = self._antialiased
        kwargs["edgecolor"] = self._edgecolor
        kwargs["facecolor"] = self._facecolor
        kwargs["color"] = self._color
        kwargs["linewidth"] = self._linewidth
        kwargs["linestyle"] = self._linestyle
        kwargs["hatch"] = self._hatch
        kwargs["fill"] = self._fill
        kwargs["capstyle"] = self._capstyle
        kwargs["joinstyle"] = self._joinstyle
        return kwargs

    def get_antialiased(self):
        if self._plot_obj is None:
            return self._antialiased
        return self._plot_obj.get_antialiased()

    def set_antialiased(self, antialiased):
        self._antialiased = antialiased
        if self._plot_obj is not None:
            self._plot_obj.set_antialiased(self._antialiased)
            self.schedule_plot_update()

    def get_edgecolor(self):
        if self._plot_obj is None:
            return self._edgecolor
        return self._plot_obj.get_edgecolor()

    def set_edgecolor(self, edgecolor):
        self._edgecolor = edgecolor
        if self._plot_obj is not None:
            self._plot_obj.set_edgecolor(self._edgecolor)
            self.schedule_plot_update()

    def get_facecolor(self):
        if self._plot_obj is None:
            return self._facecolor
        return self._plot_obj.get_facecolor()

    def set_facecolor(self, facecolor):
        self._facecolor = facecolor
        if self._plot_obj is not None:
            self._plot_obj.set_facecolor(self._facecolor)
            self.schedule_plot_update()

    def get_color(self):
        if self._plot_obj is None:
            return self._color
        return self._plot_obj.get_color()

    def set_color(self, color):
        self._color = color
        if self._plot_obj is not None:
            self._plot_obj.set_color(self._color)
            self.schedule_plot_update()

    def get_linewidth(self):
        if self._plot_obj is None:
            return self._linewidth
        return self._plot_obj.get_linewidth()

    def set_linewidth(self, linewidth):
        self._linewidth = linewidth
        if self._plot_obj is not None:
            self._plot_obj.set_linewidth(self._linewidth)
            self.schedule_plot_update()

    def get_linestyle(self):
        if self._plot_obj is None:
            return self._linestyle
        return self._plot_obj.get_linestyle

    def set_linestyle(self, linestyle):
        self._linestyle = linestyle
        if self._plot_obj is not None:
            self._plot_obj.set_linestyle(self._linestyle)
            self.schedule_plot_update()

    def get_hatch(self):
        if self._plot_obj is None:
            return self._hatch
        return self._plot_obj.get_hatch()

    def set_hatch(self, hatch):
        self._hatch = hatch
        if self._plot_obj is not None:
            self._plot_obj.set_hatch(self._hatch)

    def get_fill(self):
        if self._plot_obj is None:
            return self._fill
        return self._plot_obj.get_fill()

    def set_fill(self, fill):
        self._fill = fill
        if self._plot_obj is not None:
            self._plot_obj.set_fill(self._fill)
            self.schedule_plot_update()

    def get_capstyle(self):
        if self._plot_obj is None:
            return self._capstyle
        return self._plot_obj.get_capstyle()

    def set_capstyle(self, capstyle):
        self._capstyle = capstyle
        if self._plot_obj is not None:
            self._plot_obj.set_capstyle(self._capstyle)
            self.schedule_plot_update()


    def get_joinstyle(self):
        if self._plot_obj is None:
            return self._joinstyle
        return self._plot_obj.get_joinstyle()

    def set_joinstyle(self, joinstyle):
        self._joinstyle = joinstyle
        if self._plot_obj is not None:
            self._plot_obj.set_joinstyle(joinstyle)

    antialiased = Property(bool, get_antialiased, set_antialiased)
    edgecolor = Property(str, get_edgecolor, set_edgecolor)
    facecolor = Property(str, get_facecolor, set_facecolor)
    color = Property(str, get_color, set_color)
    linewidth = Property(float, get_linewidth, set_linewidth)
    linestyle = Property(str, get_linestyle, set_linestyle)
    hatch = Property(str, get_hatch, set_hatch)
    fill = Property(bool, get_fill, set_fill)
    capstyle = Property(str, get_capstyle, set_capstyle)
    joinstyle = Property(str, get_joinstyle, set_joinstyle)


class Polygon(Patch):
    def __init__(self, parent=None):
        super().__init__(parent)
        # self._xy = [] official Property
        self._closed = True

    @property
    def kwargs(self):
        kwargs = super().kwargs
        kwargs["closed"] = self._closed
        return kwargs

    def get_closed(self):
        if self._plot_obj is None:
            return self._closed
        return self._plot_obj.get_closed()

    def set_closed(self, closed):
        self._closed = closed
        if self._plot_obj is not None:
            self._plot_obj.set_closed(self._closed)

    closed = Property(bool, get_closed, set_closed)


class HSpan(Polygon):
    def __init__(self, parent=None):
        self._plot_obj = None
        super().__init__(parent)
        self._ymin = 0
        self._ymax = 1
        self._xmin = 0.0
        self._xmax = 1.0

        self._ax = None
   

    def init(self, ax):
        self._ax = ax
        self._plot_obj = self._ax.axhspan(self._ymin, self._ymax, self._xmin, self._xmax, **self.kwargs)

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
            if self._plot_obj.get_closed():
                xy[4][1] = self._ymin
            self._plot_obj.set_xy(xy)
            self.schedule_plot_update()

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
            self._plot_obj.set_xy(xy)
            self.schedule_plot_update()

    def get_xmin(self):
        return self._xmin

    def set_xmin(self, xmin):
        self._xmin = float(xmin)
        if self._plot_obj is not None:
            # Modify the reference of xy which also modifies the property xy
            xy = self._plot_obj.get_xy()
            xy[0][0] = self._xmin
            xy[1][0] = self._xmin
            if self._plot_obj.get_closed():
                xy[4][0] = self._xmin
            self._plot_obj.set_xy(xy)
            self.schedule_plot_update()

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
            self.schedule_plot_update()

    yMin = Property(float, get_ymin, set_ymin)
    yMax = Property(float, get_ymax, set_ymax)
    xMin = Property(float, get_xmin, set_xmin)
    xMax = Property(float, get_xmax, set_xmax)