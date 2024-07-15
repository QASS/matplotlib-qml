# Figure

## Example usage
You need to call the [init](#init-slot) method after the QML objects have been instantiated in order for the Figure to create the wrapped matplotlib objects.
```qml
Figure {
	faceColor: "blue"
	rows: 1
	columns: 1
        shortTimerInterval: 20
        longTimerInterval: 100
	Component.onCompleted: init()
	// Plot etc. here
}
```

<details>
<summary>Full Example</summary>

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
					yAxisLabel: "X-Axis"
					yAxisLabelFontSize: 15
					yAxisTickColor: "white"
					yAxisLabelColor: "white"				
					Line {
						xData: [1,2,3,4,5]
						yData: [1,2,3,4,5]
						color: "orange"					
					}
				}
			}
		}
	}	
}
```

</details>

## Properties

### faceColor (String)
The `faceColor` Property modifies the color of the figure only.
The default is `"white"`.<br>
**Python methods:**

| Name				 	| Parameters	   		| Return Type	|
| --------------------- |:---------------------:|---------------|
|get_facecolor()		| -						| String		|
|set_facecolor()		| facecolor : String	| None			|


### rows (Integer)
The amount of plots in one column. The Plots will fill up a row before moving into the next row.
This is set only during the init phase of the figure and can't be modified later.
The default is `1`.


### columns (Integer)
The amount of plots in one row. The Plots will fill up a row before moving into the next row.
This is set only during the init phase of the figure and can't be modified later.
The default is `1`.


### shortTimerInterval (Integer)
The Figure updates are driven by an event system. The short timer is responsible to propagate single standalone changes but is reset anytime an event is emitted to group changes in the figure together. 
The provided value is the timer in milliseconds.
The default is `20`.<br>

**Python methods:**

| Name				 		| Parameters	   		| Return Type	|
| ------------------------- |:---------------------:|---------------|
|get_short_timer_interval()	| -						| Integer		|
|set_short_timer_interval()	| interval : Integer	| None			|

### longTimerInterval (Integer)
The long timer is the maximum time between updates in the Figure. If you constantly modify the figure it will update after one cycle of this timer.
The provided value is the timer in milliseconds.
The default is `100`.<br>
**Python methods:**

| Name				 		| Parameters	   		| Return Type	|
| ------------------------- |:---------------------:|---------------|
|get_long_timer_interval()	| -						| Integer		|
|set_long_timer_interval()	| interval : Integer	| None			|

### coordinates(QVariantList) {#coordinates}
If the property `refreshCoordiantes` is set to `true` the signal `coordinatesChanged` will be emitted. Contains a tuple of [x, y] coordinates.
**Read-Only**.<br>
**Python methods:**

| Name				 		| Parameters	   		| Return Type	|
| ------------------------- |:---------------------:|---------------|
|get_coordinates()	| -						| QVariantList|

### refreshCoordinates(Bool)
The Figure will emit the signal `coordinatesChanged` if this property is set to `true`. Check the [coordinates](#coordinates) property for more information.
The default is `false`.<br>
**Python methods:**

| Name				 		| Parameters	   		| Return Type	|
| ------------------------- |:---------------------:|---------------|
|get_refresh_coordinates()	| -						| Bool|
|set_refresh_coordinates()	| refresh: Bool	| None			|

### coordinatesRefreshRate(Integer)
Defines the interval the `coordinatesChanged` signal is emitted in milliseconds.
The default is `50`.<br>
**Python methods:**

| Name				 		| Parameters	   		| Return Type	|
| ------------------------- |:---------------------:|---------------|
|get_coordinates_refresh_rate()	| -						| Integer		|
|set_coordinates_refresh_rate()	| refresh_rate: Integer	| None			|

### constrainedLayout(Bool)
instantiates the figure with `constrainedLayout = True/False`. [Matplotlib Constrained Layout Guide](https://matplotlib.org/stable/tutorials/intermediate/constrainedlayout_guide.html). The difference to [tightLayout](#tightlayout) is that manually added objects like Colorbars (which exist on their own axes) are taken care of as well. <br>
**This is incompatibel with [tightLayout](#tightlayout).**
<br>
The default is `true`.<br>
**Python methods:**

| Name				 		| Parameters	   		| Return Type	|
| ------------------------- |:---------------------:|---------------|
|get_constrained_layout()	| -						| Bool|
|set_constrained_layout()	| constrained_layout: Bool| None			|

### zoomRectColor(String)
The color of the zoom rectangle displayed.<br>
The default is `black`.<br>
**Python methods:**

| Name				 		| Parameters	   		| Return Type	|
| ------------------------- |:---------------------:|---------------|
|get_refresh_coordinates()	| -						| Bool|
|set_refresh_coordinates()	| refresh: Bool	| None			|

### zoomRectWidth(Integer)
The linewidth of the zoom rectangle.<br>
The default is `1`.<br>
**Python methods:**

| Name				 		| Parameters	   		| Return Type	|
| ------------------------- |:---------------------:|---------------|
|get_refresh_coordinates()	| -						| Bool|
|set_refresh_coordinates()	| refresh: Bool	| None			|

### zoomRectLinestyle(String)
Linestyle of the zoom rectangle. Supported linestyles are `(dashed, dotted, solid, dash-dot, dash-dot-dot)`. The fallback is `dotted` if an invalid linestyle is used.<br>
The default is `dotted`.<br>
**Python methods:**

| Name				 		| Parameters	   		| Return Type	|
| ------------------------- |:---------------------:|---------------|
|get_refresh_coordinates()	| -						| Bool|
|set_refresh_coordinates()	| refresh: Bool	| None			|

## Slots <a name = "figure-slots">

### init() <a name = "init-slot">
This is probably the most important Slot in the whole project. This **MUST** be called whenever the Figure Component is instantiated in QML do prepare the Matplotlib objects in the background.

### tightLayout(kwargs = {}) {#tightlayout}
Check out the [Matplotlib Documentation](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.tight_layout.html) for the full documentation. With this Slot the available space for the Figure can be adjusted. This is kind of analog to using a padding on any QML object (which won't work with the Figure). The kwargs dictionary must be provided as a Javascript object.
**Example**
This will add a padding of 10% to the bottom of the figure. 
```javascript
Figure {
	faceColor: "blue"
	rows: 1
	columns: 1
	Component.onCompleted: {
		init()
		tightLayout({rect : [0, 0.1, 1, 1]})
	}
	// Plot etc. here
}
```

### subplotsAdjust(kwargs = {})
Thats basically a direct wrapper for (matplotlib.pyplot.subplots_adjust)[https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplots_adjust.html]. Make sure you provide the keyword arguments as a JS-object.

### home()
Home button functionality of the standard matplotlib Toolbar. 
**Example**
```javascript
import Matplotlib 1.0

Button {
        text: "zoom"
        width: 100
        height: 100
        onClicked: {
                fig.home()
        }
}

Figure {
        id: fig
        anchors.fill: parent
        Component.onCompleted: {
                init()
        }
        // Axis and Plots here
}
```

### back()
Back button functionality of the standard matplotlib Toolbar. Example is analog to `home()`.

### forward()
Forward button functionality of the standard matplotlib Toolbar. Example is analog to `home()`.

### pan()
Pan button functionality of the standard matplotlib Toolbar. Example is analog to `home()`.

### zoom()
Zoom button functionality of the standard matplotlib Toolbar. Example is analog to `home()`.


## Methods
The methods can be used inside of python scripts but not inside QML

### get_child(name) // get_object(name) {#get_child}
This can be used to retrieve a plot object that is a child of the figure by the `objectName` property it had during the init phase of the figure. This way you don't need to provide a full path to all of your plot objects in the python operator. The name parameter is not case sensitive.<br>
**Example**
```py
qml_connector = QmlConnectorIF()
fig = qml_connector.getObject(FIGURE_PATH)
foo_plot_obj = fig.get_child("foo")
```

