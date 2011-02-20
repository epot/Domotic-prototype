'''
Created on 13 fevr. 2011

@author: Popotelle
'''

import cgi
import httplib, urllib
import logging

from google.appengine.api import users
from google.appengine.ext import webapp
from google.appengine.ext.webapp.util import run_wsgi_app
from google.appengine.ext import db
import os
from google.appengine.ext.webapp import template

from houses.house import House

IP = '127.0.0.1'
PORT = 8000
house = House.initSaintRaph()

class MainPage(webapp.RequestHandler):
    def get(self):
        if users.get_current_user():
            url = users.create_logout_url(self.request.uri)
            url_linktext = 'Logout'
        else:
            url = users.create_login_url(self.request.uri)
            url_linktext = 'Login'

        template_values = {
            'url': url,
            'url_linktext': url_linktext,
            'house': house
        }

        path = os.path.join(os.path.dirname(__file__), os.path.join('webapp','index.html'))
        self.response.out.write(template.render(path, template_values))

class SwitchLightCommand(webapp.RequestHandler):
    def post(self):
        try:
            logging.info(self.request.arguments())
            logging.info(self.request.get('id'))
            logging.info("on/off= " + self.request.get('action'))
            logging.info("id= " + self.request.get('id'))
            headers = {"Content-type": "application/switchLight",
                       "Accept": "text/plain",
                       "LightId": self.request.get('id'),
                       "On" : self.request.get('action')}
            conn = httplib.HTTPConnection(IP, PORT)
            conn.request("POST", "/cgi-bin/query", "", headers)
            response = conn.getresponse()
            conn.close()
        except:
            pass
        self.redirect('/')
        


application = webapp.WSGIApplication(
                                     [('/', MainPage),
                                      ('/switchLightCommand', SwitchLightCommand)],
                                     debug=True)

def main():
    httpServ = httplib.HTTPConnection("127.0.0.1", 80)
    httpServ.connect()
    run_wsgi_app(application)

if __name__ == "__main__":
    main()