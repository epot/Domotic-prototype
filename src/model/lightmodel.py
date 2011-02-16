'''
Created on 23 janv. 2011

@author: epot
'''

class LightModel():
    '''
    This class is used to define a light in your house.
    TODO: add localization information
    '''


    def __init__(self, name, id):
        '''
        Constructor
        '''
        self.name = name
        self.id = id
        self.dimmerId = None
    
    def getName(self):
        '''
        get current name
        '''
        return self.name
    
    def setDimmerId(self, id):
        self.dimmerId = id
        
    def getDimmerId(self):
        return self.dimmerId
    
    def getId(self):
        '''
        get light id (used to send command)
        '''
        return self.id
        