# Documentation


## Figure

### Example usage
You need to call the init method after the QML objects have been instantiated in order for the Figure to create the wrapped matplotlib objects.
```javascript
Figure {
	faceColor: "blue"
	rows: 1
	columns: 1
	Component.onCompleted: init()
	// Plot etc. here
}
```
### Properties

#### faceColor (String)
The `faceColor` Property modifies the color of the figure only.
The default is `"white"`.
**Python methods:**
| Name				 	| Parameters	   		| Return Type	|
| --------------------- |:---------------------:|---------------|
|get_facecolor()		| -						| String		|
|set_facecolor()		| facecolor : String	| None			|


#### rows (Integer)
The amount of plots in one column. The Plots will fill up a row before moving into the next row.
This is set only during the init phase of the figure and can't be modified later.
The default is `1`.


#### columns (Integer)
The amount of plots in one row. The Plots will fill up a row before moving into the next row.
This is set only during the init phase of the figure and can't be modified later.
The default is `1`.


#### tightLayout (Boolean) (DEPRECATED)
Readjust the plot and label positions in the figure to better fit the bounding box. This will soon be replaced by a Slot which allows a lot more flexibility.
The default is `false`.

#### shortTimerInterval (Integer)
The Figure updates are driven by an event system. The short timer is responsible to propagate single standalone changes but is reset anytime an event is emitted to group changes in the figure together. 
The provided value is the timer in milliseconds.
The default is `20`.
**Python methods:**
| Name				 		| Parameters	   		| Return Type	|
| ------------------------- |:---------------------:|---------------|
|get_short_timer_interval()	| -						| Integer		|
|set_short_timer_interval()	| interval : Integer	| None			|

#### longTimerInterval (Integer)
The long timer is the maximum time between updates in the Figure. If you constantly modify the figure it will update after one cycle of this timer.
The provided value is the timer in milliseconds.
The default is `100`.
**Python methods:**
| Name				 		| Parameters	   		| Return Type	|
| ------------------------- |:---------------------:|---------------|
|get_long_timer_interval()	| -						| Integer		|
|set_long_timer_interval()	| interval : Integer	| None			|

## Plot

### Example usage
The Plot is a child of the `Figure` and defines a subplot. The amount of Subplots is defined in the `rows` and `columns` Propertys of the `Figure`.
```javascript
Figure {
	faceColor: "blue"
	rows: 2
	columns: 1
	Component.onCompleted: init()
	Plot {
		faceColor: "red"
		// Axis etc. here
	}
	Plot {
		faceColor: "green"
		// Axis etc. here
	}
}
```

### Properties

#### faceColor (String)
The color of the face of each subplot in a figure (there might only be one plot on the figure).
The default is `"white"`.
**Python methods:**
| Name				 		| Parameters	   		| Return Type	|
| ------------------------- |:---------------------:|---------------|
|get_facecolor()			| -						| Integer		|
|set_facecolor()			| interval : Integer	| None			|


## Axis
If you want to get the Matplotlib Axes object from the wrapper class you can use the `get_matplotlib_ax_object` method on the `Axis` object.

### Example usage
The Axis is a child of a `Plot` and parent to all the different Plot-Objects. The `Axis` wraps around the Matplotlib `axes` object.
```javascript
Figure {
	faceColor: "blue"
	Component.onCompleted: init()
	Plot {
		faceColor: "red"
		Axis {
			// Plot Objects here
		}
	}
}
```

### Properties

#### projection (String)
The projection of the Axis. Check out Matplotlib documentation for available projections. The projection can't be changed during runtime.
The default is `"rectilinear"`.


#### polar
Currently defined but not implemented since it is a projection.


#### sharex
Currently only a placeholder to allow different multiple Axis behaviour in the future.


####  sharey
Currently only a placeholder to allow different multiple Axis behaviour in the future.


#### grid (Boolean)
Wether to draw a grid between the axis Ticks.
The default is `false`.


#### gridColor
Color of the grid.
The default is `"grey"`


* gridLinestyle
* gridLinewidth
* gridAlpha


#### xAxisLabel (String)
Defines the label on the X-Axis.
The default is `""`.
**Python methods:**
| Name				 		| Parameters	   		| Return Type	|
| ------------------------- |:---------------------:|---------------|
|get_x_axis_label()			| -						| String		|
|set_x_axis_label()			| label : String		| None			|

#### xAxisLabelFontSize (Integer)
The Point size of the X-Axis Label.
The default is `12`.
**Python methods:**
| Name				 		| Parameters	   		| Return Type	|
| ------------------------- |:---------------------:|---------------|
|get_x_axis_label_fontsize()| -						| Integer		|
|set_x_axis_label_fontsize()| fontsize : Integer	| None			|


