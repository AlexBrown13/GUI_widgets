import QtQuick 2.15

Rectangle {
        id: leftScreen
        anchors {
            left: parent.left
            right: rightScreen.left
            bottom: bottomBar.top
            top: parent.top
        }

        color: "white"

        Image {
            id: droneRender
            anchors.centerIn: parent
            width: parent.width * 0.75
            fillMode: Image.PreserveAspectFit
            source: "../assests/droneRender.png"
        }
    }