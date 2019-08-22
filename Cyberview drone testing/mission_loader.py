# Mission Loader

from __future__ import print_function
from dronekit import connect, VehicleMode, LocationGlobalRelative, LocationGlobal, Command
import config
import math
import time

# Import coordinates from csv file for python2.7
# def mission_load():
#     import csv
#     readable_data = []
#     with open("mission.csv") as csvfile:
#         reader = csv.reader(csvfile, quoting=csv.QUOTE_NONNUMERIC)
#         for row in reader:
#             readable_data.append(row)
#     return readable_data

# Import coordinates from csv file for python3.7
def mission_load():
    import pandas as pd
    raw_data = pd.read_csv("mission.csv")
    return raw_data.iloc[:, :].values

# Import coordinates from xls file (Excel) for python3.7
# def mission_load():
#     import pandas as pd
#     raw_data = pd.read_csv("mission.csv")
#     return raw_data.iloc[:, :].values
