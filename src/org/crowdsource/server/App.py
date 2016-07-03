__author__ = 'Juho'

from http.server import HTTPServer
from org.rlpp.server.RequestHandler import RequestHandler

class ServerApp :

    def __init__(self):
        print('Creating server.')

    def run(self, port, inputdir):
        server_address = ('', int(port))
        RequestHandler.set_inputdir(inputdir)
        httpd = HTTPServer(server_address, RequestHandler)
        print('Starting server at port %i' % (int(port)))
        httpd.serve_forever()
