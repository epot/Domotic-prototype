import serial
import time
from opennitoo.lightstatusrequest import LightStatusRequest
from opennitoo.lightbuscommand import LightBusCommand
from commands.lightcommand import LightCommand
from model.lightmodel import LightModel

import PyQt4
from PyQt4 import QtGui, QtCore

def initSerial():
    ser = serial.Serial(2)
    ser.setTimeout(0.5)
    print "Communicating through " + ser.portstr
    return ser

def initSaintRaphHouse():
    lightTv = LightModel("Light above TV", 11430977)
    cmd = LightCommand(lightTv, initSerial())
    return cmd
    
def testMethod():
    ser = initSerial()
    lightid = 11430977
    lightOff = LightBusCommand(False, lightid)
    ser.write(lightOff.getMessage())
    time.sleep(2)
    lightOn = LightBusCommand(True, lightid)
    ser.write(lightOn.getMessage())
    time.sleep(2)
    ser.write(lightOff.getMessage())
#    ser.write("*1*0*#11430977##")
    ser.close()
    
def main():
    print "flan"
#    testMethod()
    cmd = initSaintRaphHouse()
    cmd.setOn()
    time.sleep(2)
    cmd.setOff()

if __name__ == "__main__":
    try:
        main()
    except serial.SerialException, e:
        print "SerialException: " + str(e)
    except Exception, e:
        print "Exception: \"" + str(e) + "\""

    print "----------------------------------------"
    print "exiting...."