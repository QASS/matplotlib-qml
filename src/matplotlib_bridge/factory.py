from PySide2.QtQml import qmlRegisterType

module_items = dict()

def register(class_reference, qml_module_name: str, version = 1,
            subversion = 0, qml_component_name = None):
    """Registers a provided class reference in the QML Components. If Components with the same
    qml_component_name are registered the duplicate will be overwritten.

    :param class_reference: A reference to the class (not an object)
    :type class_reference: class
    :param qml_module_name: The module name that will be used as an import in QML
    :type qml_module_name: str
    :param version: The main version (in 1.0 this would be the "1")
    :type version: int, optional
    :param subversion: The subversion (in 1.0 this would be the "0")
    :type subversion: int, optional
    :param qml_component_name: The name of the QML component. By default this will be the __name__ of the class_reference
    :type qml_component_name: string, optional
    """
    if qml_component_name is None:
        qml_component_name = class_reference.__name__
    plugin = {
        "class" : class_reference,
        "qml_module_name" : qml_module_name,
        "version" : version,
        "subversion" : subversion,
    }
    module_items[qml_component_name] = plugin

def unregister(qml_component_name: str):
    """Unregister a QML component by providing it's QML identifier. Registering n existing
    qml_component_name will overwrite the old component.

    :param qml_component_name: The name of the component in QML (default is __name__ of the class_reference)
    :type qml_component_name: string
    """
    module_items.pop(qml_component_name, None)

def register_at_qml(module_items):
    """Registers all the Components that have been registered internally in QML

    :param module_items: A dictionary with the qml_component_name as a key
    :type module_items: dict

    An item looks like this::
        module_items = {
            "MyQMLComponent" : {
                "class" : my_class_reference,
                "qml_module_name" : my_module_name,
                "version": 1,
                "subversion" : 0
            }
        }

    """
    for qml_object, data in module_items.items():
        args = [
            data["class"],
            data["qml_module_name"],
            data["version"],
            data["subversion"],
            qml_object
        ]
        qmlRegisterType(*args)

