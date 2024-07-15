# Line

## Inherits from ([Artist](BaseClasses/Artist))

Wrapper for the [Line2D](https://matplotlib.org/stable/api/_as_gen/matplotlib.lines.Line2D.html) object in Matplotlib.

## Example

```qml
Line {
	id: line
	xData: [1,2,3,4,5]
	yData: [1,2,3,4,5]
	markevery: 2
	drawstyle: "steps-pre"
	solidJoinstyle: "round"
	dashJoinstyle: "bevel"
	solidCapstyle: "projecting"
	dashCapstyle: "projecting"
	antialiased: true
	fillstyle: "right"
	markerfacecoloralt: "blue"
	markersize: 20
	marker: "o"
	markerfacecolor: "orange"
	markeredgecolor: "green"
	markeredgewidth: 5
	color: "pink"
	linestyle: "dashed"
	linewidth: 5
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
    objectName: "root"
    width: 1500
    height: 800
    visible: true
    title: "Hello Python World!"
	ColumnLayout {
		objectName: "rootLayout"
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
			objectName: "figure"
			Layout.fillWidth: true
			Layout.fillHeight: true
			refreshCoordinates: true
			coordinatesRefreshRate: 1000
			faceColor: "#293133"
			Component.onCompleted: init()

			Plot {
				faceColor: "#293133"
				Axis {
					grid: true
					gridAlpha: 0.7
					gridLinestyle: "dashed"
					xAxisLabel: "X-Axis"
					xAxisLabelFontSize: 15
					xAxisTickColor: "white"
					xAxisLabelColor: "white"
					yAxisLabel: "Y-Axis"
					yAxisLabelFontSize: 15
					yAxisTickColor: "white"
					yAxisLabelColor: "white"
					Line {
						id: line
						xData: [1,2,3,4,5]
						yData: [1,2,3,4,5]
						markevery: 2
						drawstyle: "steps-pre"
						solidJoinstyle: "round"
						dashJoinstyle: "bevel"
						solidCapstyle: "projecting"
						dashCapstyle: "projecting"
						antialiased: true
						fillstyle: "right"
						markerfacecoloralt: "blue"
						markersize: 20
						marker: "o"
						markerfacecolor: "orange"
						markeredgecolor: "green"
						markeredgewidth: 5
						color: "pink"
						linestyle: "dashed"
						linewidth: 5
					}
				}
			}
		}
	}	
}
```

</details>

## Properties

[//]: # (--8<-- [start:line-props])

### linestyle (String) 
The linestyle of the line object. You can call abbreviations as stated in the matplotlib documentation or "dashed", "dotted", etc..<br>
**Python methods:**

| Name				 		| Parameters	   		| Return Type	|
| ------------------------- |:---------------------:|---------------|
|get_linestyle()			| -						| String		|
|set_linestyle()			| linestyle : String	| None			|

### linewidth (Integer) 
The linewidth or thickness of the line object. You can call abbreviations as stated in the matplotlib documentation or "dashed", "dotted", etc..<br>
**Python methods:**

| Name				 		| Parameters	   		| Return Type	|
| ------------------------- |:---------------------:|---------------|
|get_linewidth()			| -						| Integer		|
|set_linewidth()			| linewidth : Integer	| None			|

### color (String) 
Color of the line object. You can use the colors from the Matplotlib documentation.<br>
**Python methods:**

| Name				 		| Parameters	   		| Return Type	|
| ------------------------- |:---------------------:|---------------|
|get_color()				| -						| String		|
|set_color()				| color : String		| None			|

### marker (String) 
The appearance of the markers. Matplotlib has a list with all available [markers](https://matplotlib.org/stable/api/markers_api.html). The default is `None`.  
**Python methods:**

| Name | Parameters | Return Type |
|------|:----------:|-------------|
| get_marker() | - | String |
| set_marker() | marker : String | None |

### markerSize (Float) 
A list containing the sizes for each individual object in the collection. The default is `0`.  
**Python methods:**

| Name | Parameters | Return Type |
|------|:----------:|-------------|
| get_markersize() | - | Float |
| set_markersize() | markerSize : Float | None |

### markerEdgeWidth (Float) {#markeredgewidth}
Markers can have a border which can be colored differently to the face of the marker. This property adjusts the thickness of the border of a marker. The default is `20`. <br>
**Python methods:**

| Name | Parameters | Return Type |
|------|:----------:|-------------|
| get_markeredgewidth() | - | Float |
| set_markeredgewidth() | markerEdgeWidth : Float | None |

### markerEdgeColor (String) 
The color of the border of the markers. Note that a [markerEdgeWidth](#markeredgewidth) must be set in order for this to be visible. The default is the facecolor of the marker. <br>
**Python methods:**

| Name | Parameters | Return Type |
|------|:----------:|-------------|
| get_markeredgecolor() | - | String|
| set_markeredgecolor() | markerEdgeColor : String | None |

### markerFaceColorAlt (String) 
If a [fillstyle](#fillstyle) other than `full` is set then this is the second color the face of the marker is filled with. By default this is the same as the facecolor.<br>
**Python methods:**

| Name | Parameters | Return Type |
|------|:----------:|-------------|
| get_markerfacecoloralt() | - | String|
| set_markerfacecoloralt() | markerFaceColorAlt : String | None |


### fillstyle (String) {#fillstyle}
How to fill the face of the marker. Can be one of `{'full', 'left', 'right', 'bottom', 'top', 'none'}`. The default is `None` which is the same as `full`.<br>
**Python methods:**

| Name | Parameters | Return Type |
|------|:----------:|-------------|
| get_fillstyle() | - | String|
| set_fillstyle() | fillstyle: String | None |

### antialiased (Bool) 
Whether to apply antialiasing on the Line. The default is `None` which is the same as `None`.<br>
**Python methods:**

| Name | Parameters | Return Type |
|------|:----------:|-------------|
| get_antialiased() | - | Bool|
| set_antialiased() | antialiased: Bool| None |

### dashCapstyle (String) 
How the corners of a dashed Line look. Can be one of `{'miter', 'round', 'bevel'}`. The default is `None`.<br>
**Python methods:**

| Name | Parameters | Return Type |
|------|:----------:|-------------|
| get_dash_capstyle() | - | String|
| set_dash_capstyle() | dashCapstyle : String | None |

### solidCapstyle (String) 
How the corners of a solid Line look. Can be one of ` {'butt', 'projecting', 'round'}`. The default is `None`.<br>
**Python methods:**

| Name | Parameters | Return Type |
|------|:----------:|-------------|
| get_solid_capstyle() | - | String|
| set_solid_capstyle() | solidCapstyle : String | None |

### dashJoinstyle (String) 
How the corners of a dashed Line look. Can be one of ` {'butt', 'projecting', 'round'}`. The default is `None`.<br>
**Python methods:**

| Name | Parameters | Return Type |
|------|:----------:|-------------|
| get_dash_joinstyle() | - | String|
| set_dash_joinstyle() | dashJoinstyle : String | None |

### solidJoinstyle (String) 
How the corners of a solid Line look. Can be one of ` {'butt', 'projecting', 'round'}`. The default is `None`.<br>
**Python methods:**

| Name | Parameters | Return Type |
|------|:----------:|-------------|
| get_solid_joinstyle() | - | String|
| set_solid_joinstyle() | solidJoinstyle : String | None |

### drawstyle (String) 
The Line can be drawn with different style settings. For example does the `steps` drawstyle draw steps (90° angles) between two data points whereas the `default` drawstyle interpolate the data points with a straight line. Can be one of `{'default', 'steps', 'steps-pre', 'steps-mid', 'steps-post'}`. The default is `default`.<br>
**Python methods:**

| Name | Parameters | Return Type |
|------|:----------:|-------------|
| get_drawstyle() | - | String|
| set_drawstyle() | drawstyle : String | None |

### markevery (Integer) 
When a marker is defined mark every x data point with a marker. The default is `1`.<br>
**Python methods:**

| Name | Parameters | Return Type |
|------|:----------:|-------------|
| get_markevery() | - | Integer|
| set_markevery() | markevery : Integer| None |

### xData (Array/List)
Marks the points on the X-Axis that are related to the points of the same index in the Array in `yData`.
If `xData` and `yData` have different shapes or length there won't be an error if you set that in QML but there will be an error if you set it in Python. Make sure to update them right after another. 
In Python you can use numpy arrays but since QML can't interpret those they will be converted to a list whenever `get_xdata()` is used by the interface. If you want to retrieve the numpy array you did put in use the property `xdata` for retrieving it.<br>
**Python property/method:**

| Name				 		| Parameters	   		| Return Type	|
| ------------------------- |:---------------------:|---------------|
|xdata(property not method!)| -						| Array/List	|
|set_xdata()				| xdata : Array/List	| None			|

### yData (Array/List)
Marks the points on the Y-Axis that are related to the points of the same index in the Array in `xData`.
If `xData` and `yData` have different shapes or length there won't be an error if you set that in QML but there will be an error if you set it in Python. Make sure to update them right after another. 
In Python you can use numpy arrays but since QML can't interpret those they will be converted to a list whenever `get_ydata()` is used by the interface.If you want to retrieve the numpy array you did put in use the property `ydata` for retrieving it.<br>
**Python property/method:**

| Name				 		| Parameters	   		| Return Type	|
| ------------------------- |:---------------------:|---------------|
|ydata(property not method!)| -						| Array/List	|
|set_ydata()				| xdata : Array/List	| None			|

[//]: # (--8<-- [end:line-props])