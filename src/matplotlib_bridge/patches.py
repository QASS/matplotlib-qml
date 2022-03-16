from matplotlib.patches import Polygon

from matplotlib_bridge.artist import Artist


class Patch(Artist): # TODO SPAN
	def __init__(self, parent=None):
		super().__init__(parent)
		self._antialiased = None

	def get_antialiased(self):
		if self._plot_obj is None:
			return self._antialiased
		self._plot_obj.get_antialiased()

	def set_antialiased(self, antialiased):
		self._antialiased = antialiased
		if self._plot_obj is not None:
			self._plot_obj.set_antialiased(self._antialiased)
			self.schedule_plot_update()