# HSpan

## Inherits from ([Polygon](BaseClasses/Polygon))

Wrapper for [Matplotlib.axes.Axes.axhspan](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.axhspan.html)

## Example

```qml
HSpan {
	id: hspan
	yMin: 1
	yMax: 3
	xMin: 0.2
	xMax: 0.8
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
					HSpan {
						id: hspan
						yMin: 1
						yMax: 3
						xMin: 0.2
						xMax: 0.8
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
The position of the lower border line of the span on the y-axis.The default is `0`.<br>
**Python methods:**

| Name | Parameters | Return Type |
| -------------- |:------------------:|---------------|
|get_ymin() | - | Float|
|set_ymin() | yMin : Float | None |

### yMax (Float) 
The position of the upper border line of the span on the y-axis.The default is `1`.<br>
**Python methods:**

| Name | Parameters | Return Type |
| -------------- |:------------------:|---------------|
|get_ymax() | - | Float|
|set_ymax() | yMax : Float | None |

### xMin (Float) 
Defines the position of the left side of the span object on the x-axis as a ratio of the x-axis. Thus the value needs to be 0 <= xMin < xMax <= 1.The default is `0.0`.<br>
**Python methods:**

| Name | Parameters | Return Type |
| -------------- |:------------------:|---------------|
|get_xmin() | - | Float|
|set_xmin() | xMin : Float | None |

### xMax (Float) 
Defines the position of the right side of the span object on the x-axis as a ratio of the x-axis. Thus the value needs to be 0 <= xMin < xMax <= 1.The default is `1.0`.<br>
**Python methods:**

| Name | Parameters | Return Type |
| -------------- |:------------------:|---------------|
|get_xmax() | - | Float|
|set_xmax() | xMax : Float | None |

--8<-- "docs/base_classes/polygon.md:polygon-props"