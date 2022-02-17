#!/usr/bin/env python
# -*- coding: utf_8 -*-
"""
 Modbus TestKit: Implementation of Modbus protocol in python

 (C)2009 - Luc Jean - luc.jean@gmail.com
 (C)2009 - Apidev - http://www.apidev.fr

 This is distributed under GNU LGPL license, see license.txt
 
 DO THIS BEFORE TESTING CODE!!!!
 
 On Raspberry Pi 3 and 4, the main UART (ttyAMA0) is used by default for Bluetooth, and
the TX/RX pins on the GPIO connector are controlled by a limited function Mini UART
(ttyS0).
To route the main UART to the RX/TX pins that are connected to the Strato Pi serial ports
you could disable Bluetooth. Edit /boot/config.txt and add these lines at the end of the file:
# Disable Bluetooth
dtoverlay=pi3-disable-bt
You may also run the following command to disable the Bluetooth HCI UART driver:
sudo systemctl disable hciuart
"""

import serial

import modbus_tk
import modbus_tk.defines as cst
from modbus_tk import modbus_rtu

#PORT = 1
PORT = '/dev/ttyAMA0'

def main():
    """main"""
    logger = modbus_tk.utils.create_logger("console")

    try:
        #Connect to the slave
        master = modbus_rtu.RtuMaster(
            serial.Serial(port=PORT, baudrate=9600, bytesize=8, parity='N', stopbits=1, xonxoff=0)
        )
        master.set_timeout(5.0)
        master.set_verbose(True)
        logger.info("connected")

        logger.info(master.execute(1, cst.READ_HOLDING_REGISTERS, 3207, 1))
        logger.info(master.execute(2, cst.READ_HOLDING_REGISTERS, 3207, 1))
        logger.info(master.execute(3, cst.READ_HOLDING_REGISTERS, 3207, 1))

        #send some queries
        #logger.info(master.execute(1, cst.READ_COILS, 0, 10))
        #logger.info(master.execute(1, cst.READ_DISCRETE_INPUTS, 0, 8))
        #logger.info(master.execute(1, cst.READ_INPUT_REGISTERS, 100, 3))
        #logger.info(master.execute(1, cst.READ_HOLDING_REGISTERS, 100, 12))
        #logger.info(master.execute(1, cst.WRITE_SINGLE_COIL, 7, output_value=1))
        logger.info(master.execute(2, cst.WRITE_SINGLE_REGISTER, 11951, output_value=15))
        #logger.info(master.execute(1, cst.WRITE_MULTIPLE_COILS, 0, output_value=[1, 1, 0, 1, 1, 0, 1, 1]))
        #logger.info(master.execute(1, cst.WRITE_MULTIPLE_REGISTERS, 100, output_value=xrange(12)))

    except modbus_tk.modbus.ModbusError as exc:
        logger.error("%s- Code=%d", exc, exc.get_exception_code())

if __name__ == "__main__":
    main()
