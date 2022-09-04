# All imports are in params.py file

# Uncomment if this file is being run
#from params import *

# This is needed only for running the main.py
from Backend.params import *

# Setup master/slave connection
master = modbus_rtu.RtuMaster(
    serial.Serial(
        port=PORT, baudrate=BAUDRATE, bytesize=BYTESIZE, 
        parity=PARITY, stopbits=STOPBITS, xonxoff=XONXOFF
    )
)
master.set_timeout(5.0)
master.set_verbose(True)

def control(slave_number, operation, reg_address, control_code, delay=0, debug=False):
    """
    The modbus motor control function
    
    ARGS:
    - slave_number (int): Motor number
    - operation (int): READ or WRITE as int from parameters file
    - reg_address (int): Command register number
    - control_code (hex/int): Value to be written or read from the motor
    Optional:
    * delay (int): Used when writing to the motor register, (motor movement command had slight delays)
    * debug (bool): Use when you've blown something up, as usual
    """
    
    if operation == READ:
        try:
            value = master.execute(slave_number, READ, reg_address, control_code)
            return value
        except ModbusInvalidResponseError:
            if debug:
                print("Motor panel not configured or control with modbus not enabled on web")
            return (0, )
    else:
        try:
            value = master.execute(slave_number, WRITE, reg_address, output_value=control_code)
            time.sleep(delay)
            return value
        except ModbusInvalidResponseError:
            if debug:
                print("Problem with the writing procedure")
            return 0
    
# Example usage for function
#print(control(1, READ, MAINS_VOLTAGE, 1))
