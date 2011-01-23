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
        self.lights = []
        self.lights.append(light)
        self.serialCom = serialCom
        
    def addLight(self, light):
        self.lights.append(light)
        
    def setOn(self):
        self.__switchLights(True)
        
    def setOff(self):
        self.__switchLights(False)
        
    def __switchLights(self, on):
        for light in self.lights:
            cmd = lightbuscommand.LightBusCommand(on, light.getId())
            self.serialCom.write(cmd.getMessage())