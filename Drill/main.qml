import QtQuick 2.15
import QtQuick.Controls 2.15

ApplicationWindow {
    visible: true
    width: 600
    height: 500
    title: "Clock"
    property string currTime: "00:00:00"
    property QtObject backend

    Rectangle {
        anchors.fill: parent

        Image {
            anchors.fill: parent
            source: "./images/space.png"
            fillMode: Image.PreserveAspectCrop
        }

        Rectangle {
            anchors.fill: parent
            color: "transparent"

            Text {
                anchors {
                    bottom: parent.bottom
                    bottomMargin: 24
                    left: parent.left
                    leftMargin: 24
                }
                text: currTime
                font.pixelSize: 44
                color: "white"
            }

            Text {
                anchors {
                    horizontalCenter: parent.horizontalCenter
                }
                text: "Hello"
                font.pixelSize: 24
                color: "white"
            }
        }

            CheckBox {
                id: checkBoxAccept
                checked: true
                text: "Accept"

                onCheckedChanged: {
                    backend.checkbox_changed(checked)
                }
            }    

            Button {
                id: myButton
                width: 100
                height: 50
                text: "click me"
                anchors.centerIn: parent

                onClicked: {
                    console.log("clicked")
                }

                background: Rectangle {
                    color: myButton.pressed ? "#abc456" : "#234aaa"
                }
            }
    }

    
    Connections {
        target: backend

        function onUpdated(msg) {
            currTime = msg;
        }
    }

}