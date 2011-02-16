'''
Created on 16 fevr. 2011

@author: Popotelle
'''

from model.lightmodel import LightModel
from model.shuttermodel import ShutterModel

class House():
    '''
    classdocs
    '''


    def __init__(self):
        '''
        Constructor
        '''
        self.lightModels = [] 
        self.shutterModels = []
    
    @staticmethod
    def initSaintRaph():
        house = House()
        tvModel = LightModel("TV", 11430977)
        #tvModel.setDimmerId(11430978)
        house.lightModels.append(tvModel)
        house.lightModels.append(LightModel("Dining Room", 11431009))
        house.lightModels.append(LightModel("Entrance", 12407681))
        house.lightModels.append(LightModel("Kitchen", 12407137))
        house.lightModels.append(LightModel("Rear kitchen", 12407745))        
        
        house.shutterModels.append(ShutterModel("Kitchen", 12742113))
        house.shutterModels.append(ShutterModel("Living Room 1", 12741985))
        house.shutterModels.append(ShutterModel("Living Room 2", 12742273)) 
        return house
