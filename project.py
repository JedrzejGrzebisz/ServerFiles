#!/usr/bin/python3
from sense_emu import SenseHat
import json
import time

sense = SenseHat()

# Zdefiniowanie słowników z wartościami odcztanymi z SenseHat
weatherDataDict = {"TemperatureC": 0,
                   "PressureHPa": 0,
                   "HumidityPercentage": 0,
                   "TemperatureF": 0,
                   "PressureMmHg": 0,
                   "Humidity01": 0
                   }
rpyRadDict = {"Roll": 0, "Pitch": 0, "Yaw": 0}
rpyDegDict = {"Roll": 0, "Pitch": 0, "Yaw": 0}
joystickDataDict = {"xAxis": 0, "yAxis": 0, "center": 0}


def weather_condition():
    tempC = sense.temp
    tempF = 32.0 + 1.8 * tempC
    weatherDataDict['TemperatureC'] = tempC
    weatherDataDict['TemperatureF'] = tempF

    pressureHPa = sense.pressure
    pressureMmHg = pressureHPa * 0.75
    weatherDataDict['PressureHPa'] = pressureHPa
    weatherDataDict['PressureMmHg'] = pressureMmHg

    humidityPercentage = sense.humidity
    humidity01 = humidityPercentage / 100
    weatherDataDict['HumidityPercentage'] = humidityPercentage
    weatherDataDict['Humidity01'] = humidity01

    weatherDataDictJson = json.dumps(weatherDataDict)
    try:
        dataFile = open("weatherCondition.json", "w")
        dataFile.write(weatherDataDictJson)
    except:
        print("Write Error")
    finally:
        dataFile.close()


def rpy_value():
    radians = sense.get_orientation_radians()
    degrees = sense.get_orientation_degrees()

    rpyRadDict['Roll'] = radians['roll']
    rpyRadDict['Pitch'] = radians['pitch']
    rpyRadDict['Yaw'] = radians['yaw']

    rpyDegDict['Roll'] = degrees['roll']
    rpyDegDict['Pitch'] = degrees['pitch']
    rpyDegDict['Yaw'] = degrees['yaw']

    rpyRadDictJson = json.dumps(rpyRadDict)
    rpyDegDictJson = json.dumps(rpyDegDict)

    try:
        dataFileRad = open("rpyValueRad.json", "w")
        dataFileDeg = open("rpyValueDeg.json", "w")

        dataFileRad.write(rpyRadDictJson)
        dataFileDeg.write(rpyDegDictJson)
    except:
        print("Write Error")
    finally:
        dataFileRad.close()
        dataFileDeg.close()


def joystick_value():
    for e in sense.stick.get_events():
        if e.action == "pressed":
            if e.direction == "right":
                joystickDataDict["xAxis"] += 1
            if e.direction == "left":
                joystickDataDict["xAxis"] -= 1
            if e.direction == "up":
                joystickDataDict["yAxis"] += 1
            if e.direction == "down":
                joystickDataDict["yAxis"] -= 1
            if e.direction == "middle":
                joystickDataDict["center"] += 1

    joystickDataDictJson = json.dumps(joystickDataDict)
    try:
        dataFile = open("joystick.json", "w")
        dataFile.write(joystickDataDictJson)
    except:
        print("Write error")
    finally:
        dataFile.close()


try:
    while True:
        weather_condition()
        rpy_value()
        joystick_value()

        print(weatherDataDict)
        print(rpyRadDict)
        print(rpyDegDict)
        print(joystickDataDict)

        time.sleep(0.1)
except KeyboardInterrupt:
    pass
