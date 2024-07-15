# Artist

## Inherits from (QObject)

Wrapper Klasse für [matplotlib.artist.Artist](https://matplotlib.org/stable/api/artist_api.html)


## Properties

[//]: # (--8<-- [start:artist-props])

### visible (Bool) 
Whether the object is drawn on the Axes or not
The default is `True`.<br>
**Python methods:**

| Name		 | Parameters	   	| Return Type	|
| -------------- |:------------------:|---------------|
|get_visible()	| -			| Bool|
|set_visible()	| visible : Bool| None		|

### alpha (Float) 
The opacity/transparency value of the Artist, This must be a value between 0 and 1.
The default is `None`.<br>
**Python methods:**

| Name		 | Parameters	   	| Return Type	|
| -------------- |:------------------:|---------------|
|get_alpha()	| -			| Float|
|set_alpha()	| alpha : Float| None		|

### label(String) 
The label displayed in the legend of the plot.
The default is `None`.<br>
**Python methods:**

| Name		 | Parameters	   	| Return Type	|
| -------------- |:------------------:|---------------|
|get_label()	| -			| String|
|set_label()	| label : String| None		|

### zOrder(Integer) 
Position on the z-axis of the Artist in the drawing hierarchy. Higher means further in the front.
The default is `0`.<br>
**Python methods:**

| Name		 | Parameters	   	| Return Type	|
| -------------- |:------------------:|---------------|
|get_zorder()	| -			| Integer|
|set_zorder()	| label : Integer| None		|

[//]: # (--8<-- [end:artist-props])