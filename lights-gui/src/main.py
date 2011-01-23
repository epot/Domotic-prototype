'''
Created on 23 janv. 2011

@author: epot
'''

import sys
import serial
from PyQt4 import QtGui
from widgets.mainwindow import MainWindow

def initSerial():
    ser = serial.Serial(2)
    ser.setTimeout(0.5)
    print "Communicating through " + ser.portstr
    return ser
    
def testMethod():
    ser = initSerial()
    ser.write("*25*16*#11430978##")
    ser.close()

def main():
    app = QtGui.QApplication(sys.argv)
    window=MainWindow()
    window.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
#    testMethod()