# All imports are in params.py file
from params import *

master = modbus_rtu.RtuMaster(
    serial.Serial(
        port=PORT, baudrate=BAUDRATE, bytesize=BYTESIZE, 
        parity=PARITY, stopbits=STOPBITS, xonxoff=XONXOFF
    )
)
master.set_timeout(5.0)
master.set_verbose(True)

def control(slave_number, operation, reg_address, control_code):
    if operation == READ:
        value = master.execute(slave_number, READ, reg_address, control_code)
        return value
    else
        master.execute(slave_number, WRITE, reg_address, output_value=control_code)
    
# Example usage for function
control(1, READ, 3207, 1)