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
        
        logger = modbus_tk.utils.create_logger("console")
        master = modbus_rtu.RtuMaster(
            serial.Serial(port='/dev/ttyAMA0', baudrate=9600, bytesize=8, parity='N', stopbits=1, xonxoff=0)
        )
        master.set_timeout(5.0)
        master.set_verbose(True)
        logger.info("connected")

        self.master=master
        self.logger=logger

    def read_value(self):
        v = self.master.execute(self.motor_number, cst.READ_HOLDING_REGISTERS, self.reg_aadress, self.control_code)
    #def write_value(self):
    #    logger.info(master.execute(1, cst.WRITE_SINGLE_REGISTER, 8501, output_value=0x0006))

motor_1 = Controller(1, 3207, 1)
motor_1.read_value()

def control():
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
       
        # Template registrite lugemiseks sagedusmuundurilt. Esimene parameeter on slave aadress, teine parameeter on tehtav operatsioon (lugemine või kirjutamine), 
        # kolmas parameeter on loetav registri aadress, neljas parameeter mitu registrit loetakse või andmed mida registrisse kirjutada tuleb
        
        #logger.info(master.execute(1, cst.READ_HOLDING_REGISTERS, 3207, 1)) #andmete lugemine
        #logger.info(master.execute(2, cst.READ_HOLDING_REGISTERS, 3207, 1))
        #logger.info(master.execute(1, cst.READ_HOLDING_REGISTERS, 8603, 2))

        
        #Selleks, et sagedusmuundur saaks mootorit juhtida, tuleb sagedusmuundur õigesse režiimi saada. Kokku on 6 režiimi (vaata dokumentatsioonist). 
        #Meile olulised on hetkel ainult kaks (kolm) režiimi: Shutdown, (Ready), Enable operation. 
        #All on koodilõik, mis paneb mootori pöörlema päripäeva 3s ja vastupäeva 3s

        #master execute (slave_adress, READ/WRITE, register adress, command/value to be read)
        logger.info(master.execute(1, cst.WRITE_SINGLE_REGISTER, 8501, output_value=0x0006)) #Shutdown režiim, vajalik sagedusmuunduri initsaliseerimiseks
        time.sleep(3)
        logger.info(master.execute(1, cst.WRITE_SINGLE_REGISTER, 8501, output_value=0x000F)) #Enable operation režiim, paneb mootori pöörlema päripäeva
        logger.info(master.execute(1, cst.WRITE_SINGLE_REGISTER, 8502, output_value=100)) #Seadistab mootori sageduseks 10 Hz, all on veel näiteid erinevatest seadesuurustest
        time.sleep(3)

        logger.info(master.execute(1, cst.WRITE_SINGLE_REGISTER, 8501, output_value=0x0006)) #Shutdown režiim, vajalik sagedusmuunduri pöörlemissuuna muutmiseks (tuleks katsetada, kas on üldse vaja mootor seiskada?)
        time.sleep(3)
        logger.info(master.execute(1, cst.WRITE_SINGLE_REGISTER, 8501, output_value=0x080F)) #Enable operation režiim, paneb mootori pöörlema vastupäeva
        logger.info(master.execute(1, cst.WRITE_SINGLE_REGISTER, 8502, output_value=40)) #Seadistab mootori sageduseks 4 Hz
        time.sleep(3)
        logger.info(master.execute(1, cst.WRITE_SINGLE_REGISTER, 8501, output_value=0x0006)) #Shutdown režiim, peatab mootori
        
        #Juhtida saab ka seadistades mootori pöörlemiskiirust või % nimimomendist
        #logger.info(master.execute(1, cst.WRITE_SINGLE_REGISTER, 8602, output_value=200)) #Seab mootori kiiruseks 200 rpm
        #logger.info(master.execute(1, cst.WRITE_SINGLE_REGISTER, 8505, output_value=150)) #Seab mootori seadesuuruseks 15% nimimomendist
        
        #Autotune koodinäide
        #logger.info(master.execute(1, cst.WRITE_SINGLE_REGISTER, 8501, output_value=0x0006)) #Shutdown režiim, vajalik sagedusmuunduri initsaliseerimiseks
        #logger.info(master.execute(1, cst.WRITE_SINGLE_REGISTER, 9615, output_value=1)) #Autotune = true
        #logger.info(master.execute(1, cst.WRITE_SINGLE_REGISTER, 8501, output_value=0x000F)) #Enable operation režiim, võimaldab sagedusmuunduril teha autotune
        
        #FYI. Ärge kustutage, vb saab hiljem kasutada
        #logger.info(master.execute(1, cst.READ_COILS, 0, 10))
        #logger.info(master.execute(1, cst.READ_DISCRETE_INPUTS, 0, 8))
        #logger.info(master.execute(1, cst.READ_INPUT_REGISTERS, 100, 3))
        #logger.info(master.execute(1, cst.READ_HOLDING_REGISTERS, 100, 12))
        #logger.info(master.execute(1, cst.WRITE_SINGLE_COIL, 7, output_value=1))
        #logger.info(master.execute(1, cst.WRITE_MULTIPLE_COILS, 0, output_value=[1, 1, 0, 1, 1, 0, 1, 1]))
        #logger.info(master.execute(1, cst.WRITE_MULTIPLE_REGISTERS, 100, output_value=xrange(12)))

    except modbus_tk.modbus.ModbusError as exc:
        logger.error("%s- Code=%d", exc, exc.get_exception_code())

#control()