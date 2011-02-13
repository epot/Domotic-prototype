'''
Created on 13 fevr. 2011

@author: patt
'''

from PyQt4 import QtCore
from time import gmtime, strftime

class SerialListenerThread(QtCore.QThread):
    '''
    classdocs
    '''


    def __init__(self, serial, parent = None):
        '''
        Constructor
        '''
        QtCore.QThread.__init__(self, parent)
        self.serial = serial
        
    def run(self):
        str = ""
        while(self.isRunning()):
            c = self.serial.read()
            str += c
            if(str.endswith("##")):
                print "sniffsniff[" + strftime("%H:%M:%S", gmtime()) + "] " + str
                str = ""
        