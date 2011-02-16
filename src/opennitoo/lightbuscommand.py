'''
Created on 22 janv. 2011

@author: epot
'''

from buscommand import BusCommand

class LightBusCommand(BusCommand):
    '''
    classdocs
    '''
    whoValue = "1"

    def __init__(self, on, where):
        '''
        Constructor
        '''
        onValue = 1 if on else 0
        BusCommand.__init__(self, LightBusCommand.whoValue, onValue, "#" + str(where) + "")
        
    def getStartScenario(self, dimmerId):
        strMsg = "*25*11*" + str(dimmerId) + "##"
        print "getStartScenario= \"" + strMsg + "\""
        return strMsg
    
    def getDimmerMessage(self, intensity):
        strMsg = "*#1*" + self.where + "*#10*" + str(intensity) + "*1##"
        print "getDimmerMessage= \"" + strMsg + "\""
        return strMsg
