# Documentation


## Figure

### Example usage
You need to call the init method after the QML objects have been instantiated in order for the Figure to create the wrapped matplotlib objects.
```javascript
Figure {
	faceColor: "blue"
	rows: 1
	columns: 1
	Component.onCompleted: init()
	// Axis etc. here
}
```
### Properties

#### faceColor (String)
The `faceColor` Property modifies the color of the figure only.
The default is `"white"`.

### rows (Integer)
The amount of plots in one column. The Plots will fill up a row before moving into the next row.
The default is `1`.


### columns (Integer)
The amount of plots in one row. The Plots will fill up a row before moving into the next row.
The default is `1`.


### tightLayout (Boolean) (DEPRECATED)
Readjust the plot and label positions in the figure to better fit the bounding box. This will soon be replaced by a Slot which allows a lot more flexibility.
The default is `false`.

### shortTimerInterval (Integer)
The Figure updates are driven by an event system. The short timer is responsible to propagate single standalone changes but is reset anytime an event is emitted to group changes in the figure together. 
The provided value is the timer in milliseconds.
The default is `20`.

### longTimerInterval (Integer)
The long timer is the maximum time between updates in the Figure. If you constantly modify the figure it will update after one cycle of this timer.
The provided value is the timer in milliseconds.
The default is `100`.

## Plot
* faceColor

## Axis
* projection
* polar
* sharex
* sharey
* grid
* xAxisLabel
* xAxisLabelFontSize
* xAxisTickColor
* xAxisLabelColor
* yAxisLabel
* yAxisLabelFontSize
* yAxisTickColor
* yAxisLabelColor
* gridColor
* gridLinestyle
* gridLinewidth
* gridAlpha
* autoscale (can be "both", "x", "y", "". Overwrites axis limits)
* xMin
* xMax
* yMin
* yMax


## Line
* linestyle
* linewidth
* label
* color
* xData
* yData
* alpha

## Scatter
* marker
* label
* color
* xData
* yData
* alpha
* markerSize
* markerEdgeWidth
* markerEdgeColor
* markerFaceColor

## HLine
* linestyle
* linewidth
* label
* color
* xData (Array with two entrys (min_x, max_x))
* yData (Array with two entrys (y, y))
* alpha
* y 
* xMin (Same as setting the xData but more intuitive)
* xMax (Same as setting the xData but more intuitive)

## VLine
* linestyle
* linewidth
* label
* color
* xData (Array with two entrys (x, x))
* yData (Array with two entrys (y_min, y_max))
* alpha
* x 
* yMin (Same as setting the yData but more intuitive)
* yMax (Same as setting the yData but more intuitive)

## HSpan
* label
* color
* xData (DO NOT USE)
* yData (DO NOT USE)
* alpha
* yMin
* yMax
* xMin
* xMax
* faceColor
* edgeColor

## VSpan
* label
* color
* xData (DO NOT USE)
* yData (DO NOT USE)
* alpha
* yMin
* yMax
* xMin
* xMax
* faceColor
* edgeColor

## Imshow
* x
* cMap
* aspect
* interpolation

## Bar
* x
* height
* width
* color
* colors
* tickLabels (might move to Axis soon)