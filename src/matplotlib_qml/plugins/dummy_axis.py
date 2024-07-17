from matplotlib_qml.plot_objects import Axis
from PySide2.QtCore import Signal, Slot, Property


class DummyAxis(Axis):
    """This Axis object is meant to only apply the QML Properties once during initialization"""

    def __init__(self, parent=None):
        super().__init__(parent=parent)

    def init(self, ax, event_handler):
        """Iterate over every children and call the plot method on those children
        The children define how they are plotted and are provided with an axis object
        they can modify. The QML children will be plotted first.
        
        :param ax: A Matplotlib axis object
        :type ax: Matplotlib.pyplot.Axes
        """
        self._event_handler = event_handler
        self._ax = ax
        # plot all children
        self._init_children(ax, event_handler)
        # apply all the axis settings
        self._apply_axis_settings()

def init(factory):
    factory.register(DummyAxis, "Matplotlib")
