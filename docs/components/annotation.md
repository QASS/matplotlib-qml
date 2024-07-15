# Annotation

A wrapper for [matplotlib.axis.Axis.annotate](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.annotate.html).
The Annotation is used to display text in a Plot. Under the hood it's a Text object from Matplotlib. Check out the [Matplotlib Documentation](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.annotate.html) for more information.

<details>

<summary>Example</summary>

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
			Component.onCompleted: init()
			coordinatesRefreshRate: 1000
			Plot {
				Axis {
					Line {
						xData: [10,20,30]
						yData: [10,20,30]
					}
					Annotation {
						id: annotation
						text: "Hello World"
						xy: [10, 20]
						xyText: [10, 15]
						fontSize: 25
						alpha: 0.5
						color: "blue"
						arrowProps: {
							"width": 5,
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

### color (String)
Use this to set one color for the Annotation.<br>
**Python methods:**

| Name				 		| Parameters	   		| Return Type	|
| ------------------------- |:---------------------:|---------------|
|get_color()				| -						| String		|
|set_color()				| color : String		| None			|

### text (String)
This defines the displayed text. Note that Math formulars are not supported yet because it's a nightmare to translate LaTeX Code from QML to Python. It should be possible to use it from Python code however.<br>
**Python methods:**

| Name				 		| Parameters	   		| Return Type	|
| ------------------------- |:---------------------:|---------------|
|get_text()					| -						| String		|
|set_text()					| text : String			| None			|

### xy (Array/List)
The xy coordinates of the POINT that you want to annotate. This is not the position of where the text will be displayed but the position the arrow will point towards.<br>
**Python methods:**

| Name				 		| Parameters	   		| Return Type	|
| ------------------------- |:---------------------:|---------------|
|get_xy()					| -						| Array/List	|
|set_xy()					| xy : Array/List		| None			|

### xyText (Array/List)
The xy coordinates of the TEXT that you want to display.<br>
**Python methods:**

| Name				 		| Parameters	   		| Return Type	|
| ------------------------- |:---------------------:|---------------|
|get_xyText()				| -						| Array/List	|
|set_xyText()				| xyText : Array/List	| None			|

### xyCoords (String)
The coordinate system that describes how the coordinates provided shall be interpreted. Allowed types are in the [Matplotlib Documentation](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.annotate.html)
The default is `"data"`.<br>
**Python methods:**

| Name				 		| Parameters	   		| Return Type	|
| ------------------------- |:---------------------:|---------------|
|get_xycoords()				| -						| String		|
|set_xycoords()				| xycoords : String		| None			|

### fontSize (Float)
The fontSize in points. The default is `10.0`.<br>
**Python methods:**

| Name				 		| Parameters	   		| Return Type	|
| ------------------------- |:---------------------:|---------------|
|get_fontsize()				| -						| Float			|
|set_fontsize()				| fontsize : Float		| None			|

### fontStyle (String)
The font style to be used. Valid values are: ('normal', 'italic', 'oblique').
The default is `"normal"`.<br>
**Python methods:**

| Name				 		| Parameters	   		| Return Type	|
| ------------------------- |:---------------------:|---------------|
|get_fontstyle()			| -						| String		|
|set_fontstyle()			| fontstyle : String	| None			|

### fontWeight (String)
This is a value for "boldness" or how thick the text will be rendered. Valid values are: ('ultralight', 'light', 'normal', 'regular', 'book', 'medium', 'roman', 'semibold', 'demibold', 'demi', 'bold', 'heavy', 'extra bold', 'black').
The default is `"normal"`.<br>
**Python methods:**

| Name				 		| Parameters	   		| Return Type	|
| ------------------------- |:---------------------:|---------------|
|get_fontweight()			| -						| String		|
|set_fontweight()			| fontweight : String	| None			|

### fontFamily (String)
The font family of the text. Valid values are: ('serif', 'sans-serif', 'cursive', 'fantasy', 'monospace').
The default is `"serif"`.<br>
**Python methods:**

| Name				 		| Parameters	   		| Return Type	|
| ------------------------- |:---------------------:|---------------|
|get_fontfamily()			| -						| String		|
|set_fontfamily()			| fontfamily : String	| None			|

### rotation (Float)
The rotation of the text around the anchorpoint in degrees. 
The default is `0.0`.<br>
**Python methods:**

| Name				 		| Parameters	   		| Return Type	|
| ------------------------- |:---------------------:|---------------|
|get_rotation()				| -						| Float			|
|set_rotation()				| rotation : Float		| None			|
