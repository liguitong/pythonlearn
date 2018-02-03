# _*_ coding:utf-8 _*_
''' simple http server to run python web'''
from http.server import HTTPServer,CGIHTTPRequestHandler

port = 8080
httpd = HTTPServer(('',port),CGIHTTPRequestHandler)
print('Starting simple_httpd on port:' + str(httpd.server_port))
httpd.serve_forever()
