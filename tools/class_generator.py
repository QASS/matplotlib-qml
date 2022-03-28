

class ClassGenerator:

	NEW_LINE = "\n"

	def __init__(self):
		self._script = ""
		self._indent = "    "
		self._indentation_level = 0

		self._paragraph_end = "\n\n"
		self._class_doc = "\"\"\" This is class has been auto generated. PLEASE PROVIDE DOCUMENTATION!!! \"\"\""

	def _get_current_indent(self):
		"""Returns the current indentation as spaces or tab-string"""
		return self._indentation_level * self._indent

	def add_function(self, name, params, *lines):
		"""
		
		:param name: name of the function
		:param params: a tuple with parameter names
		:param lines: all the contents of the function body
		"""
		self._script += self._get_current_indent() + f"def {name}({', '.join(params)}):" + self.NEW_LINE
		self._indentation_level += 1
		for line in lines:
			self._script += self._get_current_indent() + line + self.NEW_LINE
		self._script += self.NEW_LINE
		self._indentation_level -= 1

	def generate(self, config):
		# script = ""
		# indentation_level = 0

		# imports
		self._script += "from PySide2.QtCore import QObject, Signal, Slot, Property" + self.NEW_LINE
		self._script += self._paragraph_end


		# class declaration
		self._script += f"class {config['name']}:" + self.NEW_LINE
		self._indentation_level += 1
		self._script += self._indentation_level * self._indent + self._class_doc
		self._script += self._paragraph_end

		lines = ["super().__init__(parent)"]
		for prop, value in config["properties"].items():
			lines.append("self._" + prop + " = " + str(value))
		self.add_function("__init__", ("self", "parent = None"), *lines)

		# write a getter and a setter for each property
		for prop in config["properties"].keys():
			# getter
			lines = (
				"if self._plot_obj is None:",
				self._indent + f"return self._{prop}",
				f"return self._plot_obj.get_{prop}()"
			)
			self.add_function(f"get_{prop}", ("self",), *lines)

			# setter
			lines = (
				f"self._{prop} = {prop}",
				"if self._plot_obj is not None:",
				self._indent + f"self._plot_obj.set_{prop}(self._{prop})",
				self._indent + "self.schedule_plot_update()"
			)
			self.add_function(f"set_{prop}", ("self", prop), *lines)

		# write the properties
		for prop in config["properties"].keys():
			self._script += self._indentation_level * self._indent + f"{prop} = Property(TYPE, get_{prop}, set_{prop})"
			self._script += self.NEW_LINE

	
	def save(self, filename = "output.py"):
		"""Save the script to a file in the same directory 
		WILL OVERWRITE EXISTING FILES
		"""
		with open(filename, "w+") as output_file:
			output_file.seek(0)
			output_file.truncate()
			output_file.write(self._script)


if __name__ == "__main__":

	config = {
		"name": "HLine",
		"properties": {
			"y": 0,
			"xmin": 0.0,
			"xmax": 1.0
		}
	}

	class_generator = ClassGenerator()
	class_generator.generate(config)
	class_generator.save()