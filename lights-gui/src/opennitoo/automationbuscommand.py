'''
Created on 22 janv. 2011

@author: patt
'''

from buscommand import BusCommand

class AutomationBusCommand(BusCommand):
    '''
    classdocs
    '''
    whoValue = "2"
    STOP = 0
    UP = 1
    DOWN = 2

    def __init__(self, val, where):
        '''
        Constructor
        '''
        BusCommand.__init__(self, AutomationBusCommand.whoValue, val, "#" + str(where) + "")