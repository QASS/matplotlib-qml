import QtQuick 2.0
Item {
    property var qmlConnector_arrayPointer: []
    property var qmlConnector_arrayID: []
    Connections {
        id: connection
        target: Connector
        ignoreUnknownSignals: true

        function evaluate(str){eval(str)} // wrap
        //Slots triggered from QML-Connector:
        // Confirms the test signal from the Qml connector
        onSendTestSignal:
            connection.target.testResult()

        // Sets a new value (for Widgets)
        onSendToQmlSignalOne:
            evaluate(qmlWidgetID + "." + attribut + "=\"" + value + "\"")
        // Returns the last set value
        onLastOperationTestWidget:
            connection.target.operationResult(evaluate(qmlWidgetID + "." + attribut))

        // Sets a new value (for variables)
        onSendToQmlSignalTwo:{
            var tA = {}
            tA = value
            evaluate(varName + " = " + tA)
        }
        // Sets a Array
        onSendToQmlSignalThree: {
            var tA = []
            tA = ary
            evaluate(varName+"=[]")
            for (var i = 0; i < tA.length; i++) {
                evaluate(varName +".push(\""+tA[i]+"\")")
            }
        }
        // Returns the last set value
        onLastOperationTestValue:
            connection.target.operationResult(evaluate(varName))
        // Returns the value of an Object
        onSendToQmlSignalFour:
            connection.target.value(evaluate(varName + attribut))
        // Call function
        onSendToQmlSignalFive:
            connection.target.funcReturn(evaluate(functionName))
        // Execute script
        onSendToQmlSignalSix: {
            var error = "true"
            try {
                var pointer
                for (var i = 0; i < qmlConnector_arrayID.length; i++) {
                    if (qmlConnector_arrayID[i] === par) {
                        par = "qmlConnector_arrayPointer["+i+"]." + par
                        break;
                    }
                }
                pointer = Qt.createQmlObject(script, evaluate(par), "QC_scripted_object");
                qmlConnector_arrayPointer.push(pointer)
            }
            catch (exeption) {
                error = exeption + ".toString()"
            }
            connection.target.scriptResult(error)
        }
        onSendToQmlSignalSeven: {

            var tA = []
            tA = ary
            evaluate(varName+"=[]")
            for (var i = 0; i < tA.length; i++) {
                evaluate(varName +".push(\""+tA[i]+"\")")
            }
        }
        onSendToQmlSignalEight: {
            for (var key in json) {
                //console.log(key + ": " + json[key]);
                evaluate (qmlWidgetID + "." + key + "=\"" + json[key] + "\"")
            }
        }
        onGetObjectPropertiesByName:{
            objectName
            evaluate()
            connection.target.operationResult("hallo")
        }
    }
}
