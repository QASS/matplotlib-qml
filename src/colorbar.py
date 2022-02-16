
from multiprocessing import set_forkserver_preload
from PySide2.QtCore import Signal, Slot, Property, QObject
from PySide2.QtQuick import QQuickItem
from plot_objects import Base 
from event import EventHandler, EventTypes
from matplotlib.colorbar import Colorbar as MatplotlibColorbar
from matplotlib.colorbar import make_axes

# Matplotlib source code: https://github.com/matplotlib/matplotlib/blob/v3.5.1/lib/matplotlib/colorbar.py

class Colorbar(Base):
    """Wrapper class for matplotlib.colorbar.Colorbar. Can be used to populate the 'colorbar' Property of 
    Scalar Mappables like Imshow or ScatterCollection
    
    Modifying the properties at runtime result in the object being reinstantiated which causes overhead
    """
    def __init__(self, parent = None):
        super().__init__(parent)
        self._orientation = "vertical"
        self._label = ""
        self._fraction_of_original_axis = 0.15
        self._location = "right"
        self._shrink = 1.0
        self._aspect = 20
        self._padding = 0.1        
        self._drawedges = False
        self._filled = True

        self._label_location = "center"
        self._ax = None # The axis the colorbar is drawn next to
        self._mappable = None # the mappable object from which the cbar derives
        self._cbar_event_handler = EventHandler()

    @property
    def colorbar_kwargs(self):        
        kwargs = dict()
        kwargs["orientation"] = self._orientation
        kwargs["label"] = self._label
        kwargs["location"] = self._location
        kwargs["fraction"] = self._fraction_of_original_axis
        kwargs["shrink"] = self._shrink
        kwargs["aspect"] = self._aspect
        kwargs["drawedges"] = self._drawedges
        kwargs["filled"] = self._filled
        return kwargs

    def init(self, ax, mappable):
        self._mappable = mappable
        self._ax = ax
        self._create_plot_obj(ax, self._mappable)
        self._cbar_event_handler.register(EventTypes.PLOT_DATA_CHANGED, self.redraw)

    def _create_plot_obj(self, ax, mappable):
        cax, kwargs = make_axes(ax, **self.colorbar_kwargs)
        self._plot_obj = MatplotlibColorbar(cax, mappable=mappable, **kwargs)
        self._plot_obj.set_label(self._label, loc = self._label_location)

    def redraw(self):
        """Delete the current plot object and reinstantiate it with the new parameters"""
        if self._plot_obj is not None:
            self._plot_obj.remove()
            self._plot_obj = None
        # we need to call tight layout to rescale the axis since we "stole" some space earlier to create
        # the axis for the cbar
        self._ax.figure.tight_layout(rect = (0, 0.05, 1, 1))
        self._create_plot_obj(self._ax, self._mappable)
        self._event_handler.schedule(EventTypes.AXIS_DATA_CHANGED)
        self._event_handler.schedule(EventTypes.PLOT_DATA_CHANGED)

    def update_normal(self, mappable):
        """This is meant to be called when the norm of the image or contour plot
        to which this colorbar belongs changes."""
        self._plot_obj.update_normal(mappable)

    def remove(self):
        self._plot_obj.remove()
        self._plot_obj = None
        self._event_handler.schedule(EventTypes.PLOT_DATA_CHANGED)

    def update_mappable(self, mappable):
        """If the mappable related to the colorbar changes the colorbar needs to be reinstantiated in case vmin
        and vmax changed on the mappable"""
        self._mappable = mappable
        self._cbar_event_handler.schedule(EventTypes.PLOT_DATA_CHANGED)

    def get_orientation(self):
        return self._orientation

    def set_orientation(self, orientation):
        self._orientation = orientation
        if self._plot_obj is not None:
            self._cbar_event_handler.schedule(EventTypes.PLOT_DATA_CHANGED)
    
    def get_label(self):
        return self._label

    def set_label(self, label):
        self._label = label
        if self._plot_obj is not None:
            self._plot_obj.set_label(self._label, loc = self._label_location)
            self._event_handler.schedule(EventTypes.PLOT_DATA_CHANGED)

    def get_location(self):
        return self._location

    def set_location(self, location):
        self._location = location
        if self._plot_obj is not None:
            self._cbar_event_handler.schedule(EventTypes.PLOT_DATA_CHANGED)

    def get_fraction(self):
        return self._fraction_of_original_axis

    def set_fraction(self, fraction):
        self._fraction_of_original_axis = fraction
        if self._plot_obj is not None:
            self._cbar_event_handler.schedule(EventTypes.PLOT_DATA_CHANGED)

    def get_shrink(self):
        return self._shrink
    
    def set_shrink(self, shrink):
        self._shrink = shrink
        if self._plot_obj is not None:
            self._cbar_event_handler.schedule(EventTypes.PLOT_DATA_CHANGED)

    def get_aspect(self):
        return self._aspect

    def set_aspect(self, aspect):
        self._aspect = aspect
        if self._plot_obj is not None:
            self._cbar_event_handler.schedule(EventTypes.PLOT_DATA_CHANGED)

    def get_drawedges(self):
        return self._drawedges

    def set_drawedges(self, drawedges):
        self._drawedges = drawedges
        if self._plot_obj is not None:
            self._cbar_event_handler.schedule(EventTypes.PLOT_DATA_CHANGED)

    def get_filled(self):
        return self._filled

    def set_filled(self, filled):
        self._filled = filled
        if self._plot_obj is not None:
            self._cbar_event_handler.schedule(EventTypes.PLOT_DATA_CHANGED)

    def get_label_location(self):
        return self._label_location

    def set_label_location(self, location):
        self._label_location = location
        if self._plot_obj is not None:
            self._plot_obj.set_label(self._label, loc = self._label_location)
            self._event_handler.schedule(EventTypes.PLOT_DATA_CHANGED)


    orientation = Property(str, get_orientation, set_orientation)
    label = Property(str, get_label, set_label)
    location = Property(str, get_location, set_location)
    fraction = Property(float, get_fraction, set_fraction)
    shrink = Property(float, get_shrink, set_shrink)
    aspect = Property(int, get_aspect, set_aspect)
    drawEdges = Property(bool, get_drawedges, set_drawedges)
    filled = Property(bool, get_filled, set_filled)
    labelLocation = Property(str, get_label_location, set_label_location)

