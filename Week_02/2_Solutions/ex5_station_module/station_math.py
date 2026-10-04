# Week 2, Exercise 5 -- the station math MODULE
# A module is just a .py file full of functions that other files can import.
# This file only DEFINES functions; it prints nothing by itself.

def c_to_f(celsius):
    """Celsius to Fahrenheit."""
    return (9 / 5) * celsius + 32


def wind_chill(temp_c, wind_kmh):
    """The standard wind-chill formula (temperature in C, wind in km/h)."""
    return 13.12 + 0.6215 * temp_c - 11.37 * wind_kmh ** 0.16 + 0.3965 * temp_c * wind_kmh ** 0.16


def split_shift(hours):
    """Return full 4-hour watches and the leftover hours -- two values."""
    return hours // 4, hours % 4


def is_freezing(celsius):
    """True below zero -- the comparison already IS the boolean."""
    return celsius < 0
