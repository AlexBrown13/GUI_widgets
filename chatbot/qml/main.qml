import QtQuick 2.15
import QtQuick.Controls 2.15
import "ui/BottomBar"
import "ui/RightScreen"
import "ui/LeftScreen"

ApplicationWindow { 
    id: window
    width: 1280
    height: 720
    visible: true
    title: qsTr("QuadCopter")
    
    property QtObject backend
    property string currTime: "00:00:00"
    property string currDay: ""
    property string currForecast: ""

    LeftScreen {
        id: leftScreen
    }
    
    RightScreen {
        id: rightScreen
    }

    BottomBar {
        id: bottomBar
    }
}