# This file contains modbus control parameters
import time
import serial
import modbus_tk
import modbus_tk.defines as cst
from modbus_tk import modbus_rtu

# Setup modbus master/slave communication
WRITE = cst.WRITE_SINGLE_REGISTER
READ = cst.READ_HOLDING_REGISTERS
PORT = '/dev/ttyAMA0'
BAUDRATE = 9600
BYTESIZE = 8
PARITY = 'N'
STOPBITS = 1
XONXOFF = 0