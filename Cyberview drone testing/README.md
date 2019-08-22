# dronescript
Guiding the drone using GPS

# Notes
Do NOT remove mission.csv file's headings (aka 'latitude', 'longitude', altitude) as when pandas (the library used) read the csv file it automatically treats the first row as the headings of the file. This will cause the first row of GPS coordinates to be NOT included into the dataframe. This dataframe will be later converted into an array of GPS points. Effectively, this means that the drone will not fly to the first row of GPS coordinates if headings are not used in the csv file.

# Successful Flight
13 Aug 2019 (flight log saved under name flight_log.txt)

# Further Improvements
- Auto-saving flight log feature
- Run "main.py" code immediately after Raspberry Pi is booted
