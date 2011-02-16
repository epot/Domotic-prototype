'''
Created on 23 janv. 2011

@author: epot
'''

class ShutterModel():
    '''
    This class is used to define a shutter in your house.
    TODO: add localization information
    '''


    def __init__(self, name, id):
        '''
        Constructor
        '''
        self.name = name
        self.id = id
    
    def getName(self):
        '''
        get current name
        '''
        return self.name
    
    def getId(self):
        '''
        get light id (used to send command)
        '''
        return self.id
        