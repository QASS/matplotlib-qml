# Plot

## Example usage
The Plot is a child of the `Figure` and defines a subplot. The amount of Subplots is defined in the `rows` and `columns` Propertys of the `Figure`.
```qml
Figure {
	faceColor: "blue"
	rows: 2
	columns: 1
	Component.onCompleted: init()
	Plot {
		faceColor: "red"
		// Axis etc. here
	}
	Plot {
		faceColor: "green"
		// Axis etc. here
	}
}
```

## Properties

### faceColor (String)

The color of the face of each subplot in a figure (there might only be one plot on the figure).
The default is `"white"`.<br>
**Python methods:**

| Name				 		| Parameters	   		| Return Type	|
| ------------------------- |:---------------------:|---------------|
|get_facecolor()			| -						| Integer		|
|set_facecolor()			| interval : Integer	| None			|