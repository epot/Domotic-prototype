'''
Created on 13 fevr. 2011

@author: Popotelle
'''

import cgi
import httplib, urllib

from google.appengine.api import users
from google.appengine.ext import webapp
from google.appengine.ext.webapp.util import run_wsgi_app
from google.appengine.ext import db
import os
from google.appengine.ext.webapp import template

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
        }

        path = os.path.join(os.path.dirname(__file__), 'index.html')
        self.response.out.write(template.render(path, template_values))

class SendCommand(webapp.RequestHandler):
    def post(self):
        content = self.request.get('content')
        self.redirect('/')
#        params = urllib.urlencode({'spam': 1, 'eggs': 2, 'bacon': 0})  
        headers = {"Content-type": "application/lightstuff",
                   "Accept": "text/plain",
                   "LightRequest": content}
        conn = httplib.HTTPConnection('127.0.0.1', 8000)
        conn.request("POST", "/cgi-bin/query", "", headers)
        response = conn.getresponse()
        if response.status == httplib.OK:
            print "Output from CGI request"
            print response.read()
        conn.close()
        
application = webapp.WSGIApplication(
                                     [('/', MainPage),
                                      ('/sendCommand', SendCommand)],
                                     debug=True)

def main():
    httpServ = httplib.HTTPConnection("127.0.0.1", 80)
    httpServ.connect()
    run_wsgi_app(application)

if __name__ == "__main__":
    main()