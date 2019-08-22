# Guided Mission Main

from __future__ import print_function

from dronekit import connect, VehicleMode, LocationGlobalRelative, LocationGlobal, Command
import math
import time
from pymavlink import mavutil

import config
import guided_check
import mission_loader
from mission import mission
from takeoff import takeoff


config.init()
config.vehicle.mode = VehicleMode("GUIDED") #uncomment this if using SITL comment if not
guided_check.check()

if config.vehicle.mode == VehicleMode("GUIDED"):
    takeoff(3)
    time.sleep(1)
    mission()

else:
    print("RC Interrupt")
    print("Mode changed to: %s" % config.vehicle.mode)

print("Closing vehicle object")
config.vehicle.close()

# Shut down simulator if it was started.
if config.sitl:
    config.sitl.stop()

print("Completed")
