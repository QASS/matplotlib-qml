
[![Latest Release](https://git.qass.net/qml-applications/matplotlib-bridge/-/badges/release.svg)](https://git.qass.net/qml-applications/matplotlib-bridge/-/releases) 
# Matplotlib Bridge

This project is about creating an easy to use interface to use matplotlib plots inside QML with the QML-like syntax. 

## Compatibility
Since the aim of the project is the integration in our software the wrapper is developed with the following package versions:
* matplotlib 3.3.3
* matplotlib_backend_pyside2 0.0.9 [(Download)](https://git.qass.net/qml-applications/matplotlib_backend_pyside2/-/packages)
* numpy 1.19.5
* PySide2 

## Installation guide

Since this package is just another python package you can install it in any of your host systems.

### Optimizer4D
Get the package by downloading the `.whl`-file  from the Packages & Registries Tab in this repository.<br>
Install the package on the system:
```shell
pip install --user --no-dependencies <path/to/wheel>
```
It's important to include the flag `--no-dependencies`. Otherwise pip will install the dependencies over the existing installations and break the Analyzer4D software. If that happens by mistake you can uninstall them with `pip uninstall <pacakge>` and the software should work fine again (given you used the `--user` flag.

To use the matplotlib_bridge inside the QML files you need to initialize it during the startup phase of the Analyzer4D. To achieve that you need to create a `.py` file and provide the path in the `Configuration/Preferences/Python` tab of the Analyzer4D software to the `python_init_hook` field (restart the program afterwards). 
That python file needs to include the following lines:
```py
import matplotlib_bridge

matplotlib_bridge.init()
```

### Windows
It's always advisable to create a python-virutal-environment beforehand.
```shell
py -m venv <name_of_venv>
```
Then activate the venv.

```shell
venv/Scripts/activate
```

Download the latest wheel (Download Mirror will be provided soon<sup>TM</sup>). It should look like `matplotlib_bridge-<version>...`.
Install the wheel in your environment (sometimes you have to explicitly say `pip3` for Python 3.*):
```shell
pip install <path/to/wheel>
```

### Mac/Linux
It's always advisable to create a python-virutal-environment beforehand.
```shell
python3 -m venv <name_of_venv>
```
Then activate the venv.

```shell
source venv/bin/activate
```

Download the latest wheel (Download Mirror will be provided soon<sup>TM</sup>). It should look like `matplotlib_bridge-<version>...`.
Install the wheel in your environment (sometimes you have to explicitly say `pip3` for Python 3.*):
```shell
pip3 install <path/to/wheel>
```

This should also install the required dependencies `matplotlib_backend_qtquick`, `matplotlib`, `PySide2` and `numpy`.<br>
**Thats it.**