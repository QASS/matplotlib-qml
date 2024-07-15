# AxesImage

## Inherits from ([_ImageBase](./image_base.md))
Wrapper for [Matplotlib.image.AxesImage](https://matplotlib.org/stable/api/image_api.html)

## Properties

[//]: # (--8<-- [start:axes-image-props])

### extent (List/Tuple) 
Describes the bounding box the data is stretched to fill the image. The behaviour is similar to using the `xMin`, `xMax`, `yMin`, `yMax` properties on the Axis but this won't stretch the image to the desired coordinates.
The List or Tuple typically looks like this:
```js
extent: [x_min, x_max, y_min, y_max]
```
Note that you can only use tuples over the python interface and not in QML.
The default is `None`.<br>
**Python methods:**

| Name				 		| Parameters	   		| Return Type	|
| ------------------------- |:---------------------:|---------------|
|get_extent()				| -						| List/Tuple	|
|set_extent()				| extent : List/Tuple	| None			|

--8<-- "docs/base_classes/image_base.md:image-base-props"

[//]: # (--8<-- [end:axes-image-props])