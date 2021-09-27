import Matplotlib 1.0

MatplotlibObjectWrapper {
	id: test
	
	property var data
    property var color: 'blue'
    property string linestyle: "solid"
    property string marker: 'o'
    property string label

	onInitWrapper: {
        wrapObj('self.parent().obj.scatter([], [], marker="' + marker + '")')
        applyData()
        setColor()
        setLinestyle()
        setLabel()
        redraw()
	}
	
	onDataChanged: {
        applyData()
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

    function applyData() {
        try {
            //The scatter needs a transformed array as input - not two lists but a list of 2-Tuples.
            var xVals = data.x
            var yVals = data.y

            var vals = []
            for (var i =0; i<xVals.length; i++) {
                vals.push([xVals[i], yVals[i]])
            }

            call('self.obj.set_offsets', [vals])
        }
        catch (e) {
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

    function setLabel() {
        call('self.obj.set_label', [label])
        call('self.parent().obj.legend')
    }
}
