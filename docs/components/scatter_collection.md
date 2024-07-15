# ScatterCollection

## Inherits from ([_CollectionWithSizes](BaseClasses/CollectionWithSizes))

Wrapper for [Matplotlib.axes.Axes.scatter](https://matplotlib.org/3.5.0/api/_as_gen/matplotlib.axes.Axes.scatter.html)

## Example

```qml
ScatterCollection {
	id: scatter
	x: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
	y: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
	c: [0.8998370014572835,
		0.8750622093628359,
		0.8713111949062655,
		0.25608204487581177,
		0.8322755484767956,
		0.807821917451281,
		0.9982243249422079,
		0.5387948606026356,
		0.7295445526316554,
		0.15979204475288822
		]	
		markerEdgeColors: ["red", "green", "red", "blue", "red", "green", "red", "green", "green", "green"]		
		marker: "H"
		linewidth: 5					
		colorbar: Colorbar {

		}
		cMap: "jet"
		vMin: -1
		vMax: 1
		hatch: "/"
		onXChanged: console.log("X CHANGED")
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

					ScatterCollection {
						id: scatter
						x: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
						y: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
						c: [0.8998370014572835,
							0.8750622093628359,
							0.8713111949062655,
							0.25608204487581177,
							0.8322755484767956,
							0.807821917451281,
							0.9982243249422079,
							0.5387948606026356,
							0.7295445526316554,
							0.15979204475288822
						]	
						markerEdgeColors: ["red", "green", "red", "blue", "red", "green", "red", "green", "green", "green"]		
						marker: "H"
						linewidth: 5					
						colorbar: Colorbar {

						}
						cMap: "jet"
						vMin: -1
						vMax: 1
						hatch: "/"
						onXChanged: console.log("X CHANGED")
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
The positions of the markers on the x-axis.<br>
**Python methods:**

| Name | Parameters | Return Type |
| -------------- |:------------------:|---------------|
|get_x() | - | Array/List|
|set_x() | x : Array/List| None |

### y (Array/List) 
The positions of the markers on the y-axis.<br>
**Python methods:**

| Name | Parameters | Return Type |
| -------------- |:------------------:|---------------|
|get_y() | - | Array/List|
|set_y() | y : Array/List| None |

### marker (String) 
The appearance of the markers. Matplotlib has a list with all available [markers](https://matplotlib.org/stable/api/markers_api.html). The default is `o`.<br>
**Python methods:**

| Name | Parameters | Return Type |
| -------------- |:------------------:|---------------|
|get_marker() | - | String|
|set_marker() | marker : String| None |

--8<-- "docs/base_classes/collection_with_sizes.md:collection-with-sizes-props"