# ScalarMappable

## Wrapper for [Matplotlib.cm.ScalarMappable](https://matplotlib.org/3.5.0/api/cm_api.html)


## Properties

[//]: # (--8<-- [start:scalar-mappable-props])

### cMap (String) 
The colormap of the ScalarMappable. Can b one of the [Matplotlib Colormaps](https://matplotlib.org/3.5.1/tutorials/colors/colormaps.html).
The default is `viridis`.<br>
**Python methods:**

| Name | Parameters | Return Type |
| -------------- |:------------------:|---------------|
|get_cmap() | - | String|
|set_cmap() | x : String | None |

### vMin (Float) 
The minimum value of of the colorscale for the colormap. By default the minimum of the data is used.
The default is `None`.<br>
**Python methods:**

| Name | Parameters | Return Type |
| -------------- |:------------------:|---------------|
|get_vmin() | - | String|
|set_vmin() | x : String | None |

### vMax (Float) 
The maximum value of of the colorscale for the colormap. By default the maximum of the data is used.
The default is `None`.<br>
**Python methods:**

| Name | Parameters | Return Type |
| -------------- |:------------------:|---------------|
|get_vmax() | - | String|
|set_vmax() | x : String | None |

### colorbar (Colorbar) 
A Colorbar Component.
The default is `None`.<br>
**Python methods:**

| Name | Parameters | Return Type |
| -------------- |:------------------:|---------------|
|get_colorbar() | - | Colorbar|
|set_colorbar() | colorbar : Colorbar| None |

[//]: # (--8<-- [end:scalar-mappable-props])