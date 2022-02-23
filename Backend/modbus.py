from params import *

class Controller:
    """
    Controller class:
    arguments:
    - slave number: integer
    - register address: integer
    - control code: instruction value
    - delay: value for register write task, default=3
    """
    def __init__(self, slave_number, reg_address, control_code, delay=3):
        self.slave_number=slave_number
        self.reg_address=reg_address
        self.control_code=control_code
        self.delay=delay

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
        #print(v[0]/10.0)
        return value[0]
    def write_value(self):
        v = self.master.execute(self.slave_number, WRITE, self.reg_address, output_value=self.control_code)
        time.sleep(self.delay)

# Example usage
motor_1 = Controller(1, 3207, 1)
print(motor_1.read_value())

# Function based method for reading/writing into registers
def control(slave_number, operation, reg_address, control_code):
    master = modbus_rtu.RtuMaster(
        serial.Serial(
            port=PORT, baudrate=BAUDRATE, bytesize=BYTESIZE, parity=PARITY, 
        stopbits=STOPBITS, xonxoff=XONXOFF
        )
    )
    master.set_timeout(5.0)
    master.set_verbose(True)

    value = master.execute(slave_number, operation, reg_address, control_code)
    return value[0]

#print(control(1, READ, 3207, 1))
