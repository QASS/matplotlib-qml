import Matplotlib 1.0

MatplotlibObjectWrapper {
    property int plotIdx: 1
    property bool legend: true
    property string title
    property var color: parent.color

	onInitWrapper: {
        console.log('self.parent().figure.add_subplot(' + parent.rows.toString() + parent.columns.toString() + plotIdx.toString() + ')')
        wrapObj('self.parent().figure.add_subplot(' + parent.rows.toString() + parent.columns.toString() + plotIdx.toString() + ')')
//        call('self.obj.autoscale')
        setTitle()
        setColor()
	}

    onTitleChanged: {
        setTitle()
    }

    function setTitle() {
        call('self.obj.set_title', [title])
    }

    function setColor() {
        call('self.obj.set_facecolor', [color])
    }
}