#### xAxisTickColor (String)
Color of the Ticks on the X-Axis.
The default is `"black"`.
**Python methods:**
| Name				 		| Parameters	   		| Return Type	|
| ------------------------- |:---------------------:|---------------|
|get_x_axis_tick_color()	| -						| String		|
|set_x_axis_tick_color()	| color : String		| None			|

#### xAxisMajorTicks (List)
A list/array with positions of the major ticks on the X-Axis.
The default is `None`. `None` can't be set from QML since it is another type. Use the reset slot `reset_x_ticks()` for that.
**Python methods:**
| Name				 		| Parameters	   		| Return Type	|
| ------------------------- |:---------------------:|---------------|
|get_x_axis_major_ticks()	| -						| List/Array	|
|set_x_axis_major_ticks()	| ticks : List/Array	| None			|

#### xAxisMinorTicks (List)
A list/array with positions of the minor ticks on the X-Axis.
The default is `None`. `None` can't be set from QML since it is another type. Use the reset slot `reset_x_ticks()` for that.
**Python methods:**
| Name				 		| Parameters	   		| Return Type	|
| ------------------------- |:---------------------:|---------------|
|get_x_axis_minor_ticks()	| -						| List/Array	|
|set_x_axis_minor_ticks()	| ticks : List/Array	| None			|

#### xAxisLabelColor (String)
Color of the X-Axis Label Text.
The default is `"black"`.
**Python methods:**
| Name				 		| Parameters	   		| Return Type	|
| ------------------------- |:---------------------:|---------------|
|get_x_axis_label_color()	| -						| String		|
|set_x_axis_label_color()	| color : String		| None			|

#### yAxisLabel (String)
Defines the label on the Y-Axis.
The default is `""`.
**Python methods:**
| Name				 		| Parameters	   		| Return Type	|
| ------------------------- |:---------------------:|---------------|
|get_y_axis_label()			| -						| String		|
|set_y_axis_label()			| label : String		| None			|


#### yAxisLabelFontSize (Integer)
The Point size of the Y-Axis Label.
The default is `12`.
**Python methods:**
| Name				 		| Parameters	   		| Return Type	|
| ------------------------- |:---------------------:|---------------|
|get_y_axis_label_fontsize()| -						| Integer		|
|set_y_axis_label_fontsize()| fontsize : Integer	| None			|


#### yAxisTickColor (String)
Color of the Ticks on the Y-Axis.
The default is `"black"`.
**Python methods:**
| Name				 		| Parameters	   		| Return Type	|
| ------------------------- |:---------------------:|---------------|
|get_y_axis_tick_color()	| -						| String		|
|set_y_axis_tick_color()	| color : String		| None			|

#### yAxisMajorTicks (List)
A list/array with positions of the major ticks on the Y-Axis.
The default is `None`. `None` can't be set from QML since it is another type. Use the reset slot `reset_y_ticks()` for that.
**Python methods:**
| Name				 		| Parameters	   		| Return Type	|
| ------------------------- |:---------------------:|---------------|
|get_y_axis_major_ticks()	| -						| List/Array	|
|set_y_axis_major_ticks()	| ticks : List/Array	| None			|

#### yAxisMinorTicks (List)
A list/array with positions of the minor ticks on the Y-Axis.
The default is `None`. `None` can't be set from QML since it is another type. Use the reset slot `reset_y_ticks()` for that.
**Python methods:**
| Name				 		| Parameters	   		| Return Type	|
| ------------------------- |:---------------------:|---------------|
|get_y_axis_minor_ticks()	| -						| List/Array	|
|set_y_axis_minor_ticks()	| ticks : List/Array	| None			|

#### yAxisLabelColor (String)
Color of the Y-Axis Label Text.
The default is `"black"`.
**Python methods:**
| Name				 		| Parameters	   		| Return Type	|
| ------------------------- |:---------------------:|---------------|
|get_y_axis_label_color()	| -						| String		|
|set_y_axis_label_color()	| color : String		| None			|

#### autoscale (String) (can be "both", "x", "y", "". Overwrites axis limits)
Specifys on what dimension the axis will scale automatically. Can be either `"x"`, `"y"`, `"both"` or `""`. Turning on autoscaling will overwrite the limits of the axis in that dimension.
The default is `"both`".
**Python methods:**
| Name				 		| Parameters	   		| Return Type	|
| ------------------------- |:---------------------:|---------------|
|get_autoscale()			| -						| String		|
|set_autoscale()			| autoscale : String	| None			|

