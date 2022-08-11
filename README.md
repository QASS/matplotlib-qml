# What is this project?

This project is about creating an easy to use interface to use matplotlib plots inside QML with the QML-like syntax. 

**Check out the Wiki for Documentation!**


# Installation guide

It's always advisable to create a python-virutal-environment beforehand.
```shell
py -m venv <name_of_venv>
```
Then activate the venv.
**Windows:**
```shell
venv/Scripts/activate
```

Download the latest wheel (Download Mirror will be provided soon<sup>TM</sup>). It should look like `matplotlib_bridge-<version>...`.
Install the wheel in your environment (sometimes you have to explicitly say `pip3` for Python 3.*):
```shell
pip install <path/to/wheel>
```

This should also install the required dependencies , `matplotlib`, `PySide2` and `numpy`.<br>

This project relies on the PySide2 backend which can be downloaded from here: [matplotlib_backend_pyside2](doc/README.mdhttps://git.qass.net/qml-applications/matplotlib_backend_pyside2/-/packages/34).

**Thats it.**

# Quickstart

## Analyzer4D
Coming soon<sup>TM</sup>

## For testing or using outside the Analyzer4D
In your project directory create two files `main.py` and `main.qml`.
**main.py:**
```py
import sys
from PySide2.QtGui import QGuiApplication
from PySide2.QtQml import QQmlApplicationEngine
from PySide2.QtCore import QUrl

import matplotlib_bridge
from pathlib import Path



def main():
    app = QGuiApplication(sys.argv)
    engine = QQmlApplicationEngine()

    matplotlib_bridge.init()

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

