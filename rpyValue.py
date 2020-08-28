#!/usr/bin/python3
from sense_emu import SenseHat
import json
import time

sense = SenseHat()
rpyRadDict = {"Roll": 0, "Pitch": 0, "Yaw": 0}
rpyDegDict = {"Roll": 0, "Pitch": 0, "Yaw": 0}

try:
    while True:
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

        print(rpyRadDictJson)
        print(rpyDegDictJson)
        time.sleep(0.1)
except KeyboardInterrupt:
    pass
