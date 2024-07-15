# Imshow

## Inherits from ([AxesImage](BaseClasses/AxesImage))

A wrapper for the [matplotlib.axis.Axis.imshow](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.imshow.html) object.

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

### aspect (String) 
The default is `"equal"`.<br>
**Python methods:**

| Name				 		| Parameters	   		| Return Type	|
| ------------------------- |:---------------------:|---------------|
|get_aspect()					| -						| String		|
|set_aspect()					| aspect : String			| None			|

--8<-- "docs/base_classes/axes_image.md:axes-image-props"