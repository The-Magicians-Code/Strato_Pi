from Backend.onlyfans import tempstat
from Backend.modbus import control
from Backend.params import *

# CPU temperature
print(f"Temperature: {tempstat()}°C")

# Control motors and view their status
#a = control(1, READ, MAINS_VOLTAGE, 1)[0]
print(control(1, READ, MAINS_VOLTAGE, 1)[0])