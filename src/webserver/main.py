'''
Created on 12 fevr. 2011

@author: Popotelle
'''

import BaseHTTPServer
import cgi
from houses.house import House
from opennitoo.lightbuscommand import LightBusCommand
import serial

house = House.initSaintRaph()
serialCom = serial.Serial(3)
serialCom.setTimeout(0.5)
print "Communicating through " + serialCom.portstr

class MyHandler(BaseHTTPServer.BaseHTTPRequestHandler):
    def do_POST(self):
        if(self.headers.getheader('Content-type') == "application/switchLight"):
            id = self.headers.getheader('LightId')
            on = self.headers.getheader('On')
            print "allumer la lumiere " + str(id)  + " " + str(on)
            cmd = LightBusCommand(1 if on == "1" else 0, id)
            try:
                serialCom.write(cmd.getMessage())
            except BaseException,e:
                print "error= " + str(e)
                
        self.send_response(200, 'OK')

def run(server_class=BaseHTTPServer.HTTPServer,
        handler_class=MyHandler):
    server_address = ('', 8000)
    httpd = server_class(server_address, handler_class)
    httpd.serve_forever()
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        httpd.server_close()



if __name__ == '__main__':
    print "server started"
    run()
    print "server stopped"
    
    