# Determining Distance between Current Point and Target Location
# Pass coordinates as arguments
import math

def distance_to_target(Location1, Location2):
    dlat = Location1.lat - Location2.lat
    dlon = Location2.lon - Location2.lon
    return math.sqrt((dlat * dlat) + (dlon * dlon)) * 1.113195e5
