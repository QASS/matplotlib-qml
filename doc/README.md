# Documentation

## Table of Content
1. [Figure](#figure)
   * [Properties](#figure-properties)
   * [Slots](#figure-slots)
2. [Plot](#plot)
   * [Properties](#plot-properties)
3. [Axis](#axis)
   * [Properties](#axis-properties)
   * [Slots](#axis-slots)
4. [Line](#line)
   * [Properties](#line-properties)
5. [Scatter](#scatter)
   * [Properties](#scatter-properties)
6. [HLine](#hline)
   * [Properties](#hline-properties)
7. [VLine](#vline)
   * [Properties](#vline-properties)
10. [Imshow](#imshow)
   * [Properties](#imshow-properties)
11. [Bar](#bar)
   * [Properties](#bar-properties)

## Figure

### Example usage
You need to call the [init](#init-slot) method after the QML objects have been instantiated in order for the Figure to create the wrapped matplotlib objects.
```javascript
Figure {
	faceColor: "blue"
	rows: 1
	columns: 1
	Component.onCompleted: init()
	// Plot etc. here
}
```
### Properties <a name="figure-properties"/>

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

### Slots <a name = "figure-slots">

#### init() <a name = "init-slot">
This is probably the most important Slot in the whole project. This **MUST** be called whenever the Figure Component is instantiated in QML do prepare the Matplotlib objects in the background.

#### tightLayout(kwargs = {})
Check out the [Matplotlib Documentation](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.tight_layout.html) for the full documentation. With this Slot the available space for the Figure can be adjusted. This is kind of analog to using a padding on any QML object (which won't work with the Figure). The kwargs dictionary must be provided as a Javascript object.
**Example**
This will add a padding of 10% to the bottom of the figure. 
```javascript
Figure {
	faceColor: "blue"
	rows: 1
	columns: 1
	Component.onCompleted: {
		init()
		tightLayout({rect : [0, 0.1, 1, 1]})
	}
	// Plot etc. here
}
```

### home()
Home button functionality of the standard matplotlib Toolbar. 
**Example**
```javascript
import Matplotlib 1.0

Button {
        text: "zoom"
        width: 100
        height: 100
        onClicked: {
                fig.home()
        }
}

Figure {
        id: fig
        anchors.fill: parent
        Component.onCompleted: {
                init()
        }
        // Axis and Plots here
}
```

### back()
Back button functionality of the standard matplotlib Toolbar. Example is analog to `home()`.

### forward()
Forward button functionality of the standard matplotlib Toolbar. Example is analog to `home()`.

### pan()
Pan button functionality of the standard matplotlib Toolbar. Example is analog to `home()`.

### zoom()
Zoom button functionality of the standard matplotlib Toolbar. Example is analog to `home()`.


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

### Properties <a name="plot-properties"/>

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

### Properties <a name="axis-properties"/>

#### xScale (String)
The scale on the X-Axis. See [matplotlib.axes.Axes.set_xscale](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_xscale.html#matplotlib.axes.Axes.set_xscale) for more details. Kwargs are not yet supported.
The default and fallback if a provided scale is invalid is `linear`.
**Python methods:**
| Name				 		| Parameters	   		| Return Type	|
| ------------------------- |:---------------------:|---------------|
|get_xscale()				| -						| String		|
|set_xscale()				| scale : String		| None			|

#### yScale (String)
The scale on the Y-Axis. See [matplotlib.axes.Axes.set_xscale](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_yscale.html#matplotlib.axes.Axes.set_yscale) for more details. Kwargs are not yet supported.
The default and fallback if a provided scale is invalid is `linear`.
**Python methods:**
| Name				 		| Parameters	   		| Return Type	|
| ------------------------- |:---------------------:|---------------|
|get_yscale()				| -						| String		|
|set_yscale()				| scale : String		| None			|

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
**Python methods:**
| Name				 		| Parameters	   		| Return Type	|
| ------------------------- |:---------------------:|---------------|
|get_grid()					| -						| Boolean		|
|set_grid()					| grid : Boolean		| None			|

#### gridColor (String)
Color of the grid.
The default is `"grey"`
**Python methods:**
| Name				 		| Parameters	   		| Return Type	|
| ------------------------- |:---------------------:|---------------|
|get_grid_color()			| -						| String		|
|set_grid_color()			| color : String		| None			|


#### gridLinestyle (String)
Linestyle of the grid
The default is `"-"`.
**Python methods:**
| Name				 		| Parameters	   		| Return Type	|
| ------------------------- |:---------------------:|---------------|
|get_grid_linestyle()		| -						| String		|
|set_grid_linestyle()		| linestyle : String	| None			|

#### gridLinewidth (Integer)
Linewidth of the grid.
The default is `1`.
**Python methods:**
| Name				 		| Parameters	   		| Return Type	|
| ------------------------- |:---------------------:|---------------|
|get_grid_linestyle()		| -						| String		|
|set_grid_linestyle()		| linestyle : String	| None			|

#### gridAlpha (Float)
The alpha value of the grid.
The default is `1.0`.
**Python methods:**
| Name				 		| Parameters	   		| Return Type	|
| ------------------------- |:---------------------:|---------------|
|get_grid_alpha()			| -						| Float		|
|set_grid_alpha()			| alpha : Float			| None			|

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

### Slots <a name="axis-slots"/>

#### reset()
Removes all the Plot Objects that have been added to the axis object via Slots or Python Code. Keeps the objects defined in QML. It explicitly checks the `lines`, `containers` and ìmages` attributes of the Matplotlib Axe object and calls the `remove()` method on those which aren't defined in QML.

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

### Properties <a name="line-properties"/>

#### linestyle (String)
The linestyle of the line object. You can call abbreviations as stated in the matplotlib documentation or "dashed", "dotted", etc..
**Python methods:**
| Name				 		| Parameters	   		| Return Type	|
| ------------------------- |:---------------------:|---------------|
|get_linestyle()			| -						| String		|
|set_linestyle()			| linestyle : String	| None			|


#### linewidth (Integer)
The linewidth or thickness of the line object. You can call abbreviations as stated in the matplotlib documentation or "dashed", "dotted", etc..
**Python methods:**
| Name				 		| Parameters	   		| Return Type	|
| ------------------------- |:---------------------:|---------------|
|get_linewidth()			| -						| Integer		|
|set_linewidth()			| linewidth : Integer	| None			|

#### label (String)
The label of the line object, if there are no labels on an axis, the legend won't be displayed
**Python methods:**
| Name				 		| Parameters	   		| Return Type	|
| ------------------------- |:---------------------:|---------------|
|get_label()				| -						| String		|
|set_label()				| label : String		| None			|


#### color (String)
Color of the line object. You can use the colors from the Matplotlib documentation.
**Python methods:**
| Name				 		| Parameters	   		| Return Type	|
| ------------------------- |:---------------------:|---------------|
|get_color()				| -						| String		|
|set_color()				| color : String		| None			|

#### xData (Array/List)
Marks the points on the X-Axis that are related to the points of the same index in the Array in `yData`.
If `xData` and `yData` have different shapes or length there won't be an error if you set that in QML but there will be an error if you set it in Python. Make sure to update them right after another. 
In Python you can use numpy arrays but since QML can't interpret those they will be converted to a list whenever `get_xdata()` is used by the interface.
**Python property/method:**
| Name				 		| Parameters	   		| Return Type	|
| ------------------------- |:---------------------:|---------------|
|xdata(property not method!)| -						| Array/List	|
|set_xdata()				| xdata : Array/List	| None			|

#### yData (Array/List)
Marks the points on the Y-Axis that are related to the points of the same index in the Array in `xData`.
If `xData` and `yData` have different shapes or length there won't be an error if you set that in QML but there will be an error if you set it in Python. Make sure to update them right after another. 
In Python you can use numpy arrays but since QML can't interpret those they will be converted to a list whenever `get_ydata()` is used by the interface.
**Python property/method:**
| Name				 		| Parameters	   		| Return Type	|
| ------------------------- |:---------------------:|---------------|
|ydata(property not method!)| -						| Array/List	|
|set_ydata()				| xdata : Array/List	| None			|

#### alpha (Float)
The transparency of the line on the plot. 0.0 is transparent and 1.0 is fully visible.
**Python methods:**
| Name				 		| Parameters	   		| Return Type	|
| ------------------------- |:---------------------:|---------------|
|get_alpha()				| -						| Float			|
|set_alpha()				| alpha : Float			| None			|

The properties **marker, markerSize, markerEdgeWidth, markerEdgeColor, markerFaceColor** are analogues to the ones in [Scatter](#scatter-properties)


## Scatter
The Scatter QML Type is implemented as a `matplotlib.Line2D` object without a line-style to achieve better performance during plot updates. Scatters are by default a PathCollection which makes it hard to update them efficiently. Thus it is not possible to provide different markerSizes (Array-Like).

### Properties <a name="scatter-properties"/>

#### label (String)
The label of the scatter object, if there are no labels on an axis, the legend won't be displayed
**Python methods:**
| Name				 		| Parameters	   		| Return Type	|
| ------------------------- |:---------------------:|---------------|
|get_label()				| -						| String		|
|set_label()				| label : String		| None			|	

#### color (String)
Color of the scatter object. You can use the colors from the Matplotlib documentation.
**Python methods:**
| Name				 		| Parameters	   		| Return Type	|
| ------------------------- |:---------------------:|---------------|
|get_color()				| -						| String		|
|set_color()				| color : String		| None			|

#### xData (Array/List)
Marks the points on the X-Axis that are related to the points of the same index in the Array in `yData`.
If `xData` and `yData` have different shapes or length there won't be an error if you set that in QML but there will be an error if you set it in Python. Make sure to update them right after another. 
In Python you can use numpy arrays but since QML can't interpret those they will be converted to a list whenever `get_xdata()` is used by the interface.
**Python methods:**
| Name				 		| Parameters	   		| Return Type	|
| ------------------------- |:---------------------:|---------------|
|xdata(property not method!)| -						| Array/List	|
|set_xdata()				| xdata : Array/List	| None			|

#### yData (Array/List)
Marks the points on the Y-Axis that are related to the points of the same index in the Array in `xData`.
If `xData` and `yData` have different shapes or length there won't be an error if you set that in QML but there will be an error if you set it in Python. Make sure to update them right after another. 
In Python you can use numpy arrays but since QML can't interpret those they will be converted to a list whenever `get_ydata()` is used by the interface.
**Python methods:**
| Name				 		| Parameters	   		| Return Type	|
| ------------------------- |:---------------------:|---------------|
|ydata(property not method!)| -						| Array/List	|
|set_ydata()				| xdata : Array/List	| None			|

#### alpha (Float)
The transparency of the scatter points on the plot. 0.0 is transparent and 1.0 is fully visible.
**Python methods:**
| Name				 		| Parameters	   		| Return Type	|
| ------------------------- |:---------------------:|---------------|
|get_alpha()				| -						| Float			|
|set_alpha()				| alpha : Float			| None			|

#### marker (String)
The marker Property defines the appearance of the Scatter markers. Check out the [Matplotlib-markers](https://matplotlib.org/stable/api/markers_api.html) documentation for the available markers.
The transparency of the line on the plot. 0.0 is transparent and 1.0 is fully visible.
The default is `"o"`.
**Python methods:**
| Name				 		| Parameters	   		| Return Type	|
| ------------------------- |:---------------------:|---------------|
|get_marker()				| -						| String		|
|set_marker()				| marker : String		| None			|

#### markerSize (Float)
Sets the size of all of the markers in that object.
The default is `None` which means it falls back to mthe matplotlib default.
**Python methods:**
| Name				 		| Parameters	   		| Return Type	|
| ------------------------- |:---------------------:|---------------|
|get_markersize()			| -						| Float			|
|set_markersize()			| markersize : Float	| None			|

#### markerEdgeWidth (float)
Modifies the outer border thickness of the markers. 
The default is `None` which means it falls back to mthe matplotlib default.
**Python methods:**
| Name				 		| Parameters	   		| Return Type	|
| ------------------------- |:---------------------:|---------------|
|get_markeredgewidth()		| -						| Float			|
|set_markeredgewidth()		| width : Float			| None			|

#### markerEdgeColor (String)
Sets the color of the marker borders.
The default is `None` which means it falls back to mthe matplotlib default.
**Python methods:**
| Name				 		| Parameters	   		| Return Type	|
| ------------------------- |:---------------------:|---------------|
|get_markeredgecolor()		| -						| String		|
|set_markeredgecolor()		| color : String		| None			|

#### markerFaceColor (String)
Sets the color of the marker face.
The default is `None` which means it falls back to mthe matplotlib default.
**Python methods:**
| Name				 		| Parameters	   		| Return Type	|
| ------------------------- |:---------------------:|---------------|
|get_markerfacecolor()		| -						| String		|
|set_markerfacecolor()		| color : String		| None			|


## HLine
Draws a horizontal Line on the plot.

### Properties <a name="hline-properties"/>

#### linestyle (String)
The linestyle of the hline object. You can call abbreviations as stated in the matplotlib documentation or "dashed", "dotted", etc..
**Python methods:**
| Name				 		| Parameters	   		| Return Type	|
| ------------------------- |:---------------------:|---------------|
|get_linestyle()			| -						| String		|
|set_linestyle()			| linestyle : String	| None			|


#### linewidth (Integer)
The linewidth or thickness of the hline object. You can call abbreviations as stated in the matplotlib documentation or "dashed", "dotted", etc..
**Python methods:**
| Name				 		| Parameters	   		| Return Type	|
| ------------------------- |:---------------------:|---------------|
|get_linewidth()			| -						| Integer		|
|set_linewidth()			| linewidth : Integer	| None			|

#### label (String)
The label of the hline object, if there are no labels on an axis, the legend won't be displayed
**Python methods:**
| Name				 		| Parameters	   		| Return Type	|
| ------------------------- |:---------------------:|---------------|
|get_label()				| -						| String		|
|set_label()				| label : String		| None			|


#### color (String)
Color of the hline object. You can use the colors from the Matplotlib documentation.
**Python methods:**
| Name				 		| Parameters	   		| Return Type	|
| ------------------------- |:---------------------:|---------------|
|get_color()				| -						| String		|
|set_color()				| color : String		| None			|

#### alpha (Float)
The transparency of the hline on the plot. 0.0 is transparent and 1.0 is fully visible.
The default is `1.0`.
**Python methods:**
| Name				 		| Parameters	   		| Return Type	|
| ------------------------- |:---------------------:|---------------|
|get_alpha()				| -						| Float			|
|set_alpha()				| alpha : Float			| None			|

#### y (Float)
The Y-Coordinate to draw the Hline on.
The default is `0`.
**Python methods:**
| Name				 		| Parameters	   		| Return Type	|
| ------------------------- |:---------------------:|---------------|
|get_y()					| -						| Float			|
|set_y()					| y : Float				| None			|

#### xMin (Float)
The value is given in percent like 0 <= xMin < xMax < 1. The HLine will be drawn from this margin on.
The default is `0.0`.
**Python methods:**
| Name				 		| Parameters	   		| Return Type	|
| ------------------------- |:---------------------:|---------------|
|get_xmin()					| -						| Float			|
|set_xmin()					| xmin : Float			| None			|

#### xMax (Float)
The value is given in percent like 0 <= xMin < xMax < 1. The HLine will be drawn from this margin on.
The default is `1.0`.
**Python methods:**
| Name				 		| Parameters	   		| Return Type	|
| ------------------------- |:---------------------:|---------------|
|get_xmax()					| -						| Float			|
|set_xmax()					| xmax : Float			| None			|

The properties **marker, markerSize, markerEdgeWidth, markerEdgeColor, markerFaceColor** are analogues to the ones in [Scatter](#scatter-properties)

## VLine

### Properties <a name="vline-properties"/>

#### linestyle (String)
The linestyle of the vline object. You can call abbreviations as stated in the matplotlib documentation or "dashed", "dotted", etc..
**Python methods:**
| Name				 		| Parameters	   		| Return Type	|
| ------------------------- |:---------------------:|---------------|
|get_linestyle()			| -						| String		|
|set_linestyle()			| linestyle : String	| None			|


#### linewidth (Integer)
The linewidth or thickness of the vline object. You can call abbreviations as stated in the matplotlib documentation or "dashed", "dotted", etc..
**Python methods:**
| Name				 		| Parameters	   		| Return Type	|
| ------------------------- |:---------------------:|---------------|
|get_linewidth()			| -						| Integer		|
|set_linewidth()			| linewidth : Integer	| None			|

#### label (String)
The label of the vline object, if there are no labels on an axis, the legend won't be displayed
**Python methods:**
| Name				 		| Parameters	   		| Return Type	|
| ------------------------- |:---------------------:|---------------|
|get_label()				| -						| String		|
|set_label()				| label : String		| None			|


#### color (String)
Color of the vline object. You can use the colors from the Matplotlib documentation.
**Python methods:**
| Name				 		| Parameters	   		| Return Type	|
| ------------------------- |:---------------------:|---------------|
|get_color()				| -						| String		|
|set_color()				| color : String		| None			|

#### alpha (Float)
The transparency of the vline on the plot. 0.0 is transparent and 1.0 is fully visible.
The default is `1.0`.
**Python methods:**
| Name				 		| Parameters	   		| Return Type	|
| ------------------------- |:---------------------:|---------------|
|get_alpha()				| -						| Float			|
|set_alpha()				| alpha : Float			| None			|

#### x (Float)
The Y-Coordinate to draw the Hline on.
The default is `0`.
**Python methods:**
| Name				 		| Parameters	   		| Return Type	|
| ------------------------- |:---------------------:|---------------|
|get_x()					| -						| Float			|
|set_x()					| x : Float				| None			|

#### yMin (Float)
The value is given in percent like 0 <= yMin < yMax < 1. The HLine will be drawn from this margin on.
The default is `0.0`.
**Python methods:**
| Name				 		| Parameters	   		| Return Type	|
| ------------------------- |:---------------------:|---------------|
|get_ymin()					| -						| Float			|
|set_ymin()					| ymin : Float			| None			|

#### yMax (Float)
The value is given in percent like 0 <= yMin < yMax < 1. The VLine will be drawn from this margin on.
The default is `1.0`.
**Python methods:**
| Name				 		| Parameters	   		| Return Type	|
| ------------------------- |:---------------------:|---------------|
|get_ymax()					| -						| Float			|
|set_ymax()					| ymax : Float			| None			|

The properties **marker, markerSize, markerEdgeWidth, markerEdgeColor, markerFaceColor** are analogues to the ones in [Scatter](#scatter-properties)

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

### Properties <a name="imshow-properties"/>

#### x (Array/List)
A 2D Array/List describing the data.
The default is `[]`.
**Python methods:**
| Name				 		| Parameters	   		| Return Type	|
| ------------------------- |:---------------------:|---------------|
|get_x()					| -						| Array/List	|
|set_x()					| x : Array/List		| None			|

#### cMap (String)
The color Map for the Imshow. Those have a lot of variance in colors/contrast. Check out [Matplotlib-CMaps](https://matplotlib.org/stable/tutorials/colors/colormaps.html) for the available types.
The default is `"viridis"`.
**Python methods:**
| Name				 		| Parameters	   		| Return Type	|
| ------------------------- |:---------------------:|---------------|
|get_cmap()					| -						| String		|
|set_cmap()					| cmap : String			| None			|

#### aspect (String)
The default is `"equal"`.
**Python methods:**
| Name				 		| Parameters	   		| Return Type	|
| ------------------------- |:---------------------:|---------------|
|get_cmap()					| -						| String		|
|set_cmap()					| cmap : String			| None			|

#### interpolation (String)
The default is `"antialiased"`.
**Python methods:**
| Name				 		| Parameters	   		| Return Type	|
| ------------------------- |:---------------------:|---------------|
|get_interpolation()		| -						| String		|
|set_interpolation()		| interpolation : String| None			|

#### vMin (Float)
If the imshow is not normalized this is used as the lower Boundary value for the color spectrum. The default is `None`.
**Python methods:**
| Name				 		| Parameters	   		| Return Type	|
| ------------------------- |:---------------------:|---------------|
|get_vmin()					| -						| Float			|
|set_vmin()					| vmin : Float			| None			|

#### vMax (Float)
If the imshow is not normalized this is used as the upper Boundary value for the color spectrum. The default is `None`.
**Python methods:**
| Name				 		| Parameters	   		| Return Type	|
| ------------------------- |:---------------------:|---------------|
|get_vmax()					| -						| Float			|
|set_vmax()					| vmin : Float			| None			|

#### extent (List/Tuple)
Describes the bounding box the data is stretched to fill the image.
The default is `None`.
**Python methods:**
| Name				 		| Parameters	   		| Return Type	|
| ------------------------- |:---------------------:|---------------|
|get_extent()				| -						| List/Tuple	|
|set_extent()				| extent : List/Tuple	| None			|

## Bar
The Bar Plot is a bit special since it is handled in a Container of Bar objects which can't be modified easily. Thats why the Bar plot object has it's own event handler to schedule a complete reinstantiation of the Bar plot. This causes overhead and should be noted before use.

### Properties <a name="bar-properties"/>

#### x (Array/List)
The positions on the X-Axis of the different Bars.
**Python methods:**
| Name				 		| Parameters	   		| Return Type	|
| ------------------------- |:---------------------:|---------------|
|get_x()					| -						| Array/List	|
|set_x()					| x : Array/List		| None			|

#### height (Array/List)
The heights of the different Bars. 
**Python methods:**
| Name				 		| Parameters	   		| Return Type	|
| ------------------------- |:---------------------:|---------------|
|get_height()				| -						| Array/List	|
|set_height()				| height : Array/List	| None			|

#### width (Float)
The width of all the bars. 1 = the bars have no gap in between. values must be 0 < width < 1.
The default is `0.8`.
**Python methods:**
| Name				 		| Parameters	   		| Return Type	|
| ------------------------- |:---------------------:|---------------|
|get_width()				| -						| Float			|
|set_width()				| width : Float			| None			|

#### color (String)
Use this to set one color for all of the bars.
**Python methods:**
| Name				 		| Parameters	   		| Return Type	|
| ------------------------- |:---------------------:|---------------|
|get_color()				| -						| String		|
|set_color()				| color : String		| None			|

#### colors (Array/List)
Overwrites the `color` property and gives each bar it's own color. Must have the same shape as `x` and `height`.
If you set this to an empty Array/List it will fall back to the `color` property.
**Python methods:**
| Name				 		| Parameters	   		| Return Type	|
| ------------------------- |:---------------------:|---------------|
|get_colors()				| -						| Array/List	|
|set_colors()				| colors : Array/List	| None			|


* tickLabels (might move to Axis soon)