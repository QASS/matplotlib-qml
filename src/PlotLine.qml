import Matplotlib 1.0

MatplotlibObjectWrapper {
	id: test
	
	property var data
    property var color: 'orange'
    property string linestyle: "solid"
    property bool autoScale: true
    property string marker
    property string label
	
	onInitWrapper: {
        wrapObj('self.parent().obj.plot([], [])[0]')
        applyData()
        setColor()
        setLinestyle()
        setMarker()
        setLabel()
        autoscale()
        redraw()
	}
	
	onDataChanged: {
        applyData()
        autoscale()
        redraw()
	}

    onColorChanged: {
        setColor()
        redraw()
    }

    onLinestyleChanged: {
        setLinestyle()
        redraw()
    }

    onAutoScaleChanged: {
        autoscale()
        redraw()
    }

    onMarkerChanged: {
        setMarker()
        redraw()
    }

    onLabelChanged: {
        setLabel()
        redraw()
    }

    function applyData() {
        try {
            var xVals = data.x
            var yVals = data.y

            call('self.obj.set_xdata', [xVals])
            call('self.obj.set_ydata', [yVals])
        }
        catch (e) {
        }
    }

    function autoscale() {
        if (autoScale === true) {
            call('self.parent().obj.relim')
            call('self.parent().obj.autoscale_view', [true, true, true])
        }
    }

    function redraw() {
        call('self.getGraphPane().figure.canvas.draw')
    }

    function setColor() {
        call('self.obj.set_color', [color])
    }

    function setLinestyle() {
        call('self.obj.set_linestyle', [linestyle])
    }

    function setMarker() {
        call('self.obj.set_marker', [marker])
    }

    function setLabel() {
        call('self.obj.set_label', [label])
        call('self.parent().obj.legend')
    }
}
