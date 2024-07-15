## Inherits from ([PolyCollection](BaseClasses/PolyCollection))

A wrapper for [matplotlib.Axes.fill_between](https://matplotlib.org/3.5.1/api/_as_gen/matplotlib.axes.Axes.fill_between.html).

## Example

```qml
FillBetween {
	id: fb
	x: [1,2,3,4,5]
	y1: [2,3,4,5,6]
	y2: [1,1,1,2,2]
	alpha: 0.3
	where: [true, true, false, true, true]
	interpolate: true
	step: "mid"
	linewidth: 10
	linestyle: "dashed"
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

					FillBetween {
						id: fb
						x: [1,2,3,4,5]
						y1: [2,3,4,5,6]
						y2: [1,1,1,2,2]
						alpha: 0.3
						where: [true, true, false, true, true]
						interpolate: true
						step: "mid"
						linewidth: 10
						linestyle: "dashed"
					}
				}
			}
		}
	}	
}
```

</details>

## Properties


### x (Array/List) 
The points on the x axis defining the line that wraps the colored faces of the fill_between.<br>
**Note:** If you are working with Numpy arrays and you want to retrieve the from the wrapper you should use the property `FillBetween.x`. The `get_x` method converts the numpy array to a python list in order to make it usable inside QML.<br>
**Python methods:**

| Name				 		| Parameters	   		| Return Type	|
| ------------------------- |:---------------------:|---------------|
|get_x()			| -						| Array/List|
|set_x()			| x: Array/List | None			|

### y1 (Array/List) 
One of the y data curves (in total two can be used as boundaries for the fill_between)<br>
**Note:** If you are working with Numpy arrays and you want to retrieve the from the wrapper you should use the property `FillBetween.y1`. The `get_y1` method converts the numpy array to a python list in order to make it usable inside QML.<br>
**Python methods:**

| Name				 		| Parameters	   		| Return Type	|
| ------------------------- |:---------------------:|---------------|
|get_y1()			| -						| Array/List|
|set_y1()			| y1: Array/List | None			|

### y2 (Array/List) 
The second y data curve. By default this is set to zero which is equivalent to setting it to an array of all zeros which simply ends the fill_between on the x-axis. The default is `0`.<br>
**Note:** If you are working with Numpy arrays and you want to retrieve the from the wrapper you should use the property `FillBetween.y2`. The `get_y2` method converts the numpy array to a python list in order to make it usable inside QML.<br>
**Python methods:**

| Name				 		| Parameters	   		| Return Type	|
| ------------------------- |:---------------------:|---------------|
|get_y2()			| -						| Array/List|
|set_y2()			| y2: Array/List | None			|

### where (Array/List) 
A boolean Array defining which points are being used for the fill_between. Note that single points can't have a filling. The default is `None`.<br>
**Python methods:**

| Name				 		| Parameters	   		| Return Type	|
| ------------------------- |:---------------------:|---------------|
|get_where()			| -						| Array/List|
|set_where()			| where: Array/List | None			|

### interpolate (Bool) 
Check out the Matplotlib docs (link at the top). The default is `False`.<br>
**Python methods:**

| Name				 		| Parameters	   		| Return Type	|
| ------------------------- |:---------------------:|---------------|
|get_interpolate()	| -						| Bool|
|set_interpolate()	| interpolate: Bool| None			|

### step (String) 
Check out the Matplotlib docs (link at the top). The default is `None`.<br>
**Python methods:**

| Name				 		| Parameters	   		| Return Type	|
| ------------------------- |:---------------------:|---------------|
|get_step()	| -						| String|
|set_step()	| where: String| None			|

--8<-- "docs/base_classes/poly_collection.md:poly-collection-props"