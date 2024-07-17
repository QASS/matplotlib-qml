# What is this project?

This project is about creating an easy to use interface to use matplotlib plots inside QML with the QML-like syntax. 

**Check out the [Documentation](https://qass.github.io/matplotlib-qml/)!**


## Installation guide

Just download from pypi:

```sh
pip install matplotlib-qml
```

or install with a terminal in the repository:

```sh
pip install -e .
```

**If your are installing this package on an [Optimizer4D](https://qass.net/optimizer4d), make sure to add the `--no-deps` flag to the installation to not overwrite the local PySide2 installation.

## Quickstart

If you want to include the bindings in your project to use matplotlib in qml you only need to add these two lines before you initialize your application:

```py
import matplotlib_qml

matplotlib_qml.init()
```

This will register all plugins for qml.

## Example app

In your project directory create two files `main.py` and `main.qml`.

**main.py:**
```py
import sys
from PySide2.QtGui import QGuiApplication
from PySide2.QtQml import QQmlApplicationEngine
from PySide2.QtCore import QUrl

import matplotlib_qml
from pathlib import Path

def main():
    app = QGuiApplication(sys.argv)
    engine = QQmlApplicationEngine()

    matplotlib_qml.init()

    qml_file = Path(__file__).parent / "main.qml"
    engine.load(QUrl.fromLocalFile(str(qml_file.resolve())))

    if not engine.rootObjects():
        sys.exit(-1)
    
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
```

**main.qml:**
```qml
import QtQuick 2.0
import QtQuick.Window 2.0
import QtQuick.Controls 2.0
import QtQuick.Layouts 1.15

import Matplotlib 1.0

Window {
    id: root
    
    width: 1500
    height: 800
    visible: true
    title: "Hello Python World!"
	
	ColumnLayout {
		anchors.fill: parent
		RowLayout {
			Button {
				text: "HOME"
				onClicked: {
					stack.itemAt(tabbar.currentIndex).home()
				}
			}
			Button {
				text: "BACK"
				onClicked: {
					stack.itemAt(tabbar.currentIndex).back()
				}
			}
			Button {
				text: "FORWARD"
				onClicked: {
					stack.itemAt(tabbar.currentIndex).forward()
				}
			}
			Button {
				text: "PAN"
				onClicked: {
					stack.itemAt(tabbar.currentIndex).pan()
				}
			}
			Button {
				text: "ZOOM"
				onClicked: {
					stack.itemAt(tabbar.currentIndex).zoom()
				}
			}
			Text {
				text: "(" + stack.itemAt(tabbar.currentIndex).coordinates[0].toString() + ", " + stack.itemAt(tabbar.currentIndex).coordinates[1].toString() + ")"
			}			
		}
	
	TabBar {
		id: tabbar
		TabButton {
			text: "1"
			width: 100
		}
		TabButton {
			text: "2"
			width: 100
		}
	}
	StackLayout {
		id: stack
		currentIndex: tabbar.currentIndex
		Figure {
			Layout.fillWidth: true
			Layout.fillHeight: true
			Component.onCompleted: init()
			coordinatesRefreshRate: 1000
			Plot {
				Axis {
					Line {
						xData: [10,20,30]
						yData: [10,20,30]
					}
				}
			}
		}
		Figure {
			Layout.fillWidth: true
			Layout.fillHeight: true
			Component.onCompleted: init()
			coordinatesRefreshRate: 1000
			Plot {
				Axis {
					xMin: 0
					xMax: 10
					yMin: 0
					yMax: 10
					autoscale: ""
					ScatterCollection {
						id: collection
						x: [1,2,3,4,5,6,7,8,9]
						y: [1,2,3,4,5,6,7,8,9]
						c: [1,2,3,4,5,6,7,8,9]
						cMap: "gist_rainbow"
						vMin: 0
						vMax: 10
						colorbar: Colorbar {
							orientation: "horizontal"
							location: "bottom"
							}
						}
					}
				}
			}
		}	
	}
}

```

