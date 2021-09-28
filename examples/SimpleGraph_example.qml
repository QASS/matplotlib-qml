import QtQuick 2.12
import QtQuick.Controls 2.12

import "../src" 1.0
import Matplotlib 1.0

Item {
    id: window
    objectName: "window"

    QaConnection{}
    
    SimpleGraph {
        id: graph
        objectName : "graph"
        dpi_ratio: Screen.devicePixelRatio
	    x: 600
	    y: 100
	    width: 500
	    height: 500
    }

    Component.onCompleted: {
		graph.add_plot([0, 2, 3, 4, 5], [10, 14, 30, 12, 3], {color: 'red', linestyle: 'dashed'})
		graph.add_plot([0, 2, 3, 4, 5], [10, 14, 30, 12, 3], {color: 'green', linestyle: 'dotted'})
    }
    
    property int counter: 0
    property var xVals: []
    property var yVals: []
    
    Timer {
		interval: 500; running: true; repeat: true
		onTriggered: {
            for (var i=0; i<10000; i++) {
                xVals.push(counter)
                yVals.push(counter * counter)
                counter += 1
            }
            graph.update_data(0, xVals, yVals)
		}
	}
}

