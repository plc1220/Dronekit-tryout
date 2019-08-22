# Pre-Arm Checks script
from dronekit import connect, VehicleMode, LocationGlobalRelative, LocationGlobal, Command
import math
import time
from pymavlink import mavutil
import config

def pre_arm_check():
    print("Basic pre-arm checks")

    # Don't try to arm until autopilot is ready
    while not config.vehicle.is_armable:
        print(" Waiting for vehicle to initialise...")
        time.sleep(1)

    print("Arming motors")

    config.vehicle.armed = True
    while not config.vehicle.armed:
        print(" Waiting for arming...")
        time.sleep(1)

    return None