#### xMin (Float)
The lowest X-Value on the X-Axis. Internally this is handled as a list with two elements (x_min, x_max).
The default is `None`.
**Python methods:**
| Name				 		| Parameters	   		| Return Type	|
| ------------------------- |:---------------------:|---------------|
|get_xmin()					| -						| Float			|
|set_xmin()					| xmin : Float			| None			|

#### xMax
The highest X-Value on the X-Axis. Internally this is handled as a list with two elements (x_min, x_max).
The default is `None`.
**Python methods:**
| Name				 		| Parameters	   		| Return Type	|
| ------------------------- |:---------------------:|---------------|
|get_xmax()					| -						| Float			|
|set_xmax()					| xmax : Float			| None			|

#### yMin (Float)
The lowest Y-Value on the Y-Axis. Internally this is handled as a list with two elements (y_min, y_max).
The default is `None`.
**Python methods:**
| Name				 		| Parameters	   		| Return Type	|
| ------------------------- |:---------------------:|---------------|
|get_ymin()					| -						| Float			|
|set_ymin()					| ymin : Float			| None			|

#### yMax
The highest Y-Value on the Y-Axis. Internally this is handled as a list with two elements (y_min, y_max).
The default is `None`.
**Python methods:**
| Name				 		| Parameters	   		| Return Type	|
| ------------------------- |:---------------------:|---------------|
|get_ymax()					| -						| Float			|
|set_ymax()					| ymax : Float			| None			|

### Slots

#### reset() (NOT WORKING)
Removes all the Plot Objects that have been added to the axis object via Slots or Python Code. Keeps the objects defined in QML.

#### plot(x, y, kwargs = {})
Same as `ax.plot()` in Matplotlib, kwargs dictionary is optional but you do need to provide additonal keyword arguments as a dictionary or javascript-object.

#### scatter(x, y, kwargs = {})
Same as `ax.plot()` in Matplotlib but the linestyle is set to `" "` which is equivalent to no line at all, kwargs dictionary is optional but you do need to provide additonal keyword arguments as a dictionary or javascript-object.

#### hline(y, kwargs = {})
Same as `ax.axhline()` in Matplotlib, kwargs dictionary is optional but you do need to provide additonal keyword arguments as a dictionary or javascript-object.

#### vline(x, kwargs = {})
Same as `ax.axvline()` in Matplotlib, kwargs dictionary is optional but you do need to provide additonal keyword arguments as a dictionary or javascript-object.

#### hspan(y_min, y_max, kwargs = {})
Same as `ax.axhspan()` in Matplotlib, kwargs dictionary is optional but you do need to provide additonal keyword arguments as a dictionary or javascript-object.

#### vspan(x_min, x_max, kwargs = {})
Same as `ax.axvspan()` in Matplotlib, kwargs dictionary is optional but you do need to provide additonal keyword arguments as a dictionary or javascript-object.

#### tick_params(axis, kwargs)
Same as `ax.tick_params` in Matplotlib but you do need to provide keyword arguments as a dictionary or javascript-object.

#### reset_x_ticks()
Sets the major and minor ticks on the X-Axis to the `AutoLocator` object from Matplotlib. It will also set the QML Propertys `xAxisMajorTicks` and `xAxisMinorTicks` to `None` internally.

#### reset_y_ticks()
Sets the major and minor ticks on the Y-Axis to the `AutoLocator` object from Matplotlib. It will also set the QML Propertys `yAxisMajorTicks` and `yAxisMinorTicks` to `None` internally.

## Line
* linestyle
* linewidth
* label
* color
* xData
* yData
* alpha

## Scatter
* marker
* label
* color
* xData
* yData
* alpha
* markerSize
* markerEdgeWidth
* markerEdgeColor
* markerFaceColor

## HLine
* linestyle
* linewidth
* label
* color
* xData (Array with two entrys (min_x, max_x))
* yData (Array with two entrys (y, y))
* alpha
* y 
* xMin (Same as setting the xData but more intuitive)
* xMax (Same as setting the xData but more intuitive)

## VLine
* linestyle
* linewidth
* label
* color
* xData (Array with two entrys (x, x))
* yData (Array with two entrys (y_min, y_max))
* alpha
* x 
* yMin (Same as setting the yData but more intuitive)
* yMax (Same as setting the yData but more intuitive)

## HSpan
* label
* color
* xData (DO NOT USE)
* yData (DO NOT USE)
* alpha
* yMin
* yMax
* xMin
* xMax
* faceColor
* edgeColor

## VSpan
* label
* color
* xData (DO NOT USE)
* yData (DO NOT USE)
* alpha
* yMin
* yMax
* xMin
* xMax
* faceColor
* edgeColor

## Imshow
* x
* cMap
* aspect
* interpolation

## Bar
* x
* height
* width
* color
* colors
* tickLabels (might move to Axis soon)