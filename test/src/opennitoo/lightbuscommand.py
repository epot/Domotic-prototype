'''
Created on 22 janv. 2011

@author: patt
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