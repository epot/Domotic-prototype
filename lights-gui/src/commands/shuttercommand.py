'''
Created on 23 janv. 2011

@author: epot
'''
from opennitoo.automationbuscommand import AutomationBusCommand

class ShutterCommand():
    '''
    This class allows the manipulation of a given shutter.
    '''

    def __init__(self, shutter, serialCom):
        '''
        Constructor
        '''
        self.shutter = shutter
        self.serialCom = serialCom
        
    def setUp(self):
        self.__switchShutter(AutomationBusCommand.UP)
        
    def setDown(self):
        self.__switchShutter(AutomationBusCommand.DOWN)
        
    def setStop(self):
        self.__switchShutter(AutomationBusCommand.STOP)
   
    def getShutter(self):
        return self.shutter
        
    def __switchShutter(self, val):
        cmd = AutomationBusCommand(val, self.shutter.getId())
        self.serialCom.write(cmd.getMessage())