'''
Created on 23 janv. 2011

@author: epot
'''

import sys
import serial
from PyQt4 import QtGui
from qtapp.widgets.mainwindow import MainWindow

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
    
    try:
        window=MainWindow()
        window.show()
    except serial.SerialException, e:
        msgBox = QtGui.QMessageBox(QtGui.QMessageBox.Critical,
                                   app.tr("Critical error"), 
                                   app.tr("Could not initialize connection..."))
        msgBox.setDetailedText(str(e))
        msgBox.open()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
#    testMethod()