# VLine

## Inherits from ([Line](Components/Line))

## Example

```qml
VLine {
	id: hLine
	linewidth: 4
	label: "SOLID"
	color: "yellow"
	alpha: 0.5
	yMin: 0.3
	yMax: 0.8
	x: 2
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

					VLine {
						id: hLine
						linewidth: 4
						label: "SOLID"
						color: "yellow"
						alpha: 0.5
						yMin: 0.3
						yMax: 0.8
						x: 2
					}
				}
			}
		}
	}	
}
```

</details>


## Properties


### x (Float) 
The Y-Coordinate to draw the Hline on.
The default is `0`.<br>
**Python methods:**
| Name				 		| Parameters	   		| Return Type	|
| ------------------------- |:---------------------:|---------------|
|get_x()					| -						| Float			|
|set_x()					| x : Float				| None			|

### yMin (Float) 
The value is given in percent like 0 <= yMin < yMax < 1. The HLine will be drawn from this margin on.
The default is `0.0`.<br>
**Python methods:**
| Name				 		| Parameters	   		| Return Type	|
| ------------------------- |:---------------------:|---------------|
|get_ymin()					| -						| Float			|
|set_ymin()					| ymin : Float			| None			|

### yMax (Float) 
The value is given in percent like 0 <= yMin < yMax < 1. The VLine will be drawn from this margin on.
The default is `1.0`.<br>
**Python methods:**
| Name				 		| Parameters	   		| Return Type	|
| ------------------------- |:---------------------:|---------------|
|get_ymax()					| -						| Float			|
|set_ymax()					| ymax : Float			| None			|

--8<-- "docs/components/line.md:line-props"