'''
Created on 23 janv. 2011

@author: epot
'''
from opennitoo.lightbuscommand import LightBusCommand

class LightCommand():
    '''
    This class allows the manipulation of a given light.
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
    
#    def setDimmerIntensity(self, intensity):
#        if(self.light.getDimmerId() == None):
#            return
#        cmd = LightBusCommand(intensity, self.light.getId())
#        self.serialCom.write(cmd.getDimmerMessage(intensity))
#        self.serialCom.write(cmd.getStartScenario(self.light.getDimmerId()))
        
    def __switchLights(self, on):
        cmd = LightBusCommand(on, self.light.getId())
        self.serialCom.write(cmd.getMessage())