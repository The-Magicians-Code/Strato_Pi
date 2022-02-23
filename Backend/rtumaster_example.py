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

# importing modules
import time
import serial
import modbus_tk
import modbus_tk.defines as cst
from modbus_tk import modbus_rtu

#PORT = 1
PORT = '/dev/ttyAMA0'

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
        
        logger.info(master.execute(2, cst.WRITE_SINGLE_REGISTER, 8501, output_value=0x0006)) #Shutdown režiim, vajalik sagedusmuunduri initsaliseerimiseks
        time.sleep(3)
        logger.info(master.execute(2, cst.WRITE_SINGLE_REGISTER, 8501, output_value=0x000F)) #Enable operation režiim, paneb mootori pöörlema päripäeva
        logger.info(master.execute(2, cst.WRITE_SINGLE_REGISTER, 8502, output_value=300)) #Seadistab mootori sageduseks 10 Hz, all on veel näiteid erinevatest seadesuurustest
        time.sleep(3)

        logger.info(master.execute(2, cst.WRITE_SINGLE_REGISTER, 8501, output_value=0x0006)) #Shutdown režiim, vajalik sagedusmuunduri pöörlemissuuna muutmiseks (tuleks katsetada, kas on üldse vaja mootor seiskada?)
        time.sleep(3)
        logger.info(master.execute(2, cst.WRITE_SINGLE_REGISTER, 8501, output_value=0x080F)) #Enable operation režiim, paneb mootori pöörlema vastupäeva
        logger.info(master.execute(2, cst.WRITE_SINGLE_REGISTER, 8502, output_value=40)) #Seadistab mootori sageduseks 4 Hz
        time.sleep(3)
        logger.info(master.execute(2, cst.WRITE_SINGLE_REGISTER, 8501, output_value=0x0006)) #Shutdown režiim, peatab mootori
        
        
        logger.info(master.execute(3, cst.WRITE_SINGLE_REGISTER, 8501, output_value=0x0006)) #Shutdown režiim, vajalik sagedusmuunduri initsaliseerimiseks
        time.sleep(3)
        logger.info(master.execute(3, cst.WRITE_SINGLE_REGISTER, 8501, output_value=0x000F)) #Enable operation režiim, paneb mootori pöörlema päripäeva
        logger.info(master.execute(3, cst.WRITE_SINGLE_REGISTER, 8502, output_value=100)) #Seadistab mootori sageduseks 10 Hz, all on veel näiteid erinevatest seadesuurustest
        time.sleep(3)

        logger.info(master.execute(3, cst.WRITE_SINGLE_REGISTER, 8501, output_value=0x0006)) #Shutdown režiim, vajalik sagedusmuunduri pöörlemissuuna muutmiseks (tuleks katsetada, kas on üldse vaja mootor seiskada?)
        time.sleep(3)
        logger.info(master.execute(3, cst.WRITE_SINGLE_REGISTER, 8501, output_value=0x080F)) #Enable operation režiim, paneb mootori pöörlema vastupäeva
        logger.info(master.execute(3, cst.WRITE_SINGLE_REGISTER, 8502, output_value=40)) #Seadistab mootori sageduseks 4 Hz
        time.sleep(3)
        logger.info(master.execute(3, cst.WRITE_SINGLE_REGISTER, 8501, output_value=0x0006)) #Shutdown režiim, peatab mootori
        
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

control()
