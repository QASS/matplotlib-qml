# How to read this documentation

This documentation is structured around the available components and their hierarchy.
A [`Figure`](components/figure.md) wraps a [`Plot`](components/plot.md) which wraps an [`Axes`](components/axes.md) which 
then contains [`Artist`](base_classes/artist.md) objects.

The package follows a plugin architecture that still relies on a python inheritance tree.
This tree is very heavily inspired by the matplotlib inheritance tree to the point where you can look it up for a full picture.

The base classes like [`Artist`](base_classes/artist.md) or [`Polygon`](base_classes/polygon.md) aim to provide the same functionality as their matplotlib counterparts.
This makes adding more matplotlib types easier since this base structure is already available. It also prevents having to implement the same functionality multiple times.

The Base Classes are not meant to be instantiated and are not available in QML.
The [Components](architecture.md) are available through import `Matplotlib 1.0` in QML and you can use every property that is listed on the component and
