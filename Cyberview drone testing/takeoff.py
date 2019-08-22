# takeoff script
from dronekit import connect, VehicleMode, LocationGlobalRelative, LocationGlobal, Command
import math
import time
from pymavlink import mavutil
import config
from pre_arm_check import pre_arm_check
import home_location

def takeoff(TargetAltitude):
    pre_arm_check()
    home_location.home()

    time.sleep(1)

    print("Taking off!")
    config.vehicle.simple_takeoff(TargetAltitude)

    while config.vehicle.mode == VehicleMode("GUIDED"):
        print(" Altitude: ", config.vehicle.location.global_relative_frame.alt)      
        if config.vehicle.location.global_relative_frame.alt>=TargetAltitude*0.95: #Trigger just below target alt.
            print("Reached target altitude")
            break
        time.sleep(1)

    if config.vehicle.mode != VehicleMode("GUIDED"):
        print("RC Interrupt")
        print("Mode changed to: %s" % config.vehicle.mode)
        return None

    else:
        return None
