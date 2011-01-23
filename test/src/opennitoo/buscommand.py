'''
Created on 22 janv. 2011

@author: epot
This module handles bus command messages
'''

class BusCommand():
    '''
    classdocs
    '''


    def __init__(self, who, what, where):
        '''
        Constructor
        '''
        self.who = who
        self.what = what
        self.where = where
        
    def getMessage(self):
        strMsg = "*" + str(self.who) + "*" + str(self.what) + "*" + str(self.where) + "##"
        print "getMessage= \"" + strMsg + "\""
        return strMsg
        