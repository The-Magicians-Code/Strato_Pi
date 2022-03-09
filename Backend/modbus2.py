# All imports are in params.py file
from params import *
import time

class Controller:
    """
    Controller class:
    arguments:
    - slave number: integer
    - register address: integer
    - control code: instruction value

    init sets up modbus master,
    parameters are set in params.py file

    read_value() - read register value
    write_value() - set register value
    """
    def __init__(self, slave_number, reg_address, control_code):
        self.slave_number=slave_number
        self.reg_address=reg_address
        self.control_code=control_code

        master = modbus_rtu.RtuMaster(
            serial.Serial(
                port=PORT, baudrate=BAUDRATE, bytesize=BYTESIZE, 
                parity=PARITY, stopbits=STOPBITS, xonxoff=XONXOFF
            )
        )
        master.set_timeout(5.0)
        master.set_verbose(True)
        
        self.master=master

    def read_value(self):
        value = self.master.execute(self.slave_number, READ, self.reg_address, self.control_code)
        return value[0]
    def write_value(self):
        self.master.execute(self.slave_number, WRITE, self.reg_address, output_value=self.control_code)

# Example usage
#motor_1 = Controller(1, 3207, 1)
#print(motor_1.read_value())

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
    else:
        master.execute(slave_number, WRITE, reg_address, output_value=control_code)
    
# Example usage for function
print(control(1, READ, 8411, 1))
control(1, WRITE, 8411, 96)
print(control(2, READ, 8411, 1))
control(2, WRITE, 8411, 96)
print(control(3, READ, 8411, 1))
control(3, WRITE, 8411, 96)

#print(control(2, READ, 5212, 1))
control(1, WRITE, 5212, 0b00)
control(2, WRITE, 5212, 0b00)
control(3, WRITE, 5212, 0b00)
#print(control(2, READ, 5212, 1))
#control(3, WRITE, 8602, 0x0006)
#control(3, WRITE, 8602, 0x000F)


#time.sleep(10)

#control(1, WRITE, 8601, 0x0006)
#control(3, WRITE, 8601, 0x0006)