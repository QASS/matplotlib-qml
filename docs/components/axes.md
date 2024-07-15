# Wrapper for Matplotlib.axes.Axes

If you want to get the Matplotlib Axes object from the wrapper class you can use the `get_matplotlib_ax_object` method on the `Axes` object.

Note: right now the actual class is still called Axis but will be completely renamed to Axes in a few minor releases.

## Example usage
The Axis is a child of a `Plot` and parent to all the different Plot-Objects. The `Axis` wraps around the Matplotlib `axes` object.
```qml
Figure {
	faceColor: "blue"
	Component.onCompleted: init()
	Plot {
		faceColor: "red"
		Axes {
			// Plot Objects here
		}
	}
}
```

<details>

<summary>Extended Example</summary>

```qml
import QtQuick 2.0
import QtQuick.Window 2.0
import QtQuick.Controls 2.0
import QtQuick.Layouts 1.15

import Matplotlib 1.0

Window {
    id: root
    
    width: 1500
    height: 800
    visible: true
    title: "Hello Python World!"
	
	ColumnLayout {
		anchors.fill: parent
		RowLayout {
			Button {
				text: "HOME"
				onClicked: {
					figure.home()
				}
			}
			Button {
				text: "BACK"
				onClicked: {
					figure.back()
				}
			}
			Button {
				text: "FORWARD"
				onClicked: {
					figure.forward()
				}
			}
			Button {
				text: "PAN"
				onClicked: {
					figure.pan()
				}
			}
			Button {
				text: "ZOOM"
				onClicked: {
					figure.zoom()
				}
			}
			Text {
				text: "(" + figure.coordinates[0].toString() + ", " + figure.coordinates[1].toString() + ")"
			}			
		}
		Figure {
			id: figure
			Layout.fillWidth: true
			Layout.fillHeight: true
			coordinatesRefreshRate: 1000
			faceColor: "#293133"
			Component.onCompleted: init()

			Plot {
				faceColor: "#293133"
				Axes {
					grid: true
					gridColor: "white"
					gridLinestyle: "dashed"
					gridAlpha: 0.7
					xAxisLabel: "X-Axis"
					xAxisLabelFontSize: 15
					xAxisTickColor: "white"
					xAxisLabelColor: "white"
					yAxisLabel: "X-Axis"
					yAxisLabelFontSize: 15
					yAxisTickColor: "white"
					yAxisLabelColor: "white"
					autoscale: "x"
					yMin: -1
					yMax: 30					
					Line {
						xData: [10,20,30]
						yData: [10,20,30]
						label: "QML"
					}
					Component.onCompleted: plot([15, 25], [10, 20], {label: "SLOT"})
				}
			}
		}
	}	
}
```

</details>

## Properties

