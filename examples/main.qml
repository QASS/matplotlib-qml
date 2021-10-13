import QtQuick 2.0
import QtQuick.Window 2.0
import QtQuick.Controls 2.0

import Matplotlib 1.0

Window {
    id: root
    
    width: 1000
    height: 500
    visible: true
    title: "Hello Python World!"

	
	Figure {
		id: fig
		anchors.fill: parent
		faceColor: "pink"
		rows: 2
		columns: 2

		Component.onCompleted: {
			// for (var i = 0; i < 4; i++) {
			// 	ax1.hspan(i, i + 0.5)
			// 	ax1.vspan(i, i + 0.5)
			// }
			init()
		}
		Plot {
			Axis {
				projection: "rectilinear"
				polar: true
				sharex: false
				sharey: false
				grid: true

				Line {
					id: line1
					xData: [1,2,3]
					yData: [1,2,3]
					label: "Line"
					linestyle: "dashed"
				}
			}
			Axis {
				projection: "rectilinear"
				polar: true
				sharex: false
				sharey: false
				grid: false

				Line {
					id: line2
					xData: [1,2,3]
					yData: [1,2,3]
					label: "Line"
					linestyle: "dotted"
				}
				Scatter {
					id: scatter1
					xData: [2,5,4]
					yData: [1,6,3]
					color: "red"
					label: "Scatter"
					marker: "x"
				}
			}
		}
		Plot {
			Axis {
				id: ax1
				xAxisTickColor: "green"
				xAxisLabelColor: "blue"
				xAxisLabel: "TestX"
				yAxisTickColor: "green"
				yAxisLabelColor: "blue"
				yAxisLabel: "TestY"
				grid: true
				Scatter {
					id: scatter2
					xData: [2,5,4]
					yData: [1,6,3]
					color: "green"
					alpha: 0.5
					label: "Scatter"
					marker: "^"
				}
				HSpan {
					id: hspan
					yMin: 1
					yMax: 2
					xMin: 0.5
					alpha: 0.2
					facecolor: "green"
					edgecolor: "pink"
				}
				HLine {
					id: hline
					y: 2
				}
				VLine {
					id: vline
					x: 3
				}
			}
		}
		Plot {
			Axis {
				Imshow {
					id: imshow
					x: [[1,2,3,4,5], [3,4,5,6,7], [5,4,3,2,1]]
				}
			}
		}		
	}
	Button {
		id: test
		text: "Test"
		onReleased: {
			imshow.x = [[1,8,3,7,5], [3,4,1,1,7], [5,9,3,6,1]]
			imshow.cMap = "binary"
			imshow.interpolation = "nearest"
		}
	}
	Button {
		anchors.left: test.right
		text: "RESET"
		onReleased: {
			ax1.reset()
		}
	}

}