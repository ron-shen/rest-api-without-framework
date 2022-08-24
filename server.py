from http.server import HTTPServer, BaseHTTPRequestHandler
import json
import re

with open('./users.json') as datafile:
    users = json.load(datafile)

def get_all_users(*args):
    return json.dumps(users).encode()

def get_user(*args):
    path = args[0]
    id = path.split("/")[-2]
    try:
        user = users[id]
        return json.dumps(user).encode()
    except KeyError:
        raise KeyError("User doesn't exist")

url_path = [["^/users+/$", get_all_users], ["^/users/+\d+/$", get_user]]


class ServiceHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        function = None
        for path, fun in url_path:
            if re.match(path, self.path):
                function = fun
                break
        try:
            data = function(self.path)
            self.send_response(200)
            self.send_header('Content-type','text/json')
            self.send_header('Content-Length',999)
            self.end_headers()
            self.wfile.write(data)
        except Exception as error:
            print(repr(error))
            self.send_response(404)
            self.end_headers()


    def do_POST(self):
        pass

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