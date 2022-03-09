from Backend.onlyfans import tempstat
from Backend.modbus import control
from Backend.params import *

# CPU temperature
print(f"Temperature: {tempstat()}°C")

# Control motors and view their status
#a = control(1, READ, MAINS_VOLTAGE, 1)[0]
print(control(1, READ, MAINS_VOLTAGE, 1)[0])
print(f"Current: {control(1, READ, MOTOR_CURRENT, 1)}\n\
Frequency: {control(1, READ, OUTPUT_FREQ, 1)}\n\
RPM: {control(1, READ, OUTPUT_VEL, 1)}\n\
Power: {control(1, READ, MOTOR_POWER, 1)}")
