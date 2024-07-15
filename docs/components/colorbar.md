# Colorbar

Wrapper for the [matplotlib.pyplot.colorbar](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.colorbar.html) object.

The colorbar creates a new Axes object on the existing Axis it is drawn into. This causes the figure to reposition the plots and can cause unexpected behaviour when changing some properties while using the `tightLayout` slot on the figure. Since some property-changes result in a reinstantiation of the colorbar, the whole axis is removed and then reinstantiated again if needed. This is to enable/disable the colorbar at runtime. To ensure the plot is being drawn correctly after the colorbar is removed the `tightLayout` slot is called on the figure.


## Example usage
The Colorbar QML type can be used on the property `colorbar` of the Scalarmappables `ScatterCollection` and `Imshow`

```qml
Figure {
	Layout.fillWidth: true
	Layout.fillHeight: true
	Component.onCompleted: init()
	coordinatesRefreshRate: 1000
	Plot {
		Axis {
			Imshow {
				x: [[1, 2, 3], [3, 2, 1]]
				vMin: 0
				vMax: 10
				colorbar: Colorbar {
					id: cbar
					tickColor: "white"
					tickLabelColor: "white"
					label: "Colorbar"
					orientation: "horizontal"
					fraction: 0.15
					shrink: 1.0
					aspect: 20
					drawEdges: true
					labelLocation: "center"
					labelColor: "white"
					labelFontSize: 20
				}
			}
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
				Axis {
					xAxisLabel: "X-Axis"
					xAxisLabelFontSize: 15
					xAxisTickColor: "white"
					xAxisLabelColor: "white"
					yAxisLabel: "X-Axis"
					yAxisLabelFontSize: 15
					yAxisTickColor: "white"
					yAxisLabelColor: "white"				
					Imshow {
						x: [[1,2,3], [2,3,4]]
						cMap: "gist_rainbow"
						aspect: "auto"
						extent: [0, 3, 0, 4]
						colorbar: Colorbar {
							tickColor: "white"
							tickLabelColor: "white"
							label: "Colorbar"
							orientation: "horizontal"
							fraction: 0.15
							shrink: 1.0
							aspect: 20
							drawEdges: true
							labelLocation: "center"
							labelColor: "white"
							labelFontSize: 20
						}						
					}
				}
			}
		}
	}	
}
```

</details>


## Properties


### orientation (String)
The orientation of the Colorbar can be either horizontal or vertical. In Matplotlib 3.3.3 (The version on the Analyzer) `location` and `orientation` is mutually exclusive so make sure you only set one of them! The default is `vertical`.<br>
**Python methods:**

| Name				 		| Parameters	   		| Return Type	|
| ------------------------- |:---------------------:|---------------|
|get_orientation()			| -						| String		|
|set_orientation()			| orientation : String	| None			|

### label (String)
The label of the Colorbar. The position can be adjusted with the [location](#location) property. The default is `""`.<br>
**Python methods:**

| Name				 		| Parameters	   		| Return Type	|
| ------------------------- |:---------------------:|---------------|
|get_label()				| -						| String		|
|set_label()				| label : String		| None			|

### location (String) {#location}
The position of the Colorbar relative to the plot it is used with. Note that for the orientation `horizontal` the colorbar can be only above or underneath the plot. In Matplotlib 3.3.3 (The version on the Analyzer) `location` and `orientation` is mutually exclusive so make sure you only set one of them! The default is `"right"`.<br>
**Python methods:**

| Name				 		| Parameters	   		| Return Type	|
| ------------------------- |:---------------------:|---------------|
|get_location()				| -						| String		|
|set_location()				| location : String		| None			|

### fraction (Float)
The new Axis for the Colorbar will "steal" space from the axis it is drawn next to. The fraction defines how much space of the axis the colorbar will steal for it's own axis. The default is `0.15`.<br>
**Python methods:**

| Name				 		| Parameters	   		| Return Type	|
| ------------------------- |:---------------------:|---------------|
|get_fraction()				| -						| Float			|
|set_fraction()				| fraction : Float		| None			|

### shrink (Float)
A multiplier of how much the colorbar will shrink compared to the dimension of the plot it is used with. The default is `1.0`.<br>
**Python methods:**

| Name				 		| Parameters	   		| Return Type	|
| ------------------------- |:---------------------:|---------------|
|get_shrink()				| -						| Float			|
|set_shrink()				| shrink : Float		| None			|

### aspect (Integer)
The default is `20`.<br>
**Python methods:**

| Name				 		| Parameters	   		| Return Type	|
| ------------------------- |:---------------------:|---------------|
|get_aspect()				| -						| Integer		|
|set_aspect()				| aspect : Integer		| None			|

### drawEdges (Bool)
Draws "steps" into the colorbar. The default is `False`.<br>
**Python methods:**

| Name				 		| Parameters	   		| Return Type	|
| ------------------------- |:---------------------:|---------------|
|get_drawedges()			| -						| Bool			|
|set_drawedges()			| drawEdges : Bool		| None			|

### filled (Bool)
Whether the Colorbar is filled with the color gradient. The default is `True`.<br>
**Python methods:**

| Name				 		| Parameters	   		| Return Type	|
| ------------------------- |:---------------------:|---------------|
|get_filled()				| -						| Bool			|
|set_filled()				| filled : Bool			| None			|

### tickColor(String)
The color of the ticks on the axis. The ticks will always be on the long axis (i.e. on the y-axis if location is "bottom"). 
The default is `"black"`.<br>
**Python methods:**

| Name				 		| Parameters	   		| Return Type	|
| ------------------------- |:---------------------:|---------------|
|get_tickcolor()		| -						| String		|
|set_tickcolor()		| tickColor: String| None			|

### tickLabelColor(String)
The color of the ticks marking the distances on the long axis.
The default is `"black"`.<br>
**Python methods:**

| Name				 		| Parameters	   		| Return Type	|
| ------------------------- |:---------------------:|---------------|
|get_tick_label_color()		| -						| String		|
|set_tick_label_color()		| tickLabelColor: String| None			|

### labelLocation (String)
Whether the Colorbar is filled with the color gradient. For horizontal orientation it can be (left, center, right). For vertical orientation it can be (bottom, center, top).
The default is `"center"`.<br>
**Python methods:**

| Name				 		| Parameters	   		| Return Type	|
| ------------------------- |:---------------------:|---------------|
|get_label_location()		| -						| String		|
|set_label_location()		| labelLocation : String| None			|

### labelColor(String)
The color of the label written next to the long axis.
The default is `"black"`.<br>
**Python methods:**

| Name				 		| Parameters	   		| Return Type	|
| ------------------------- |:---------------------:|---------------|
|get_label_color()		| -						| String		|
|set_label_color()		| labelColor: String| None			|

### labelFontSize(String)
The color of the label written next to the long axis.
The default is `12`.<br>
**Python methods:**

| Name				 		| Parameters	   		| Return Type	|
| ------------------------- |:---------------------:|---------------|
|get_label_fontsize()		| -						| Int|
|set_label_font_size()		| labelFontSize: Int| None			|
