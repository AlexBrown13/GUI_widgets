import QtQuick 2.15
import QtPositioning
import QtLocation

Rectangle {
        id: rightScreen

        anchors {
            top: parent.top
            bottom: bottomBar.top
            right: parent.right
        }
        
        Plugin {
            id: mapPlugin
            name: "osm"
        }
        Map {
            anchors.fill: parent
            plugin: mapPlugin
            center: QtPositioning.coordinate(32.343, 34.913) // Ruppin College
            zoomLevel: 14
        }

        Text {
            id: dateTimeDispaly
            anchors {
                left: parent.left
                leftMargin: 40
                top: parent.top
                margins: 20
                
            }

            font.pixelSize: 12
            font.bold: true
            color: "black"
            text: window.currTime
        }

        Text {
            id: tempratureDisplay
            anchors {
                left: dateTimeDispaly.right
                leftMargin: 40
                bottom: dateTimeDispaly.bottom
            }

            font.pixelSize: 12
            font.bold: true
            color: "black"
            text: window.currForecast
        }

        Text {
            id: dayDisplay
            anchors {
                left: tempratureDisplay.right
                leftMargin: 40
                bottom: tempratureDisplay.bottom
            }

            font.pixelSize: 12
            font.bold: true
            color: "black"
            text: window.currDay
        }

        

        width: parent.width * 2/3


        Connections {
            target: window.backend

            function onTimeUpdated(params) {
                window.currTime = params;
            }

            function onDayUpdated(params) {
                window.currDay = params
            }

            function  onForecastReceived(params) {
                window.currForecast = params
            }
        }

    }

    
