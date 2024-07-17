from PySide2.QtCore import Signal, Slot, Property
from matplotlib_qml.graphs_2d import Text
from matplotlib_qml.event import EventTypes, EventHandler
from matplotlib_qml.plot_objects import Axis
from matplotlib_qml.utils import numpy_compatibility



class Annotation(Text):
    """Wrapper for Matplotlib.axes.Axes.annotate
    This class utilizes it's own event handler to reinstantiate the plot object whenever the correct modification
    of the given plot object hasn't been implemented yet"""

    COORDINATE_SYSTEMS = ("figure points", "figure pixels", "figure fraction", "subfigure points",
        "subfigure pixels", "subfigure fraction", "axes points", "axes pixels", "axes fraction",
        "data", "polar")

    def __init__(self, parent=None):
        super().__init__(parent=parent)
        self._text = None
        self._xy = [0, 0] # point to annotate
        self._xytext = self._xy # point to place text
        self._xycoords = "data"
        self._arrowprops = None
        self._annotation_event_handler = EventHandler()

    def init(self, ax):
        self._create_plot_obj(ax)
        self._annotation_event_handler.register(EventTypes.PLOT_DATA_CHANGED, self.redraw)

    def _create_plot_obj(self, ax):
        if self._text is None:
            raise ValueError("Missing text Property!")
        self._plot_obj = ax.annotate(self._text, self._xy, self._xytext, self._xycoords, arrowprops = self._arrowprops, 
            **self.matplotlib_2d_kwargs)

    def redraw(self):
        if self._plot_obj is not None:
            self._plot_obj.remove()
            self._plot_obj = None
        
        axis = self.parent()
        if not isinstance(axis, Axis):
            raise LookupError("The parent needs to be an Axis wrapper object")
        self._create_plot_obj(axis.get_matplotlib_ax_object())
        self._event_handler.schedule(EventTypes.PLOT_DATA_CHANGED)

    def get_text(self):
        return self._text

    def set_text(self, text):
        self._text = text
        if self._plot_obj is not None:
            self._plot_obj.set_text(self._text)
            self.textChanged.emit()
            self._event_handler.schedule(EventTypes.PLOT_DATA_CHANGED)

    @numpy_compatibility
    def get_xy(self):
        return self._xy

    def set_xy(self, xy):
        if self._xy == self._xytext:
            self.set_xytext(xy)
        self._xy = xy
        if self._plot_obj is not None:
            self.xyChanged.emit()
            self._annotation_event_handler.schedule(EventTypes.PLOT_DATA_CHANGED)
        
    def get_xytext(self):
        return self._xy

    def set_xytext(self, xytext):
        self._xytext = xytext
        if self._plot_obj is not None:
            pass

    @numpy_compatibility
    def get_xycoords(self):
        return self._xycoords

    def set_xycoords(self, xycoords):
        if not xycoords in self.COORDINATE_SYSTEMS:
            raise ValueError("provided xycoords are not supported")
        self._xycoords = xycoords
        if self._plot_obj is not None:
            self._plot_obj.set_anncoords(self._xycoords)
            self.xyCoordsChanged.emit()
            self._event_handler.schedule(EventTypes.PLOT_DATA_CHANGED)

    def get_arrowprops(self):
        return self._arrowprops

    def set_arrowprops(self, arrowprops):
        self._arrowprops = arrowprops
        if self._plot_obj is not None:
            self.arrowPropsChanged.emit()       
            self._annotation_event_handler.schedule(EventTypes.PLOT_DATA_CHANGED)

    textChanged = Signal()
    xyChanged = Signal()
    xyTextChanged = Signal()
    xyCoordsChanged = Signal()
    arrowPropsChanged = Signal()

    text = Property(str, get_text, set_text)
    xy = Property("QVariantList", get_xy, set_xy)
    xyText = Property("QVariantList", get_xytext, set_xytext)
    xyCoords = Property(str, get_xycoords, set_xycoords)
    arrowProps = Property("QVariantMap", get_arrowprops, set_arrowprops)

def init(factory):
    factory.register(Annotation, "Matplotlib")
