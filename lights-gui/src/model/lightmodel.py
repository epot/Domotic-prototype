'''
Created on 23 janv. 2011

@author: epot
'''

class LightModel():
    '''
    This class is used to define a light in your appartment.
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
        