'''
Created on 23 janv. 2011

@author: epot
'''
from opennitoo import lightbuscommand

class LightCommand():
    '''
    This class allows the manipulation of a given light or group of light.
    '''

    def __init__(self, light, serialCom):
        '''
        Constructor
        '''
        self.light = light
        self.serialCom = serialCom
        
    def setOn(self):
        self.__switchLights(True)
        
    def setOff(self):
        self.__switchLights(False)
        
    def getLight(self):
        return self.light
        
    def __switchLights(self, on):
        cmd = lightbuscommand.LightBusCommand(on, self.light.getId())
        self.serialCom.write(cmd.getMessage())