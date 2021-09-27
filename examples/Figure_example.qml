import QtQuick 2.12
import QtQuick.Controls 2.12

import "./1.0"
import Matplotlib 1.0
import "./Matplotlib"

Item {
    id: window
    objectName: "window"

    QaConnection{}

    FigureCanvas {
        objectName: "foo"
    }

    Figure {
        id: graph
        objectName : "graph"
        dpi_ratio: Screen.devicePixelRatio
        x: 0
        y: 0
        width: parent.width
        height: parent.height

        columns: 1
        rows: 2

        color: "lightgrey"
	    
	    Plot {
			id: plot
            title: 'Test'
            color: 'lightgreen'
            plotIdx: 1

			
            PlotLine {
                id: line1
                label: 'Foo'
            }

            PlotLine {
                id: line2
                color: 'green'
                label: 'bar'
            }

            PlotLine {
                id: line3
                color: 'blue'
            }

            PlotScatter {
                id: scatter
                label: 'hui'
            }
		}

        Plot {
            id: plot2

            plotIdx: 2

            PlotLine {
                id: line4
                label: 'Foo2'
            }
        }
		Component.onCompleted: {
			graph.propagate_init()
		}
    }
    
    Button {
		id: button
		text: 'Test'
		onClicked: {
            line1.data = {x: [0, 2, 4], y: [-1, 2, 3]}
            line2.data = {x: [0, 2, 5], y: [-1, 2, 3]}
            line3.data = {x: [-3, 2, 6], y: [-5, 2, 3]}
            scatter.data = {x: [-5, 5, 10], y: [-4, 2, 7]}
		}
	}
}