### xScale (String)
The scale on the X-Axis. See [matplotlib.axes.Axes.set_xscale](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_xscale.html#matplotlib.axes.Axes.set_xscale) for more details. Kwargs are not yet supported.
The default and fallback if a provided scale is invalid is `linear`.<br>
**Python methods:**

| Name				 		| Parameters	   		| Return Type	|
| ------------------------- |:---------------------:|---------------|
|get_xscale()				| -						| String		|
|set_xscale()				| scale : String		| None			|

### yScale (String)
The scale on the Y-Axis. See [matplotlib.axes.Axes.set_xscale](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_yscale.html#matplotlib.axes.Axes.set_yscale) for more details. Kwargs are not yet supported.
The default and fallback if a provided scale is invalid is `linear`.<br>
**Python methods:**

| Name				 		| Parameters	   		| Return Type	|
| ------------------------- |:---------------------:|---------------|
|get_yscale()				| -						| String		|
|set_yscale()				| scale : String		| None			|

### projection (String)
The projection of the Axis. Check out Matplotlib documentation for available projections. The projection can't be changed during runtime.
The default is `"rectilinear"`.


### polar
Currently defined but not implemented since it is a projection.


### sharex
Currently only a placeholder to allow different multiple Axis behaviour in the future.


###  sharey
Currently only a placeholder to allow different multiple Axis behaviour in the future.


### grid (Boolean)
Wether to draw a grid between the axis Ticks.
The default is `false`.<br>
**Python methods:**

| Name				 		| Parameters	   		| Return Type	|
| ------------------------- |:---------------------:|---------------|
|get_grid()					| -						| Boolean		|
|set_grid()					| grid : Boolean		| None			|

### gridColor (String)
Color of the grid.
The default is `"grey"`.<br>
**Python methods:**

| Name				 		| Parameters	   		| Return Type	|
| ------------------------- |:---------------------:|---------------|
|get_grid_color()			| -						| String		|
|set_grid_color()			| color : String		| None			|


### gridLinestyle (String)
Linestyle of the grid
The default is `"-"`.<br>
**Python methods:**

| Name				 		| Parameters	   		| Return Type	|
| ------------------------- |:---------------------:|---------------|
|get_grid_linestyle()		| -						| String		|
|set_grid_linestyle()		| linestyle : String	| None			|

### gridLinewidth (Integer)
Linewidth of the grid.
The default is `1`.<br>
**Python methods:**

| Name				 		| Parameters	   		| Return Type	|
| ------------------------- |:---------------------:|---------------|
|get_grid_linestyle()		| -						| String		|
|set_grid_linestyle()		| linestyle : String	| None			|

### gridAlpha (Float)
The alpha value of the grid.
The default is `1.0`.<br>
**Python methods:**

| Name				 		| Parameters	   		| Return Type	|
| ------------------------- |:---------------------:|---------------|
|get_grid_alpha()			| -						| Float		|
|set_grid_alpha()			| alpha : Float			| None			|

### xAxisLabel (String)
Defines the label on the X-Axis.
The default is `""`.<br>
**Python methods:**

| Name				 		| Parameters	   		| Return Type	|
| ------------------------- |:---------------------:|---------------|
|get_x_axis_label()			| -						| String		|
|set_x_axis_label()			| label : String		| None			|

### xAxisLabelFontSize (Integer)
The Point size of the X-Axis Label.
The default is `12`.<br>
**Python methods:**

| Name				 		| Parameters	   		| Return Type	|
| ------------------------- |:---------------------:|---------------|
|get_x_axis_label_fontsize()| -						| Integer		|
|set_x_axis_label_fontsize()| fontsize : Integer	| None			|


### xAxisTickColor (String)
Color of the Ticks on the X-Axis.
The default is `"black"`.<br>
**Python methods:**

| Name				 		| Parameters	   		| Return Type	|
| ------------------------- |:---------------------:|---------------|
|get_x_axis_tick_color()	| -						| String		|
|set_x_axis_tick_color()	| color : String		| None			|

### xAxisMajorTicks (List)
A list/array with positions of the major ticks on the X-Axis.
The default is `None`. `None` can't be set from QML since it is another type. Use the reset slot `reset_x_ticks()` for that.<br>
**Python methods:**

| Name				 		| Parameters	   		| Return Type	|
| ------------------------- |:---------------------:|---------------|
|get_x_axis_major_ticks()	| -						| List/Array	|
|set_x_axis_major_ticks()	| ticks : List/Array	| None			|

### xAxisMinorTicks (List)
A list/array with positions of the minor ticks on the X-Axis.
The default is `None`. `None` can't be set from QML since it is another type. Use the reset slot `reset_x_ticks()` for that.<br>
**Python methods:**

| Name				 		| Parameters	   		| Return Type	|
| ------------------------- |:---------------------:|---------------|
|get_x_axis_minor_ticks()	| -						| List/Array	|
|set_x_axis_minor_ticks()	| ticks : List/Array	| None			|

### xAxisLabelColor (String)
Color of the X-Axis Label Text.
The default is `"black"`.<br>
**Python methods:**

| Name				 		| Parameters	   		| Return Type	|
| ------------------------- |:---------------------:|---------------|
|get_x_axis_label_color()	| -						| String		|
|set_x_axis_label_color()	| color : String		| None			|

### yAxisLabel (String)
Defines the label on the Y-Axis.
The default is `""`.<br>
**Python methods:**

| Name				 		| Parameters	   		| Return Type	|
| ------------------------- |:---------------------:|---------------|
|get_y_axis_label()			| -						| String		|
|set_y_axis_label()			| label : String		| None			|


### yAxisLabelFontSize (Integer)
The Point size of the Y-Axis Label.
The default is `12`.<br>
**Python methods:**

| Name				 		| Parameters	   		| Return Type	|
| ------------------------- |:---------------------:|---------------|
|get_y_axis_label_fontsize()| -						| Integer		|
|set_y_axis_label_fontsize()| fontsize : Integer	| None			|


### yAxisTickColor (String)
Color of the Ticks on the Y-Axis.
The default is `"black"`.<br>
**Python methods:**

| Name				 		| Parameters	   		| Return Type	|
| ------------------------- |:---------------------:|---------------|
|get_y_axis_tick_color()	| -						| String		|
|set_y_axis_tick_color()	| color : String		| None			|

### yAxisMajorTicks (List)
A list/array with positions of the major ticks on the Y-Axis.
The default is `None`. `None` can't be set from QML since it is another type. Use the reset slot `reset_y_ticks()` for that.<br>
**Python methods:**

| Name				 		| Parameters	   		| Return Type	|
| ------------------------- |:---------------------:|---------------|
|get_y_axis_major_ticks()	| -						| List/Array	|
|set_y_axis_major_ticks()	| ticks : List/Array	| None			|

### yAxisMinorTicks (List)
A list/array with positions of the minor ticks on the Y-Axis.
The default is `None`. `None` can't be set from QML since it is another type. Use the reset slot `reset_y_ticks()` for that.<br>
**Python methods:**

| Name				 		| Parameters	   		| Return Type	|
| ------------------------- |:---------------------:|---------------|
|get_y_axis_minor_ticks()	| -						| List/Array	|
|set_y_axis_minor_ticks()	| ticks : List/Array	| None			|

### yAxisLabelColor (String)
Color of the Y-Axis Label Text.
The default is `"black"`.<br>
**Python methods:**

| Name				 		| Parameters	   		| Return Type	|
| ------------------------- |:---------------------:|---------------|
|get_y_axis_label_color()	| -						| String		|
|set_y_axis_label_color()	| color : String		| None			|

### autoscale (String) (can be "both", "x", "y", "". Overwrites axis limits)
Specifys on what dimension the axis will scale automatically. Can be either `"x"`, `"y"`, `"both"` or `""`. Turning on autoscaling will overwrite the limits of the axis in that dimension.
The default is `"both`".<br>
**Python methods:**

| Name				 		| Parameters	   		| Return Type	|
| ------------------------- |:---------------------:|---------------|
|get_autoscale()			| -						| String		|
|set_autoscale()			| autoscale : String	| None			|

### xMin (Float)
The lowest X-Value on the X-Axis. Internally this is handled as a list with two elements (x_min, x_max).
The default is `None`.<br>
**Python methods:**

| Name				 		| Parameters	   		| Return Type	|
| ------------------------- |:---------------------:|---------------|
|get_xmin()					| -						| Float			|
|set_xmin()					| xmin : Float			| None			|

### xMax
The highest X-Value on the X-Axis. Internally this is handled as a list with two elements (x_min, x_max).
The default is `None`.<br>
**Python methods:**

| Name				 		| Parameters	   		| Return Type	|
| ------------------------- |:---------------------:|---------------|
|get_xmax()					| -						| Float			|
|set_xmax()					| xmax : Float			| None			|

### yMin (Float)
The lowest Y-Value on the Y-Axis. Internally this is handled as a list with two elements (y_min, y_max).
The default is `None`.<br>
**Python methods:**

| Name				 		| Parameters	   		| Return Type	|
| ------------------------- |:---------------------:|---------------|
|get_ymin()					| -						| Float			|
|set_ymin()					| ymin : Float			| None			|

### yMax
The highest Y-Value on the Y-Axis. Internally this is handled as a list with two elements (y_min, y_max).
The default is `None`.<br>
**Python methods:**

| Name				 		| Parameters	   		| Return Type	|
| ------------------------- |:---------------------:|---------------|
|get_ymax()					| -						| Float			|
|set_ymax()					| ymax : Float			| None			|

## Slots <a name="axis-slots"/>

### reset()

Removes all the Plot Objects that have been added to the axis object via Slots or Python Code. Keeps the objects defined in QML. It explicitly checks the `lines`, `containers` and ìmages` attributes of the Matplotlib Axe object and calls the `remove()` method on those which aren't defined in QML.

### plot(x, y, kwargs = {})

Same as `ax.plot()` in Matplotlib, kwargs dictionary is optional but you do need to provide additonal keyword arguments as a dictionary or javascript-object.

### scatter(x, y, kwargs = {})

Same as `ax.plot()` in Matplotlib but the linestyle is set to `" "` which is equivalent to no line at all, kwargs dictionary is optional but you do need to provide additonal keyword arguments as a dictionary or javascript-object.

### hline(y, kwargs = {})

Same as `ax.axhline()` in Matplotlib, kwargs dictionary is optional but you do need to provide additonal keyword arguments as a dictionary or javascript-object.

### vline(x, kwargs = {})

Same as `ax.axvline()` in Matplotlib, kwargs dictionary is optional but you do need to provide additonal keyword arguments as a dictionary or javascript-object.

### hspan(y_min, y_max, kwargs = {})

Same as `ax.axhspan()` in Matplotlib, kwargs dictionary is optional but you do need to provide additonal keyword arguments as a dictionary or javascript-object.

### vspan(x_min, x_max, kwargs = {})

Same as `ax.axvspan()` in Matplotlib, kwargs dictionary is optional but you do need to provide additonal keyword arguments as a dictionary or javascript-object.

### tick_params(axis, kwargs)

Same as `ax.tick_params` in Matplotlib but you do need to provide keyword arguments as a dictionary or javascript-object.

### reset_x_ticks()

Sets the major and minor ticks on the X-Axis to the `AutoLocator` object from Matplotlib. It will also set the QML Propertys `xAxisMajorTicks` and `xAxisMinorTicks` to `None` internally.

### reset_y_ticks()

Sets the major and minor ticks on the Y-Axis to the `AutoLocator` object from Matplotlib. It will also set the QML Propertys `yAxisMajorTicks` and `yAxisMinorTicks` to `None` internally.