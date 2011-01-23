'''
Created on 22 janv. 2011

@author: epot
This module handles status request messages
'''

class StatusRequest():
    '''
    classdocs
    '''


    def __init__(self, who, where):
        '''
        Constructor
        '''
        self.who = who
        self.where = where
        
    def getMessage(self):
        return "*#" + str(self.who) + "*" + str(self.where) + ""
        