#!/usr/bin/python3

from sense_emu import SenseHat
import time
import json

sense = SenseHat()
joystickDataDict = {"xAxis": 0, "yAxis": 0, "center": 0}

try:
    while True:
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
        
        print(joystickDataDictJson)
        time.sleep(0.1)
        
except KeyboardInterrupt:
    pass

