from http.server import HTTPServer, BaseHTTPRequestHandler, SimpleHTTPRequestHandler
import json
import time

with open('./users.json') as datafile:
    users = json.load(datafile)


class ServiceHandler(BaseHTTPRequestHandler):
    def do_GET(self): 
        #print(self.wfile.raw)
        #setting response header fields
        self.send_response(200)
        self.send_header('Content-type','text/json')
        #add a blank line to indicate end of header
        self.end_headers()
        print(type(self.wfile._sock))
        #message body
        self.wfile.write(json.dumps(users).encode())
        #self.wfile.write(json.dumps(users).encode())
        # print("requestline:", self.requestline)
        # print("raw_requestline:", self.raw_requestline)
        #print("headers:", self.headers)
        # print("command:", self.command)
        # print("path:", self.path)
        # print("request_version:", self.request_version)

    def do_POST(self):
        print("requestline:", self.requestline)
        print("raw_requestline:", self.raw_requestline)
        print("headers:", self.headers)
        print("command:", self.command)
        print("path:", self.path)
        print("request_version:", self.request_version)

    def do_PUT(self):
        pass

    def do_PATCH(self):
        pass

    def do_DELETE(self):
        pass



#Server Initialization
server = HTTPServer(('127.0.0.1',8080), ServiceHandler)
print("server started...")
server.serve_forever()