# Week 2, Exercise 5 -- tonight.py uses the station_math module
# Run from THIS folder (station_math.py must be next to this file):
#   python tonight.py
#
# (a) tonight.py only CALLS the functions by name. If you improve a formula
#     inside station_math.py, nothing here needs to change.
# (b) No. Variables created inside wind_chill are LOCAL: they exist only
#     while the function runs and vanish when it returns. Only the
#     returned value comes back.
import station_math                  # file name without .py

outside = -17.1
wind = 35.0
duty_hours = 11

watches, spare = station_math.split_shift(duty_hours)   # unpack the two returned values

print(f"Outside: {outside} C = {station_math.c_to_f(outside):.2f} F")
print(f"Freezing: {station_math.is_freezing(outside)}")
print(f"Feels like: {station_math.wind_chill(outside, wind):.1f} C in the wind")
print(f"Watches: {watches} full, {spare} hours spare")
