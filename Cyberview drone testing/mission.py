# GPS guided mission script

from dronekit import connect, VehicleMode, LocationGlobalRelative, LocationGlobal, Command
import math
import time
from pymavlink import mavutil
import config
import numpy as np
from distance_calculate import distance_to_target
from mission_loader import mission_load

def mission():
    if config.vehicle.mode == VehicleMode("GUIDED"):
        print ("\nLoading Mission")
        gps_points = np.array(mission_load())
        print ("\nReceived GPS Points")

        # Determine size of gps points' array
        nrows = len(gps_points)
        ncols = len(gps_points[0])

        # Print amount of GPS Points there are
        print("\nThere are %d Target Locations" % (nrows))

    else:
        return None

    # Assuming that the data is stored as 3 columns (lat, lon, alt)
    for i in range (nrows):
        if config.vehicle.mode == VehicleMode("GUIDED"):
            target_location = LocationGlobalRelative(gps_points[i, 0], gps_points[i, 1], gps_points[i, 2])
            print("\nHeading to Target Location %d: %s" % (i + 1, target_location))

            config.vehicle.simple_goto(target_location, groundspeed=3)

            while config.vehicle.mode == VehicleMode("GUIDED"):
                vehicle_location = config.vehicle.location.global_relative_frame
                print("Current Location: %s" % vehicle_location)
                time.sleep(1)
                distance = distance_to_target(vehicle_location, target_location)
                print("Distance from Target Location: %f" % distance)
                if distance <= 1:
                    print("Reached Target Location")
                    break
                    
            time.sleep(1)

            RC_Interrupt = 0
        else:
            print("RC Interrupt")
            print("Mode changed to: %s" % config.vehicle.mode)
            RC_Interrupt = 1
            break

    if RC_Interrupt == 0:
        print("Mission completed, vehicle returning to launch.")
        config.vehicle.mode = VehicleMode("RTL")
        return None
    else:
        return None
