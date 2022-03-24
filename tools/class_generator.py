

class ClassGenerator:

	NEW_LINE = "\n"

	def __init__(self):
		self._indent = "    "

		self._paragraph_end = "\n\n"
		self._class_doc = "\"\"\" This is class has been auto generated. ABSOLUTELY PROVIDE  \"\"\""

	def generate(self, config):
		script = ""
		indentation_level = 0

		# imports
		script += "from PySide2.QtCore import QObject, Signal, Slot, Property" + self.NEW_LINE
		script += self._paragraph_end


		# class declaration
		script += f"class {config['name']}:" + self.NEW_LINE
		indentation_level += 1
		script += indentation_level * self._indent + self._class_doc
		script += self._paragraph_end
		script += indentation_level * self._indent + "def __init__(self, parent = None):" + self.NEW_LINE
		indentation_level += 1
		script += indentation_level * self._indent + "super().__init__(parent)" + self.NEW_LINE

		for prop, value in config["properties"].items():
			script += indentation_level * self._indent + "self._" + prop + " = " + str(value)
			script += "\n"

		indentation_level -= 1
		script += self._paragraph_end

		# write a getter and a setter for each property
		for prop in config["properties"].keys():
			# getter
			script += indentation_level * self._indent + f"def get_{prop}(self):" + self.NEW_LINE
			indentation_level += 1
			script += indentation_level * self._indent + "if self._plot_obj is None:" + self.NEW_LINE
			indentation_level += 1
			script += indentation_level * self._indent + f"return self._{prop}" + self.NEW_LINE
			indentation_level -= 1
			script += indentation_level * self._indent + f"return self._plot_obj.get_{prop}()" + self.NEW_LINE
			indentation_level -= 1
			script += self.NEW_LINE

			# setter
			script += indentation_level * self._indent + f"def set_{prop}(self, {prop}):" + self.NEW_LINE
			indentation_level += 1
			script += indentation_level * self._indent + f"self._{prop} = {prop}" + self.NEW_LINE
			script += indentation_level * self._indent + "if self._plot_obj is not None:" + self.NEW_LINE
			indentation_level += 1
			script += indentation_level * self._indent + f"self._plot_obj.set_{prop}(self._{prop})" + self.NEW_LINE
			script += indentation_level * self._indent + "self.schedule_plot_update()" + self.NEW_LINE
			indentation_level -= 2
			script += self.NEW_LINE

		script += self._paragraph_end

		# write the properties
		for prop in config["properties"].keys():
			script += indentation_level * self._indent + f"{prop} = Property(TYPE, get_{prop}, set_{prop})"
			script += self.NEW_LINE

		# save the script
		with open("output.py", "w+") as output_file:
			output_file.seek(0)
			output_file.truncate()
			output_file.write(script)


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