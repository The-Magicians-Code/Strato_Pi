#!/usr/bin/env python
# -*- coding: utf_8 -*-
import time
import serial
import modbus_tk
import modbus_tk.defines as cst
from modbus_tk import modbus_rtu
#import params as ps

PORT = '/dev/ttyAMA0'

class Controller:
    def __init__(self, motor_number, reg_aadress, control_code):
        self.motor_number=motor_number
        self.reg_aadress=reg_aadress
        self.control_code=control_code
        
        #logger = modbus_tk.utils.create_logger("console")
        master = modbus_rtu.RtuMaster(
            serial.Serial(port='/dev/ttyAMA0', baudrate=9600, bytesize=8, parity='N', stopbits=1, xonxoff=0)
        )
        master.set_timeout(5.0)
        master.set_verbose(True)
        #logger.info("connected")

        self.master=master
        #self.logger=logger

    def read_value(self):
        v = self.master.execute(self.motor_number, cst.READ_HOLDING_REGISTERS, self.reg_aadress, self.control_code)
        print(v[0]/10.0)
    #def write_value(self):
    #    logger.info(master.execute(1, cst.WRITE_SINGLE_REGISTER, 8501, output_value=0x0006))

motor_1 = Controller(1, 3207, 1)
motor_1.read_value()