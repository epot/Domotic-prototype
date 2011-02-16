'''
Created on 23 janv. 2011

@author: patt
'''

from PyQt4 import QtGui, QtCore

from commands.lightcommand import LightCommand
from model.lightmodel import LightModel
from commands.shuttercommand import ShutterCommand
from model.shuttermodel import ShutterModel
import serial

from houses.house import House

from listener.SerialListenerThread import SerialListenerThread

class MainWindow(QtGui.QMainWindow):
    '''
    classdocs
    '''


    def __init__(self):
        '''
        Constructor
        '''
        QtGui.QMainWindow.__init__(self)
        self.ser = None
        self.setWindowTitle(self.tr("Home automation application"))

        self.__initModel()
        self.__createCentralWidget()
        self.__initMenuBar()
        
        # init thread dude !
        thread = SerialListenerThread(self.ser, self)
        thread.start()
        
    def __createCentralWidget(self):
        centralWidget = QtGui.QWidget(self)
        self.setCentralWidget(centralWidget)
        self.layout = QtGui.QVBoxLayout(centralWidget)
        quitBtn = QtGui.QPushButton("Quit", centralWidget)
        layoutbTN = QtGui.QHBoxLayout()
        layoutbTN.addStretch()
        layoutbTN.addWidget(quitBtn)
        quitBtn.clicked.connect(self.close)
        
        lightsGroup = QtGui.QGroupBox(self.tr("Lights"), self)       
        i = 0
        lightsLayout = QtGui.QGridLayout(lightsGroup)
        self.lightButtons = []
        self.lightSliders = []
        for lightCommand in self.lightCommands:
            onBtn = QtGui.QPushButton("on", centralWidget)
            offBtn = QtGui.QPushButton("off", centralWidget)
            lightsLayout.addWidget(QtGui.QLabel(lightCommand.getLight().getName()), i, 0)
            lightsLayout.addWidget(onBtn, i, 1)
            lightsLayout.addWidget(offBtn, i, 2)
            dimmerSlider = None
            if(lightCommand.getLight().getDimmerId() != None):
                dimmerSlider = QtGui.QSlider(QtCore.Qt.Horizontal, self)
                dimmerSlider.setMinimum(0)
                dimmerSlider.setMaximum(251)
                lightsLayout.addWidget(dimmerSlider, i, 3)
                dimmerTuple = lightCommand, dimmerSlider
                self.lightSliders.append(dimmerTuple)
                dimmerSlider.sliderReleased.connect(self.__setDimmer)
            
            onBtn.clicked.connect(self.__switchLight)
            offBtn.clicked.connect(self.__switchLight)
            lightTuple = lightCommand, onBtn, offBtn
            self.lightButtons.append(lightTuple)
            i += 1
            
        shuttersGroup = QtGui.QGroupBox(self.tr("Shutters"), self)      
        i = 0
        shuttersLayout = QtGui.QGridLayout(shuttersGroup)
        self.shutterButtons = []
        for shutterCommand in self.shutterCommands:
            upBtn = QtGui.QPushButton("up", centralWidget)
            stopBtn = QtGui.QPushButton("stop", centralWidget)
            downBtn = QtGui.QPushButton("down", centralWidget)
            shuttersLayout.addWidget(QtGui.QLabel(shutterCommand.getShutter().getName()), i, 0)
            shuttersLayout.addWidget(upBtn, i, 1)
            shuttersLayout.addWidget(stopBtn, i, 2)
            shuttersLayout.addWidget(downBtn, i, 3)
            upBtn.clicked.connect(self.__switchShutter)
            stopBtn.clicked.connect(self.__switchShutter)
            downBtn.clicked.connect(self.__switchShutter)
            shutterTuple = shutterCommand, upBtn, stopBtn, downBtn
            self.shutterButtons.append(shutterTuple)
            i += 1
           
        cmdGrp = QtGui.QGroupBox(self.tr("Command"), self)   
        layout = QtGui.QHBoxLayout(cmdGrp)
        self.cmdEdit = QtGui.QLineEdit(self)
        layout.addWidget(self.cmdEdit)
        cmdBtn = QtGui.QPushButton(self.tr("Send"), self)
        layout.addWidget(cmdBtn)
        cmdBtn.clicked.connect(self.__sendCommand)
        self.cmdEdit.returnPressed.connect(self.__sendCommand)
           
        self.layout.addWidget(lightsGroup)
        self.layout.addWidget(shuttersGroup)
        self.layout.addWidget(cmdGrp)
        self.layout.addStretch()
        self.layout.addLayout(layoutbTN) 
               
    def __initMenuBar(self):
        toolbar = self.menuBar()
        fileMenu = QtGui.QMenu(self.tr("File"), self)
        fileMenu.addAction(QtGui.QIcon(), self.tr("Quit"), self.close)
        helpMenu = QtGui.QMenu(self.tr("Help"), self)
        helpMenu.addAction(QtGui.QIcon(), self.tr("About"), self.aboutThisApp)
        toolbar.addMenu(fileMenu)
        toolbar.addMenu(helpMenu)
        
    def __initModel(self):
        self.__initSaintRaphHouse()
        
    def __getSerial(self):
        if(self.ser == None):
            self.ser = serial.Serial(2)
            self.ser.setTimeout(0.5)
            print "Communicating through " + self.ser.portstr
        return self.ser

    def __initSaintRaphHouse(self):
        house = House.initSaintRaph()
        
        self.lightCommands = [] 
        for lightModel in house.lightModels:
            self.lightCommands.append(LightCommand(lightModel, 
                                               self.__getSerial()))    
        
        self.shutterCommands = []
        for shutterModel in house.shutterModels:
            self.shutterCommands.append(ShutterCommand(shutterModel, 
                                               self.__getSerial()))  
    
    @QtCore.pyqtSlot()
    def __switchLight(self):
        sender = self.sender()
        for lightButton in self.lightButtons:
            if(lightButton[1] == sender):
                lightButton[0].setOn()
                return
            if(lightButton[2] == sender):
                lightButton[0].setOff()
                return
            
    @QtCore.pyqtSlot()
    def __setDimmer(self):
        pass
#        sender = self.sender()
#        for slider in self.lightSliders:
#            if(slider[1] == sender):
#                slider[0].setDimmerIntensity(slider[1].value())
#                return
                
    @QtCore.pyqtSlot()
    def __switchShutter(self):
        sender = self.sender()
        for shutterButton in self.shutterButtons:
            if(shutterButton[1] == sender):
                shutterButton[0].setUp()
                return
            if(shutterButton[2] == sender):
                shutterButton[0].setStop()
                return
            if(shutterButton[3] == sender):
                shutterButton[0].setDown()
                return
        
    @QtCore.pyqtSlot()
    def aboutThisApp(self):
        QtGui.QMessageBox.about(self, self.tr("About"), self.tr("This application allows you to turn on and off lights !!!"))

    @QtCore.pyqtSlot()
    def __sendCommand(self):
        print "Sending command: " + self.cmdEdit.text()
        self.ser.write(self.cmdEdit.text())
        self.ser.flushOutput()


