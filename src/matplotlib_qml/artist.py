from PySide2.QtCore import QObject, Property, Signal

from .event import EventTypes
from .utils import numpy_compatibility

class Artist(QObject):
    """Wrapper class for matplotlib.artist.Artist
    The state of the matplotlib object is synchronized with the internal state of the wrapper object because collections
    and possibly other objects can only be instantiated after the figure has been initialized"""
    def __init__(self, parent = None):
        super().__init__(parent)
        # self._plot_obj = None
        self._axes = None

        # self._transform = None
        # self._transformSet = False
        self._visible = True
        # self._animated = False
        self._alpha = None
        # self._clipbox = None # thats some sort of object and probably not usable in QML
        # self._clippath = None
        self._clipon = True
        self._label = None
        self._zorder = 0 # TODO check default
        self._picker = None
        # self._contains = None
        # self._rasterized = None
        # self._agg_filter = None
        self._picker = None
        self._zorder = 1

        # self._plot_obj = None
        self.figure = None
        self._event_handler = None

    @property
    def kwargs(self):
        kwargs = {
            "visible": self._visible,
            "alpha": self._alpha,
            #"clipon": self._clipon,
            "label": self._label,
            "zorder": self._zorder,
            "picker": self._picker
        }
        return kwargs

    @property
    def figure(self):
        if self._plot_obj is not None:
            return self._plot_obj.get_figure()

    @figure.setter
    def figure(self, figure):
        if self._plot_obj is not None:
            self._plot_obj.set_figure(figure)

    def schedule_plot_update(self):
        if self._event_handler is not None:
            self._event_handler.schedule(EventTypes.PLOT_DATA_CHANGED)

    def set_event_handler(self, event_handler):
        self._event_handler = event_handler
        
    def remove(self):
        if self._plot_obj is not None:
            self._plot_obj.remove()
            self._plot_obj = None

    def findobj(self, match = None, include_self = True):
        if self._plot_obj is not None:
            return self._plot_obj.findobj(match = match, include_self = include_self)
        raise LookupError("The Matplotlib Plot object has not been instantiated yet")

    def get_visible(self):
        return self._visible # or self._plot_object.get_visible

    def set_visible(self, visible):
        self._visible = visible
        if self._plot_obj is not None:
            self._plot_obj.set_visible(self._visible)
            self.visibleChanged.emit()

    @numpy_compatibility
    def get_alpha(self):
        return self._alpha # or self._plot_obj.get_alpha

    def set_alpha(self, alpha):
        self._alpha = alpha
        if self._plot_obj is not None:
            self._plot_obj.set_alpha(self._alpha)
            self.alphaChanged.emit()

    # def get_clipbox(self):
    #     return self._clipbox # self._plot_obj.get_clippbox from the original artist // or the clipbox property

    # def set_clipbox(self):
    #     pass

    def get_clipon(self):
        return self._clipon # or self._plot_obj.get_clip_on()

    def set_clipon(self, clipon):
        self._clipon = clipon
        if self._plot_obj is not None:
            self._plot_obj.set_clip_on(self._clipon)
            self.cliponChanged.emit()

    def get_label(self):
        return self._label # or self._plot_obj.get_label()

    def set_label(self, label):
        self._label = label
        if self._plot_obj is not None:
            self._plot_obj.set_label(self._label)
            self.labelChanged.emit()

    @numpy_compatibility
    def get_zorder(self):
        return self._zorder # or self._plot_obj.get_zorder()

    def set_zorder(self, zorder):
        self._zorder = zorder
        if self._plot_obj is not None:
            self._plot_obj.set_zorder(self._zorder)
            self.zOrderChanged.emit()

    def get_picker(self):
        return self._picker # or self._plot_obj.get_picker()

    def set_picker(self, picker):
        self._picker = picker
        if self._plot_obj is not None:
            self._plot_obj.set_picker(self._picker)
            self.pickerChanged.emit()

    visibleChanged = Signal()
    alphaChanged = Signal()
    cliponChanged = Signal()
    labelChanged = Signal()
    zOrderChanged = Signal()
    pickerChanged = Signal()

    visible = Property(bool, get_visible, set_visible)
    alpha = Property(float, get_alpha, set_alpha)
    clipon = Property(bool, get_clipon, set_clipon)
    label = Property(str, get_label, set_label)
    zOrder = Property(int, get_zorder, set_zorder)
    picker = Property(bool, get_picker, set_picker)

    
