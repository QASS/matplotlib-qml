from matplotlib.collections import PathCollection as MatplotlibPathCollection
from PySide2.QtCore import Property, Slot, Signal
import numpy as np

from matplotlib_bridge.artist import Artist
from matplotlib_bridge.cm import ScalarMappable
from matplotlib_bridge.event import EventHandler, EventTypes

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
        self._antialiaseds=None
        self._offsets=None
        self._transOffset=None
        self._norm=None  # optional for ScalarMappable
        self._cmap=None  # ditto
        self._pickradius=5.0
        self._hatch=None
        self._urls=None
        self._offset_position='screen'
        

        # set_paths is not implemented in the base class and raises an error (only the getter for the paths)

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

    def get_edgecolor(self):
        if self._plot_obj is None:
            return self._edgecolor
        return self._plot_obj.get_edgecolor() # TODO check if list or string

    def set_edgecolor(self, edgecolor):
        self._edgecolor = edgecolor
        if self._plot_obj is not None:
            self._plot_obj.set_edgecolor(edgecolor)
            self.schedule_plot_update()

    def get_facecolors(self):
        if self._plot_obj is None:
            return self._facecolors[0]
        return self._plot_obj.get_facecolor()[0] # returns the edgecolors under the hood

    def set_facecolors(self, facecolors):
        """In matplotlib it is possible to provide one color for the whole collection or a list of colors
        This setter can be used to provide a list of colors"""
        self._plot_obj.set_facecolor(facecolors)
    
    def get_facecolor(self):
        if self._plot_obj is None:
            return self._facecolors
        return self._plot_obj.get_facecolor()

    def set_facecolor(self, facecolor):
        self._plot_obj.set_facecolor(facecolor)

    def get_linewidths(self):
        if self._plot_obj is None:
            return self._linewidths
        return self._plot_obj.get_linewidth() # or self._plot_obj.get_linewidth()

    def set_linewidths(self, linewidths):
        self._linewidths = linewidths
        if self._plot_obj is not None:
            self._plot_obj.set_linewidth(linewidths)
            self.schedule_plot_update()

    def get_linewidth(self):
        if self._plot_obj is None:
            return self._linewidth
        return self._plot_obj.get_linewidth() # or self._plot_obj.get_linewidth()

    def set_linewidth(self, linewidth):
        self._linewidth = linewidth
        if self._plot_obj is not None:
            self._plot_obj.set_linewidth(linewidth)
            self.schedule_plot_update()

    def get_linestyle(self):
        if self._plot_obj is None:
            return self._linestyles
        return self._plot_obj.get_linestyle() # or self._plot_obj.get_linestyle()

    def set_linestyle(self, linestyle):
        self._plot_obj.set_linestyle(linestyle)
        self.schedule_plot_update()

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
        if self._plot_obj is not None:
            self._plot_obj.set_hatch(hatch)
            self.schedule_plot_update()

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

    # def get_alpha(self):
    #     return super().get_alpha()

    # def set_alpha(self, alpha):#
    #     """This method needs to be overwritten since the collection manages edge and facecolors 
    #     which are handled differently"""
    #     self._alpha = alpha
    #     if self._plot_obj is not None:
    #         self._plot_obj.set_alpha(alpha)
    #         self.schedule_plot_update()

    

    colors = Property("QVariantList", get_colors, set_colors)
    c = colors
    color = Property(str, get_color, set_color)
    markerEdgeColors = Property("QVariantList", get_edgecolors, set_edgecolors)
    markerEdgeColor = Property(str, get_edgecolor, set_edgecolor)
    linewidths = Property("QVariantList", get_linewidths, set_linewidths)
    linewidth = Property(float, get_linewidth, set_linewidth)
    hatch = Property(str, get_hatch, set_hatch)

class _CollectionWithSizes(Collection):
    def __init__(self, parent=None):
        super().__init__(parent)
        self._sizes = None
        self._size = 20

    def get_sizes(self):
        if self._plot_obj is None:
            return self._sizes
        return self._plot_obj.get_sizes()

    def set_sizes(self, sizes):
        self._sizes = sizes
        if self._plot_obj is not None:
            self._plot_obj.set_sizes(sizes)
            self.schedule_plot_update()

    def get_size(self):
        if self._plot_obj is None:
            return self._size
        return self._plot_obj.get_sizes()

    def set_size(self, size):
        self._size = size
        if self._plot_obj is not None:
            self._plot_obj.set_sizes(size)
            self.schedule_plot_update()

    sizes = Property("QVariantList", get_sizes, set_sizes)
    s = sizes
    size = Property(float, get_size, set_size)
    

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

from matplotlib.markers import MarkerStyle

class ScatterCol(PathCollection):
    """A Collection can't exist outside of an axes because it requires the transform data"""
    OFFSET_CHANGED = "OFFSET_CHANGED"

    def __init__(self, parent=None):
        super().__init__(parent)
        self._x = []
        self._y = []
        self._marker = "o"
        self._ax = None
        self._scatter_event_handler = EventHandler()

    def init(self, ax):       
        self._ax = ax
        self._create_plot_obj(ax)
        # initialize the ScalarMappable to enable the colorbar
        ScalarMappable.init(self, ax)
        self._scatter_event_handler.register(self.OFFSET_CHANGED, self._adjust_offset)

    def _create_plot_obj(self, ax):
        """First check whether there are lists of properties otherwise fall back to the defaults or single properties"""
        edgecolors = self._edgecolors if self._edgecolors is not None else self._edgecolor
        colors = self._facecolors if self._facecolors is not None else self._facecolor
        linewidths = self._linewidths if self._linewidths is not None else self._linewidth
        sizes = self._sizes if self._sizes is not None else self._size
        self._plot_obj = ax.scatter(self._x, self._y, c = colors, s = sizes, marker = self._marker, cmap = self._cmap, 
                                    norm = None, vmin = self._vmin, vmax = self._vmax, alpha = self._alpha, 
                                    linewidths = linewidths, edgecolors = edgecolors, hatch = self._hatch)

    def _adjust_offset(self):
        x = np.array(self._x).reshape(len(self._x), 1)
        y = np.array(self._y).reshape(len(self._y), 1)

        offsets = np.hstack((x, y))
        self._plot_obj.set_offsets(offsets)
    
    def get_x(self):
        if isinstance(self._x, np.ndarray):
            return self._x.tolist()
        return self._x

    def set_x(self, x):
        self._x = x
        if self._plot_obj is not None:
            if len(self._x ) == len(self._y):
                self._adjust_offset()
                self.schedule_plot_update()

    def get_y(self):
        if isinstance(self._y, np.ndarray):
            return self._y.tolist()
        return self._y

    def set_y(self, y):
        self._y = y
        if self._plot_obj is not None:
            if len(self._x ) == len(self._y):
                self._adjust_offset()
                self.schedule_plot_update()

    def get_marker(self):
        return self._marker

    def set_marker(self, marker):
        """Fetch the marker style and the current applied transform of the marker style object"""
        self._marker = marker
        if self._plot_obj is not None:            
            marker_obj = MarkerStyle(marker)
            marker_path = marker_obj.get_path().transformed(marker_obj.get_transform())
            self.set_paths((marker_path,))
            self.schedule_plot_update()


    xChanged = Signal()
    yChanged = Signal()

    x = Property("QVariantList", get_x, set_x, notify = xChanged)
    y = Property("QVariantList", get_y, set_y, notify = yChanged)
    marker = Property(str, get_marker, set_marker)
