# Setting Home Location
# Setting current location as home location

from dronekit import connect, VehicleMode, LocationGlobalRelative, LocationGlobal, Command
import math
import time
from pymavlink import mavutil
import config

def home():
    current_location = config.vehicle.location.global_frame
    config.vehicle.home_location = current_location
    print("New Home Location: %s" % config.vehicle.home_location)

    # Confirm current value on vehicle
    cmds = config.vehicle.commands
    cmds.download()
    cmds.wait_ready()
    print("Check new home location: %s" % config.vehicle.home_location)

    return None
