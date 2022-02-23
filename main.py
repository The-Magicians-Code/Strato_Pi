from Backend.onlyfans import tempstat
from Backend.modbus import control
from Backend.params import *

# CPU temperature
tempstat()

# Control motors and view their status
print(control(1, READ, 3207, 1)[0])