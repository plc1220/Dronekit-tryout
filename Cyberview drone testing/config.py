# Initialisation

from dronekit import connect, VehicleMode, LocationGlobalRelative, LocationGlobal, Command
import math
import time
from pymavlink import mavutil

def init():
    global vehicle
    ## Works for Windows SITL
    #Set up option parsing to get connection string
    CoSe = input('Enter Desired Connection way: \n1) USB\n2) Home\n3)TCP\n4)COM')

    if CoSe == '1':
        connection_string =  '/dev/ttyUSB0'
    elif CoSe == '2':
        connection_string =  "127.0.0.1:14551"
    elif CoSe == '3':
        connection_string = 'tcp:127.0.0.1:5760'    
    elif Cose == '4':
        COMNO = input('Enter COM port number:')
        connection_string = ('com'+str(COMNO))

    # Connect to the Vehicle.
    #   Set `wait_ready=True` to ensure default attributes are populated before `connect()` returns.
    print("\nConnecting to vehicle on: %s" % connection_string)
    vehicle = connect(connection_string, wait_ready = True)

    return None
