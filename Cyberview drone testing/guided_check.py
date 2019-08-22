# Checks for GUIDED mode

from __future__ import print_function

from dronekit import connect, VehicleMode, LocationGlobalRelative, LocationGlobal, Command
import math
import time
from pymavlink import mavutil

import config

def check():
    while config.vehicle.mode != VehicleMode("GUIDED"):
        print("Waiting for mode change")
        print("Current vehicle mode: %s" % config.vehicle.mode)
        time.sleep(1)
    
    print("Vehicle mode changed to GUIDED")
    
    return None
