from PySide2 import QtQml, QtCore, QtQuick

from matplotlib_backend_qtquick.backend_qtquick import NavigationToolbar2QtQuick
from matplotlib_backend_qtquick.backend_qtquickagg import FigureCanvasQtQuickAgg


QtQml.qmlRegisterType(FigureCanvasQtQuickAgg, "Matplotlib", 1, 0, "FigureCanvas")

class SimpleGraph(FigureCanvasQtQuickAgg):
	@QtCore.Slot(list, list)
	@QtCore.Slot(list, list, 'QVariantMap')
	@QtCore.Slot('QVariantList')
	@QtCore.Slot('QVariantList', 'QVariantList')
	@QtCore.Slot('QVariantList', 'QVariantList', 'QVariantMap')
	def add_plot(self, x, y, kwargs = {}):
		print(kwargs)
		l, = self.axes.plot(x, y, **kwargs)
		self.plots.append(l)
		self.figure.canvas.draw()
	
	@QtCore.Slot(int, list, list)
	@QtCore.Slot('int', 'QVariantList', 'QVariantList')
	def update_data(self, idx, x, y):
		self.plots[idx].set_xdata(x)
		self.plots[idx].set_ydata(y)
		self.axes.relim()
		self.axes.autoscale_view(True,True,True)
		self.figure.canvas.draw()
	
	def __init__(self, parent=None):
		super().__init__(None, parent)
		self.axes = self.figure.add_subplot(111)
		self.axes.set_autoscale_on(True)
		self.axes.autoscale_view(True,True,True)
		self.axes.grid(True)
		self.plots = []

QtQml.qmlRegisterType(SimpleGraph, "Matplotlib", 1, 0, "SimpleGraph")


class PyObjectWrapper(QtQuick.QQuickItem):
	initWrapper = QtCore.Signal()
	
	def __init__(self, parent=None):
		super().__init__(parent)
		self.__obj = None
	
	@QtCore.Slot(None)
	def propagate_init(self):
		self.initWrapper.emit()
		for child in self.children():
			if isinstance(child, PyObjectWrapper):
				child.propagate_init()
	
	@QtCore.Slot(None)
	def get(self):
		return self.obj
	
	@QtCore.Slot(str)
	@QtCore.Slot(str, 'QVariantList')
	@QtCore.Slot(str, 'QVariantList', 'QVariantMap')
	def call(self, func, args=[], kwargs={}):
		print('func: ', func)
		f = eval(func)
		arg_tuple = tuple(args)
		return f(*arg_tuple, **kwargs)
	
	@QtCore.Slot(str)
	def evaluate(self, cmd):
		print('cmd: ', cmd)
		return eval(cmd)
	
	@property
	def obj(self):
		return self.__obj
	
	@QtCore.Slot(str)
	def wrapObj(self, str):
		self.__obj = eval(str)
		print(self.obj)
	

QtQml.qmlRegisterType(PyObjectWrapper, "PythonBridge", 1, 0, "PyObjectWrapper")


class GraphPane(FigureCanvasQtQuickAgg):
	initWrapper = QtCore.Signal()
	
	def __init__(self, parent=None):
		super().__init__(parent)
		self.__obj = self.figure
	
	@QtCore.Slot(None)
	def propagate_init(self):
		self.initWrapper.emit()
		for child in self.children():
			if isinstance(child, PyObjectWrapper):
				child.propagate_init()
	
	@QtCore.Slot(None)
	def get(self):
		return self.obj
	
	@QtCore.Slot(str)
	@QtCore.Slot(str, 'QVariantList')
	@QtCore.Slot(str, 'QVariantList', 'QVariantMap')
	def call(self, func, args=[], kwargs={}):
		print('func: ', func)
		f = eval(func)
		arg_tuple = tuple(args)
		return f(*arg_tuple, **kwargs)
	
	@QtCore.Slot(str)
	def evaluate(self, cmd):
		print('cmd: ', cmd)
		return eval(cmd)
	
	@property
	def obj(self):
		return self.__obj
	
	@QtCore.Slot(str)
	def wrapObj(self, str):
		self.__obj = eval(str)
		print(self.obj)

QtQml.qmlRegisterType(GraphPane, "Matplotlib", 1, 0, "GraphPane")


class MatplotlibObjectWrapper(PyObjectWrapper):
	def __init__(self):
		# Initialize the Circle as a QObject so it can emit signals
		PyObjectWrapper.__init__(self)
 
	@QtCore.Slot()
	def getGraphPane(self):
		p = self.parent()
		while p is not None and not isinstance(p, GraphPane):
			p = p.parent()
		
		if isinstance(p, GraphPane):
			return p
		else:
			raise RuntimeError('The object seems to be not a child of a GraphPane!')

QtQml.qmlRegisterType(MatplotlibObjectWrapper, "Matplotlib", 1, 0, "MatplotlibObjectWrapper")


#import matplotlib.pyplot as plt

#obj1 = PyObjectWrapper()
#obj1.wrapObj('plt')

#obj2 = PyObjectWrapper(obj1)

#obj1.propagate_init()
#obj1.call('plot', [range(5), range(5)])
#obj1.call('show')
