# ToDos

- [x] implement possible QML Interface from Python
- [x] implement plugin architecture for new components
- [x] enable redrawing on every property change in the plt object tree (EventHandler)
- [x] implement JS interface to achieve the same behaviour (as in Matplotlib)
- [ ] test if it is possible to generate the same behaviour

## Axes Functions from Matplotlib implemented
### Basic
- [x] Axes.plot (QML / JS)
- [ ] Axes.errorbar
- [x] Axes.scatter (QML / JS) (intern als Axes.plot ohne linestyle)
- [ ] Axes.plot_date
- [ ] Axes.step
- [ ] Axes.loglog
- [ ] Axes.semilogx
- [ ] Axes.semilogy
- [ ] Axes.fill_between
- [ ] Axes.fill_betweenx
- [ ] Axes.bar
- [ ] Axes.barh
- [ ] Axes.bar_label
- [ ] Axes.stem
- [ ] Axes.eventplot
- [ ] Axes.pie
- [ ] Axes.stackplot
- [ ] Axes.broken_barh
- [ ] Axes.vlines
- [ ] Axes.hlines
- [ ] Axes.fill

### Spans
- [x] Axes.axhline (QML / JS)
- [x] Axes.axhspan (QML / JS)
- [x] Axes.axvline (QML / JS)
- [x] Axes.axvspan (QML / JS)
- [x] Axes.axline (QML / JS)

### Spectral
- [ ] Axes.acorr
- [ ] Axes.angle_spectrum
- [ ] Axes.cohere
- [ ] Axes.csd
- [ ] Axes.magnitude_spectrum
- [ ] Axes.phase_spectrum
- [ ] Axes.psd
- [ ] Axes.specgram
- [ ] Axes.xcorr

### Statistics
- [ ] Axes.boxplot
- [ ] Axes.violinplot
- [ ] Axes.violin
- [ ] Axes.bxp

### Binned
- [ ] Axes.hexbin
- [ ] Axes.hist
- [ ] Axes.hist2d
- [ ] Axes.stairs

### Contours
- [ ] Axes.clabel
- [ ] Axes.contour
- [ ] Axes.contourf

### 2D Arrays
- [x] Axes.imshow (QML)
- [ ] Axes.matshow
- [ ] Axes.pcolor
- [ ] Axes.pcolorfast
- [ ] Axes.pcolormesh
- [ ] Axes.spy

### Unstructured Triangles
- [ ] Axes.tripcolor
- [ ] Axes.triplot
- [ ] Axes.tricontour
- [ ] Axes.tricontourf

### Text and Annotations
- [ ] Axes.annotate
- [ ] Axes.text
- [ ] Axes.table
- [ ] Axes.arrow
- [ ] Axes.inset_axes
- [ ] Axes.indicate_inset
- [ ] Axes.indicate_inset_zoom
- [ ] Axes.secondary_xaxis
- [ ] Axes.secondary_yaxis

### Vector fields
- [ ] Axes.barbs
- [ ] Axes.quiver
- [ ] Axes.quiverkey
- [ ] Axes.streamplot

### Clearing
- [ ] Axes.cla
- [x] Axes.clear (JS "reset")

### Appearance
- [ ] Axes.axis
- [ ] Axes.set_axis_off
- [ ] Axes.set_axis_on
- [ ] Axes.set_frame_on
- [ ] Axes.get_frame_on
- [ ] Axes.set_axisbelow
- [ ] Axes.get_axisbelow
- [x] Axes.grid (QML)
- [x] Axes.get_facecolor (QML)
- [x] Axes.set_facecolor (QML)

### Labels, Titles, Legend
- [x] Axes.set_xlabel (QML)
- [x] Axes.get_xlabel (QML)
- [x] Axes.set_ylabel (QML)
- [x] Axes.get_ylabel (QML)
- [ ] Axes.set_title
- [ ] Axes.get_title
- [x] Axes.legend (passiert automatisch)
- [ ] Axes.get_legend
- [ ] Axes.get_legend_handles_labels





# How to use

create venv for python
```
python -m venv <name_of_venv>
```
activate venv
```
<name_of_venv>/Scripts/activate
```
install `requirements.txt`
```
pip install -r requirements.txt
```

Now run:
```
py main.py
```

# How to write a plugin

On application start the `plugin_loader` will attempt to load all modules in the `/plugins/` directory. Each modules needs to implement a `init` function that registers the plugin to the program. The init function receives a `factory` as an argument which mus receive the `class` and the QML module name to register the class in:
```python
class MyClass(LineObject2D):
	# Code here

def init(factory):
	factory.register(MyClass, "QMLModuleName")
```

The factory register function allows to set the following arguments:
| Argument		  | Value	   		| Required      | Description 						   	|
| --------------- |:---------------:|:-------------:|--------------------------------------:|
| class_reference | Class      		| True          | reference to the class definition		|
| QMLModuleName	  | String      	| True          | The Module name in QML (for imports)	|
| version		  | Int      		| False         | Main version number (default = 1)		|
| subversion	  | Int      		| False         | Subversion number (default = 0)		|
| QMLComponentName| String     		| False         | Component name in QML default = \_\_name\_\_ From the Python class		|

In QML the component is then used like:
```
import QMLModuleName 1.0

MyClass {

}
```

The Plugin Class must implement the methods `init`. It might also want to inherit one of the base classes like `LineObject2D`, `PlotObject2D` or `GraphObject2D` which already provide propertys for 2D Plots.
Each object inheriting from `PlotObject2D` (so far I will most likely change that to a lower tier class) will receive an Event Handler from the axes which is handed down from the figure. You can use this Event Handler to emit Events whenever the data lying in the plot object changes. Available Events can be found in the `EventTypes` class which contains all the constants.