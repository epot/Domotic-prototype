'''
Created on 12 fevr. 2011

@author: Popotelle
'''

import BaseHTTPServer
import cgi

class MyHandler(BaseHTTPServer.BaseHTTPRequestHandler):
    def do_POST(self):
        print "allumer la lumiere " + str(self.headers.getheader('LightRequest'))

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
    
    