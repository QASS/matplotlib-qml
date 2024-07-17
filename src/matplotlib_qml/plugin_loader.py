import importlib
import os
from typing import List, Callable
from matplotlib_qml import factory


def import_module(module_name: str):
	return importlib.import_module(module_name)

def get_plugins():
	"""Searches for the plugin folder in the same directory and returns a list
	of all python file names without the file endings
	
	
	:return: A list of all the modules
	:rtype: List[str]
	"""
	modules = []
	curr_file_path = os.path.dirname(os.path.abspath(__file__))
	for module in os.listdir(curr_file_path + "/plugins"):
		if module.startswith("__") or ".py" not in module:
			continue
		# append to module list and strip file ending
		modules.append("matplotlib_qml.plugins." + module[:-3])
	return modules

def load_plugins(plugins: List[str]):
	"""Receives a list of plugins to load with the importlib module. 
	The loader will call the init function of each module and provide the factory to let
	the modules register themselves. Existing modules will be overwritten (name conflicts)
	
	:param plugins: A list of module names
	:type plugins: List[str]

	"""
	for plugin_name in plugins:
		plugin = import_module(plugin_name)
		plugin.init(factory)
