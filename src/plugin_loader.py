import importlib
import os
from typing import List, Callable
import factory


def import_module(module_name: str):
	return importlib.import_module(module_name)

def get_plugins():
	"""Searches for the plugin folder in the same directory and returns a list
	of all python file names without the file endings
	
	
	:return: A list of all the modules
	:rtype: List[str]
	"""
	modules = []
	for module in os.listdir("./plugins"):
		if module.startswith("__") or ".py" not in module:
			continue
		# append to module list and strip file ending
		modules.append("plugins." + module[:-3])
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

if __name__ == "__main__":
	print(get_plugins())