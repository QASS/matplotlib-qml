import numpy as np



def numpy_compatibility(func):
	"""Decorator to convert numpy return types to python data types so that they can be used in the QML environment"""
	def inner(*args, **kwargs):
		result = func(*args, **kwargs)
		if isinstance(result, np.ndarray):
			result = result.tolist()
		elif isinstance(result, np.floating):
			result = float(result)
		elif isinstance(result, np.integer):
			result = float(result)
		elif isinstance(result, np.character):
			result = str(result)
		return result
	return inner