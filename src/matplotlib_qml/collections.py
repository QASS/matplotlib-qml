from matplotlib.collections import PathCollection as MatplotlibPathCollection
from PySide2.QtCore import Property, Slot, Signal
import numpy as np

from .artist import Artist
from .cm import ScalarMappable
from .event import EventHandler, EventTypes
from .utils import numpy_compatibility

# TODO updates to decorator
# TODO add callback function to artist for plot updates

class Collection(Artist, ScalarMappable):
    """THis object needs to keep track of the plot_objects data structures since the plot object can't be instantiated 
    outside of an axis thus requiring to be updated by the state of the wrapper object"""
    def __init__(self, parent=None):
        self._plot_obj = None
        Artist.__init__(self, parent)
        ScalarMappable.__init__(self)
        self._edgecolors=None # fallback if edgecolors is None {'face', 'none', None} or list of color or sequence of color
        self._edgecolor = "face"
        self._facecolors=None
        self._facecolor = None # fallback if facecolors is None
        self._linewidths=None
        self._linewidth = 1.5 # fallback if linewidths is None
        self._linestyles= "solid" # is by default a string
        self._capstyle=None
        self._joinstyle=None
        self._antialiased=None
        self._offsets=None
        self._transOffset=None
        self._pickradius=5.0
        self._hatch=None
        self._urls=None
        self._offset_position='screen'
        

        # set_paths is not implemented in the base class and raises an error (only the getter for the paths)
    @property
    def kwargs(self):
        kwargs = super(Collection, self).kwargs # this gets the Artist kwargs (__mro__)
        for key, value in super(Artist, self).kwargs.items(): # this gets the ScalarMappable kwargs
            kwargs[key] = value
        kwargs["edgecolor"] = self._edgecolors if self._edgecolors is not None else self._edgecolor
        kwargs["facecolor"] = self._facecolors if self._facecolors is not None else self._facecolor
        kwargs["linewidth"] = self._linewidths if self._linewidths is not None else self._linewidth
        kwargs["linestyle"] = self._linestyles
        kwargs["antialiased"] = self._antialiased
        kwargs["hatch"] = self._hatch
        return kwargs

    @numpy_compatibility
    def get_edgecolors(self):
        if self._plot_obj is None:
            return self._edgecolors
        return self._plot_obj.get_color() # returns the edgecolors under the hood

    def set_edgecolors(self, edgecolors):
        """In matplotlib it is possible to provide one color for the whole collection or a list of colors
        This setter can be used to provide a list of colors"""
        self._edgecolors = edgecolors
        if self._plot_obj is not None:
            self._plot_obj.set_edgecolor(edgecolors)
            self.schedule_plot_update()
            self.markerEdgeColorsChanged.emit()

    @numpy_compatibility
    def get_edgecolor(self):
        if self._plot_obj is None:
            return self._edgecolor
        return self._plot_obj.get_edgecolor() # TODO check if list or string

    def set_edgecolor(self, edgecolor):
        self._edgecolor = edgecolor
        if self._plot_obj is not None:
            self._plot_obj.set_edgecolor(edgecolor)
            self.schedule_plot_update()
            self.markerEdgeColorChanged.emit()

    @numpy_compatibility
    def get_facecolors(self):
        if self._plot_obj is None:
            return self._facecolors[0]
        return self._plot_obj.get_facecolor()[0] # returns the edgecolors under the hood

    def set_facecolors(self, facecolors):
        """In matplotlib it is possible to provide one color for the whole collection or a list of colors
        This setter can be used to provide a list of colors"""
        self._plot_obj.set_facecolor(facecolors)
        self.schedule_plot_update()        
    
    @numpy_compatibility
    def get_facecolor(self):
        if self._plot_obj is None:
            return self._facecolors
        return self._plot_obj.get_facecolor()

    def set_facecolor(self, facecolor):
        self._plot_obj.set_facecolor(facecolor)

    @numpy_compatibility
    def get_linewidths(self):
        if self._plot_obj is None:
            return self._linewidths
        return self._plot_obj.get_linewidth() # or self._plot_obj.get_linewidth()

    def set_linewidths(self, linewidths):
        self._linewidths = linewidths
        if self._plot_obj is not None:
            self._plot_obj.set_linewidth(linewidths)
            self.schedule_plot_update()
            self.linewidthsChanged.emit()

    @numpy_compatibility
    def get_linewidth(self):
        if self._plot_obj is None:
            return self._linewidth
        return self._plot_obj.get_linewidth() # or self._plot_obj.get_linewidth()

    def set_linewidth(self, linewidth):
        self._linewidth = linewidth
        if self._plot_obj is not None:
            self._plot_obj.set_linewidth(linewidth)
            self.schedule_plot_update()
            self.linewidthChanged.emit()

    def get_linestyle(self):
        if self._plot_obj is None:
            return self._linestyles
        return self._plot_obj.get_linestyle() # or self._plot_obj.get_linestyle()

    def set_linestyle(self, linestyle):
        self._linestyles = linestyle
        if self._plot_obj is not None:
            self._plot_obj.set_linestyle(self._linestyles)
            self.schedule_plot_update()
            self.linestyleChanged.emit()

    def get_pickradius(self):
        if self._plot_obj is None:
            return self._pickradius
        return self._plot_obj.get_pickradius() # or self._plot_obj.get_pickradius

    def set_pickradius(self, pickradius):
        self._plot_obj.set_pickradius(pickradius)
        self.schedule_plot_update()

    def get_hatch(self):
        if self._plot_obj is None:
            return self._hatch
        return self._plot_obj.get_hatch()

    def set_hatch(self, hatch):
        self._hatch = hatch
        if self._plot_obj is not None:
            self._plot_obj.set_hatch(hatch)
            self.schedule_plot_update()
            self.hatchChanged.emit()

    def get_capstyle(self):
        if self._plot_obj is None:
            return self._capstyle
        return self._plot_obj.get_capstyle()

    def set_capstyle(self, capstyle):
        self._plot_obj.set_capstyle(capstyle)
        self.schedule_plot_update()

    def get_joinstyle(self):
        if self._plot_obj is None:
            return self._joinstyle
        return self._plot_obj.get_joinstyle()

    def set_joinstyle(self, joinstyle):
        self._plot_obj.set_joinstyle(joinstyle)
        self.schedule_plot_update()

    @numpy_compatibility
    def get_color(self):
        if self._plot_obj is None:
            return self._edgecolors
        return self._plot_obj.get_color() # returns the edgecolors under the hood

    def set_color(self, color):
        """In matplotlib the color attribute sets the facecolor under the hood. Not setting the edgecolor results
        in it defaulting to the facecolor"""
        self._facecolor = color
        if self._plot_obj is not None:
            self._plot_obj.set_color(color)
            self.schedule_plot_update()
            self.colorChanged.emit()

    @numpy_compatibility
    def get_colors(self):
        """By default return the facecolor"""
        return self._plot_obj.get_color() # returns the edgecolors under the hood

    def set_colors(self, colors):
        """In matplotlib it is possible to provide one color for the whole collection or a list of colors
        This setter can be used to provide a list of colors"""
        if self._facecolors is None:
            self._facecolors = colors
        if self._plot_obj is not None:
            # self._plot_obj.set_color(colors)
            self.set_array(colors)
            # self.set_array
            self.schedule_plot_update()
            self.colorsChanged.emit()
            self.cChanged.emit()

    colorsChanged = Signal()
    cChanged = Signal()
    colorChanged = Signal()
    markerEdgeColorsChanged = Signal()
    markerEdgeColorChanged = Signal()
    linewidthsChanged = Signal()
    linewidthChanged = Signal()
    linestyleChanged = Signal()
    hatchChanged = Signal()

    colors = Property("QVariantList", get_colors, set_colors)
    c = colors
    color = Property(str, get_color, set_color)
    markerEdgeColors = Property("QVariantList", get_edgecolors, set_edgecolors)
    markerEdgeColor = Property(str, get_edgecolor, set_edgecolor)
    linewidths = Property("QVariantList", get_linewidths, set_linewidths)
    linewidth = Property(float, get_linewidth, set_linewidth)
    linestyle = Property(str, get_linestyle, set_linestyle)
    hatch = Property(str, get_hatch, set_hatch)

