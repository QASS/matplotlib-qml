# VSpan

## Inherits from ([Polygon](BaseClasses/Polygon))

Wrapper for [Matplotlib.axes.Axes.axhspan](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.axhspan.html)

## Example

```qml
VSpan {
	id: vspan
	xMin: 1
	xMax: 3
	yMin: 0.2
	yMax: 0.8
	label: "SPANNY"
	alpha: 0.5
	facecolor: "orange"
	edgecolor: "white"
	linewidth: 4
	linestyle: "dashed"
	fill: true
	hatch: "/"
	closed: false
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
					VSpan {
						id: vspan
						xMin: 1
						xMax: 3
						yMin: 0.2
						yMax: 0.8
						label: "SPANNY"
						alpha: 0.5
						facecolor: "orange"
						edgecolor: "white"
						linewidth: 4
						linestyle: "dashed"
						fill: true
						hatch: "/"
						closed: false
					}
				}
			}
		}
	}	
}
```

</details>

## Properties

### yMin (Float) 
Defines the position of the bottom side of the span object on the x-axis as a ratio of the x-axis. Thus the value needs to be 0 <= yMin < yMax <= 1.The default is `0.0`.<br>
**Python methods:**

| Name | Parameters | Return Type |
| -------------- |:------------------:|---------------|
|get_ymin() | - | Float|
|set_ymin() | yMin : Float | None |

### yMax (Float) 
Defines the position of the upper side of the span object on the x-axis as a ratio of the x-axis. Thus the value needs to be 0 <= yMin < yMax <= 1.The default is `1.0`.<br>
**Python methods:**

| Name | Parameters | Return Type |
| -------------- |:------------------:|---------------|
|get_ymax() | - | Float|
|set_ymax() | yMax : Float | None |

### xMin (Float) 
The position of the left border line of the span on the y-axis.The default is `0`.<br>
**Python methods:**

| Name | Parameters | Return Type |
| -------------- |:------------------:|---------------|
|get_xmin() | - | Float|
|set_xmin() | xMin : Float | None |

### xMax (Float) 
The position of the right border line of the span on the y-axis.The default is `0`.<br>
**Python methods:**

| Name | Parameters | Return Type |
| -------------- |:------------------:|---------------|
|get_xmax() | - | Float|
|set_xmax() | xMax : Float | None |

--8<-- "docs/base_classes/polygon.md:polygon-props"