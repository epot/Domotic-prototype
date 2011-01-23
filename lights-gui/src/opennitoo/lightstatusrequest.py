'''
Created on 22 janv. 2011

@author: epot
'''

from statusrequest import StatusRequest

class LightStatusRequest(StatusRequest):
    '''
    classdocs
    '''
    whoValue = 1

    def __init__(self):
        '''
        Constructor
        '''
        StatusRequest.__init__(self, LightStatusRequest.whoValue, "#0")