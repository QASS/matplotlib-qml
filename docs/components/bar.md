# Bar

The Bar Plot is a bit special since it is handled in a Container of Bar objects which can't be modified easily. Thats why the Bar plot object has it's own event handler to schedule a complete reinstantiation of the Bar plot whenever a property changes. This causes overhead and should be noted before use.

## Example

```qml
Bar {
	id: bar
	x: [1,2,3,4,5,6,7,8,9]
	height: [1,2,3,4,5,6,7,8,9]
	widths: [0.3, 0.5, 0.7, 0.3, 0.5, 0.7, 0.3, 0.5, 0.7]
	bottoms: [0, 1, 2, 0, 1, 2, 0, 1, 2]
	colors: ["red", "green", "blue", "red", "green", "blue", "red", "green", "blue"]
	edgecolor: "white"
	linewidth: 5
	xerr: [0.1, 0.2, 0.3, 0.1, 0.2, 0.3, 0.1, 0.2, 0.3]
	yerr: [0.1,0.2,0.3,0.1,0.2,0.3,0.1,0.2,0.3]
	ecolor: "pink"
	capsize: 3
	alpha: 0.8
	label: "bar"
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
					xMin: 0
					xMax: 10
					yMin: 0
					yMax: 10
					autoscale: ""

					Bar {
						id: bar
						x: [1,2,3,4,5,6,7,8,9]
						height: [1,2,3,4,5,6,7,8,9]
						widths: [0.3, 0.5, 0.7, 0.3, 0.5, 0.7, 0.3, 0.5, 0.7]
						bottoms: [0, 1, 2, 0, 1, 2, 0, 1, 2]
						colors: ["red", "green", "blue", "red", "green", "blue", "red", "green", "blue"]
						edgecolor: "white"
						linewidth: 5
						xerr: [0.1, 0.2, 0.3, 0.1, 0.2, 0.3, 0.1, 0.2, 0.3]
						yerr: [0.1,0.2,0.3,0.1,0.2,0.3,0.1,0.2,0.3]
						ecolor: "pink"
						capsize: 3
						alpha: 0.8
						label: "bar"
					}
				}
			}
		}
	}	
}
```

</details


## Properties 


### x (Array/List) 
The positions on the X-Axis of the different Bars.<br>
**Python methods:**

| Name				 		| Parameters	   		| Return Type	|
| ------------------------- |:---------------------:|---------------|
|get_x()					| -						| Array/List	|
|set_x()					| x : Array/List		| None			|

### height (Array/List) 
The heights of the different Bars. <br>
**Python methods:**

| Name				 		| Parameters	   		| Return Type	|
| ------------------------- |:---------------------:|---------------|
|get_height()				| -						| Array/List	|
|set_height()				| height : Array/List	| None			|

### widths (List/Array) 
A List of widths for the individual bars. This is prioritized over the `width` property. values must be 0 < width < 1.
The default is `None`.<br>
**Python methods:**

| Name				 		| Parameters	   		| Return Type	|
| ------------------------- |:---------------------:|---------------|
|get_widths()				| -						| List/Array			|
|set_widths()				| widths : List/Array		| None			|

### width (Float) 
The width of all the bars. 1 = the bars have no gap in between. values must be 0 < width < 1.
The default is `0.8`.<br>
**Python methods:**

| Name				 		| Parameters	   		| Return Type	|
| ------------------------- |:---------------------:|---------------|
|get_width()				| -						| Float			|
|set_width()				| width : Float			| None			|

### bottoms (List/Array) 
A List of values describing the position where the bars start on the y-axis. This is prioritized over the `bottom` property.
The default is `None`.<br>
**Python methods:**

| Name				 		| Parameters	   		| Return Type	|
| ------------------------- |:---------------------:|---------------|
|get_bottoms()				| -						| List/Array			|
|set_bottoms()				| bottoms : List/Array		| None			|

### bottom (Float) 
Defines where the bars start on the y-axis.
The default is `0`.<br>
**Python methods:**

| Name				 		| Parameters	   		| Return Type	|
| ------------------------- |:---------------------:|---------------|
|get_width()				| -						| Float			|
|set_width()				| width : Float			| None			|

### align (String) 
Where to position the base of the bar on the X-Axis.
The default is `center`.<br>
**Python methods:**

| Name 		| Parameters	  | Return Type	|
| ------------- |:---------------:|--------------|
|get_align()	| -		| String	|
|set_align()	| align : String  | None	|

