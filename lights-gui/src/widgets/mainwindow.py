'''
Created on 23 janv. 2011

@author: patt
'''

from PyQt4 import QtGui, QtCore

from commands.lightcommand import LightCommand
from model.lightmodel import LightModel
import serial

class MainWindow(QtGui.QMainWindow):
    '''
    classdocs
    '''


    def __init__(self):
        '''
        Constructor
        '''
        QtGui.QMainWindow.__init__(self)
        centralWidget = QtGui.QWidget(self)
        self.setCentralWidget(centralWidget)
        self.layout = QtGui.QVBoxLayout(centralWidget)
        quitBtn = QtGui.QPushButton("Quit", centralWidget)
        layoutbTN = QtGui.QHBoxLayout()
        layoutbTN.addStretch()
        layoutbTN.addWidget(quitBtn)
        quitBtn.clicked.connect(self.close)
        
        onBtn = QtGui.QPushButton("on", centralWidget)
        offBtn = QtGui.QPushButton("off", centralWidget)
        layoutLights = QtGui.QHBoxLayout()
        layoutLights.addStretch()
        layoutLights.addWidget(onBtn)
        layoutLights.addWidget(offBtn)
#        QtCore.QObject.connect(onBtn, QtCore.SIGNAL('clicked()'), self.on)  
#        QtCore.QObject.connect(onBtn, QtCore.SIGNAL('clicked()'), self.off)  
        onBtn.clicked.connect(self.on)
        offBtn.clicked.connect(self.off)
           
        self.layout.addLayout(layoutLights)
        self.layout.addStretch()
        self.layout.addLayout(layoutbTN)

        self.initModel()
        
    def initModel(self):
        self.cmd = self.__initSaintRaphHouse()
        
    def __initSerial(self):
        ser = serial.Serial(2)
        ser.setTimeout(0.5)
        print "Communicating through " + ser.portstr
        return ser

    def __initSaintRaphHouse(self):
        lightTv = LightModel("Light above TV", 11430977)
        cmd = LightCommand(lightTv, self.__initSerial())
        return cmd
    
    @QtCore.pyqtSlot()
    def on(self):
        self.cmd.setOn()
        
    @QtCore.pyqtSlot()
    def off(self):
        self.cmd.setOff()

