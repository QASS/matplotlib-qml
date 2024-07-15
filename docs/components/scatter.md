# Scatter

## Inherits from [Line2D](./line.md)

The Scatter QML Type is implemented as a `matplotlib.Line2D` object without a line-style to achieve better performance during plot updates. Scatters are by default a PathCollection which makes it hard to update them efficiently. Thus it is not possible to provide different markerSizes (Array-Like). If you want to have that functionality, use the [ScatterCollection]().

## Properties 


### label (String)
The label of the scatter object, if there are no labels on an axis, the legend won't be displayed.<br>
**Python methods:**

| Name				 		| Parameters	   		| Return Type	|
| ------------------------- |:---------------------:|---------------|
|get_label()				| -						| String		|
|set_label()				| label : String		| None			|	

### color (String)
Color of the scatter object. You can use the colors from the Matplotlib documentation.<br>
**Python methods:**

| Name				 		| Parameters	   		| Return Type	|
| ------------------------- |:---------------------:|---------------|
|get_color()				| -						| String		|
|set_color()				| color : String		| None			|

### xData (Array/List)
Marks the points on the X-Axis that are related to the points of the same index in the Array in `yData`.
If `xData` and `yData` have different shapes or length there won't be an error if you set that in QML but there will be an error if you set it in Python. Make sure to update them right after another. 
In Python you can use numpy arrays but since QML can't interpret those they will be converted to a list whenever `get_xdata()` is used by the interface. If you want to retrieve the original numpy array you put in, use the property `xdata`.<br>
**Python methods:**

| Name				 		| Parameters	   		| Return Type	|
| ------------------------- |:---------------------:|---------------|
|xdata(property not method!)| -						| Array/List	|
|set_xdata()				| xdata : Array/List	| None			|

### yData (Array/List)
Marks the points on the Y-Axis that are related to the points of the same index in the Array in `xData`.
If `xData` and `yData` have different shapes or length there won't be an error if you set that in QML but there will be an error if you set it in Python. Make sure to update them right after another. 
In Python you can use numpy arrays but since QML can't interpret those they will be converted to a list whenever `get_ydata()` is used by the interface. If you want to retrieve the original numpy array you put in, use the property `ydata`.<br>
**Python methods:**

| Name				 		| Parameters	   		| Return Type	|
| ------------------------- |:---------------------:|---------------|
|ydata(property not method!)| -						| Array/List	|
|set_ydata()				| xdata : Array/List	| None			|

### alpha (Float)
The transparency of the scatter points on the plot. 0.0 is transparent and 1.0 is fully visible.<br>
**Python methods:**

| Name				 		| Parameters	   		| Return Type	|
| ------------------------- |:---------------------:|---------------|
|get_alpha()				| -						| Float			|
|set_alpha()				| alpha : Float			| None			|

### marker (String)
The marker Property defines the appearance of the Scatter markers. Check out the [Matplotlib-markers](https://matplotlib.org/stable/api/markers_api.html) documentation for the available markers.
The transparency of the line on the plot. 0.0 is transparent and 1.0 is fully visible.
The default is `"o"`.<br>
**Python methods:**

| Name				 		| Parameters	   		| Return Type	|
| ------------------------- |:---------------------:|---------------|
|get_marker()				| -						| String		|
|set_marker()				| marker : String		| None			|

### markerSize (Float)
Sets the size of all of the markers in that object.
The default is `None` which means it falls back to mthe matplotlib default.<br>
**Python methods:**

| Name				 		| Parameters	   		| Return Type	|
| ------------------------- |:---------------------:|---------------|
|get_markersize()			| -						| Float			|
|set_markersize()			| markersize : Float	| None			|

### markerEdgeWidth (float)
Modifies the outer border thickness of the markers. 
The default is `None` which means it falls back to mthe matplotlib default.<br>
**Python methods:**

| Name				 		| Parameters	   		| Return Type	|
| ------------------------- |:---------------------:|---------------|
|get_markeredgewidth()		| -						| Float			|
|set_markeredgewidth()		| width : Float			| None			|

### markerEdgeColor (String)
Sets the color of the marker borders.
The default is `None` which means it falls back to mthe matplotlib default.<br>
**Python methods:**

| Name				 		| Parameters	   		| Return Type	|
| ------------------------- |:---------------------:|---------------|
|get_markeredgecolor()		| -						| String		|
|set_markeredgecolor()		| color : String		| None			|

### markerFaceColor (String)
Sets the color of the marker face.
The default is `None` which means it falls back to mthe matplotlib default.<br>
**Python methods:**

| Name				 		| Parameters	   		| Return Type	|
| ------------------------- |:---------------------:|---------------|
|get_markerfacecolor()		| -						| String		|
|set_markerfacecolor()		| color : String		| None			|