### colors (Array/List) 
Overwrites the `color` property and gives each bar it's own color. Must have the same shape as `x` and `height`.
If you set this to an empty Array/List it will fall back to the `color` property.<br>
**Python methods:**

| Name				 		| Parameters	   		| Return Type	|
| ------------------------- |:---------------------:|---------------|
|get_colors()				| -						| Array/List	|
|set_colors()				| colors : Array/List	| None			|


### color (String) 
Use this to set one color for all of the bars.<br>
**Python methods:**

| Name				 		| Parameters	   		| Return Type	|
| ------------------------- |:---------------------:|---------------|
|get_color()				| -						| String		|
|set_color()				| color : String		| None			|

### edgecolors (Array/List) 
The border colors of the individual bar patches. This is being prioritized over `edgecolor`<br>
**Python methods:**

| Name			| Parameters	   	| Return Type	|
| --------------------- |:------------------:|---------------|
|get_edgecolors()	| -		| Array/List	|
|set_edgecolors()	| edgecolors : Array/List	| None			|


### edgecolor (String) 
Use this to set one color for all of the bars.<br>
**Python methods:**

| Name			| Parameters	   	| Return Type	|
| --------------------- |:---------------------:|---------------|
|get_edgecolor()	| -			| String	|
|set_edgecolor()	| edgecolor : String	| None		|

### linewidths (Array/List) 
The thickness of the border line for each individual bar patch. This is being prioritized over `linewidth`<br>
**Python methods:**

| Name			| Parameters	   	| Return Type	|
| --------------------- |:------------------:|---------------|
|get_linewidths()	| -		| Array/List	|
|set_linewidths()	| linewidths: Array/List	| None			|


### linewidth (Float) 
The border thickness of the bar patches. The default is: `None`.<br>
**Python methods:**

| Name			| Parameters	   	| Return Type	|
| --------------------- |:---------------------:|---------------|
|get_linewidth()	| -			| Float		|
|set_linewidth()	| linewidth : Float	| None		|

### tickLabels (Array/List) 
Modifies the ticks displayed on the x-axis for the bar plot. This will modify the ticks on the Axes object<br>
**Python methods:**

| Name			| Parameters	   	| Return Type	|
| --------------------- |:---------------------:|---------------|
|get_tick_label()	| -			| Array/List	|
|set_tick_label()	| tick_label: Array/List| None		|

### xerr (Array/List) 
The values of the error bars thats spans over the bar patch along the x-axis<br>
**Python methods:**

| Name			| Parameters	   	| Return Type	|
| --------------------- |:---------------------:|---------------|
|get_xerr()	| -			| Array/List	|
|set_xerr()	| xerr: Array/List| None		|

### yerr (Array/List) 
The values of the error bars thats spans over the bar patch along the y-axis<br>
**Python methods:**

| Name			| Parameters	   	| Return Type	|
| --------------------- |:---------------------:|---------------|
|get_yerr()	| -			| Array/List	|
|set_yerr()	| yerr: Array/List| None		|

### ecolor (Array/List) 
The color of the error bars<br>
**Python methods:**

| Name			| Parameters	   	| Return Type	|
| --------------------- |:---------------------:|---------------|
|get_ecolor()	| -			| Array/List	|
|set_ecolor()	| ecolor: Array/List| None		|

### capsize (Float) 
The length of the error bar caps in points. The default is: `None`.<br>
**Python methods:**

| Name			| Parameters	   	| Return Type	|
| --------------------- |:---------------------:|---------------|
|get_capsize()	| -			| Float		|
|set_capsize()	| capsize: Float	| None		|

### error_kw (Dictionary, Javascript Object, "QVariantMap") 
A Dictionary with keyword arguments that are passed to the error bars. Those arguments are prioritized over the other properties<br>
**Python methods:**

| Name			| Parameters	   	| Return Type	|
| --------------------- |:---------------------:|---------------|
|get_error_kw()	| -			| Dictionary|
|set_error_kw()	| error_kw: Dictionary| None		|

### alpha (Float) 
Alpha value of the bar patches. The default is: `None`.<br>
**Python methods:**

| Name			| Parameters	   	| Return Type	|
| --------------------- |:---------------------:|---------------|
|get_alpha()	| -			| Float		|
|set_alpha()	| alpha: Float	| None		|

### label (String) 
Alpha value of the bar patches. The default is: `None`.<br>
**Python methods:**

| Name			| Parameters	   	| Return Type	|
| --------------------- |:---------------------:|---------------|
|get_alpha()	| -	| String|
|set_alpha()	| alpha: String| None		|