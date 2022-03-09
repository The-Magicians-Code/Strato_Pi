from Backend.onlyfans import tempstat
from Backend.modbus import control
from Backend.params import *

# CPU temperature
print(f"Temperature: {tempstat()}°C")

# Control motors and view their status
#a = control(1, READ, MAINS_VOLTAGE, 1)[0]
print(f"Voltage: {control(1, READ, MAINS_VOLTAGE, 1)[0]/10.0} V\n\
Current: {control(1, READ, MOTOR_CURRENT, 1)[0]/10.0} A\n\
Frequency: {control(1, READ, OUTPUT_FREQ, 1)[0]/10.0} Hz\n\
RPM: {control(1, READ, OUTPUT_VEL, 1)[0]} rpm\n\
Power: {control(1, READ, MOTOR_POWER, 1)[0]} %")

#control mains
mode = control(1, READ, REF_SWITCH, 1)[0] #if write then control 1 Read REF_SWITCH terminal/modbusis
#modes = dict()
print(f"Mode: {mode}")
if mode == W_TERMINAL:
    print("Terminal")
if mode == W_MODBUS:
    print("Modbus")