class _CollectionWithSizes(Collection):
    def __init__(self, parent=None):
        super().__init__(parent)
        self._sizes = None
        self._size = 20

    @numpy_compatibility
    def get_sizes(self):
        if self._plot_obj is None:
            return self._sizes
        return self._plot_obj.get_sizes()

    def set_sizes(self, sizes):
        self._sizes = sizes
        if self._plot_obj is not None:
            self._plot_obj.set_sizes(sizes)
            self.schedule_plot_update()
            self.markerSizesChanged.emit()
            self.sChanged.emit()

    @numpy_compatibility
    def get_size(self):
        if self._plot_obj is None or self._sizes is None:
            return self._size
        return self._plot_obj.get_sizes()

    def set_size(self, size):
        """sizes always have priority over size. 
        Even though size is a single value it must be provided as an iterable (list,tuple,np.array)
        In order to keep the state of the wrapper synchron with QML property compatibilities it needs to be done like this"""
        self._size = size
        if self._plot_obj is not None and self._sizes is None:
            self._plot_obj.set_sizes((size,))
            self.schedule_plot_update()
            self.markerSizeChanged.emit()
            

    markerSizesChanged = Signal()
    sChanged = Signal()
    markerSizeChanged = Signal()

    markerSizes = Property("QVariantList", get_sizes, set_sizes)
    s = markerSizes
    markerSize = Property(float, get_size, set_size)
    

class PathCollection(_CollectionWithSizes):
    def __init__(self, parent=None):
        # self._plot_obj = MatplotlibPathCollection()
        super().__init__(parent)
        self._paths = []

    def get_paths(self):
        return self._plot_obj.get_paths()

    def set_paths(self, paths):
        """paths must be a tuple or list"""
        self._plot_obj.set_paths(paths)


class PolyCollection(_CollectionWithSizes):
    """ This is class has been auto generated. PLEASE PROVIDE DOCUMENTATION!!! """

    def __init__(self, parent = None):
        super().__init__(parent)
        self._verts = []

    def get_verts(self):
        if self._plot_obj is None:
            return self._verts
        return self._plot_obj.get_verts()

    def set_verts(self, verts):
        self._verts = verts
        if self._plot_obj is not None:
            self._plot_obj.set_verts(self._verts)
            self.schedule_plot_update()

    # No signal here since verts won't become a valid property for now
    
    verts = Property("QVariantList", get_verts, set_verts)


