
from PySide2.QtCore import Signal, Slot, Property, QObject
from PySide2.QtQuick import QQuickItem
from graphs_2d import PlotObject2D
from plot_objects import Axis
from event import EventHandler, EventTypes
from matplotlib.colorbar import Colorbar as MatplotlibColorbar
from matplotlib.colorbar import make_axes

# Matplotlib source code: https://github.com/matplotlib/matplotlib/blob/v3.5.1/lib/matplotlib/colorbar.py

class Colorbar(QObject):
    def __init__(self, parent = None):
        super().__init__(parent)
        self._plot_obj = None
        self._alpha = None
        self._orientation = "vertical"
        self._ticklocation = "auto"
        self._label = ""

    @property
    def colorbar_kwargs(self):
        kwargs = {
            "alpha" : self._alpha,
            "orientation" : self._orientation,
            "ticklocation" : self._ticklocation,
            "label" : self._label
        }
        return kwargs

    def init(self, ax, mappable):
        cax, kw = make_axes(ax, **self.colorbar_kwargs)
        self._plot_obj = MatplotlibColorbar(cax, mappable=mappable)#, **self.colorbar_kwargs)

    def update_normal(self, mappable):
        """This is meant to be called when the norm of the image or contour plot
        to which this colorbar belongs changes."""
        self._plot_obj.update_normal(mappable)
