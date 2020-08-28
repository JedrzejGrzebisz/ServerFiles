#!/usr/bin/python3
from sense_emu import SenseHat
import json

sense = SenseHat()
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
orange = (255, 165, 0)
white = (255, 255, 255)
colorPicked = ()


dataFile = open("singleLedColor.json", "r")
dataLedJson = dataFile.readline()
dataFile.close()
dataLed = json.loads(dataLedJson)

if dataLed["color"] == "red":
    colorPicked = red
elif dataLed["color"] == "green":
    colorPicked = green
elif dataLed["color"] == "blue":
    colorPicked = blue
elif dataLed["color"] == "orange":
    colorPicked = orange
elif dataLed["color"] == "white":
    colorPicked = white
else:
    colorPicked = (0, 0, 0)

sense.set_pixel(dataLed["column"], dataLed["row"], colorPicked)
