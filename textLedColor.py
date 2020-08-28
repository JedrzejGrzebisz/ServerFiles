#!/usr/bin/python3
from sense_emu import SenseHat
import json

sense = SenseHat()
textColorList = []

dataFile = open("textLedColor.json", "r")
dataLedJson = dataFile.readline()
dataFile.close()
dataLed = json.loads(dataLedJson)
if dataLed["color"] == "red":
    textColorList = [255, 0, 0]
elif dataLed["color"] == "green":
    textColorList = [0, 255, 0]
elif dataLed["color"] == "blue":
    textColorList = [0, 0, 255]
elif dataLed["color"] == "orange":
    textColorList = [255, 165, 0]
elif dataLed["color"] == "white":
    textColorList = [255, 255, 255]
else:
    textColorList = [0, 0, 0]

sense.show_message(str(dataLed["text"]), text_colour=textColorList)
