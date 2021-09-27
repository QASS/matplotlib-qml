import Matplotlib 1.0

GraphPane {
    property int columns: 1
    property int rows: 1
    property var color

    onInitWrapper: {
        setColor()
    }

    onColorChanged: {
        setColor()
    }

    function setColor() {
        call('self.obj.set_facecolor', [color])
    }
}
