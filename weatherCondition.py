#!/usr/bin/python3
from sense_emu import SenseHat
import json
import time

sense = SenseHat()
weatherDataDict = {"TemperatureC": 0,
                   "PressureHPa": 0,
                   "HumidityPercentage": 0,
                   "TemperatureF": 0,
                   "PressureMmHg": 0,
                   "Humidity01": 0
                   }

try:
    while True:
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

        print(weatherDataDictJson)
        time.sleep(0.1)
except KeyboardInterrupt:
    pass
