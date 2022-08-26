from http.server import HTTPServer, BaseHTTPRequestHandler
import json
import re
from copy import deepcopy

with open('./users.json') as datafile:
    users = json.load(datafile)

def get_all_users(*args):
    return json.dumps(users).encode()

def get_user(*args):
    path = args[0]
    id = path.split("/")[-2]
    try:
        user = {id: users[id]}
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
            self.send_header("Content-type","text/json; charset=UTF-8")
            self.send_header("Content-Language", "en-US")
            self.send_header("Content-Length", len(data))
            self.end_headers()
            self.wfile.write(data)
        except Exception as error:
            print(repr(error))
            self.send_response(404)
            self.end_headers()


    def do_POST(self):
        if not self._valid_path():
            return

        data = self._read_data()
        id = str(len(users) + 1)
        data_dict = {}
        try:
            for key_val in data:
                key, value = key_val.split('=')
                data_dict[key] = value          
            users[id] = data_dict
            with open("./users.json",'w+') as file_data:
                json.dump(users, file_data)
            self.send_response(200)
            self.end_headers()    
        except ValueError as error:
            print(repr(error))
            self.send_response(400)
            self.end_headers()            


    def do_PUT(self):
        if not self._valid_path():
            return
        
        data = self._read_data()
        id = data[0]
        try:
            user = deepcopy(users[id])
            if len(data) - 1 != len(user):
                raise ValueError(f"Number of given attributes don't match to attributes in id {id}...")
            for i in range(1, len(data)):
                key, value = data[i].split('=')
                if key not in user:
                    raise KeyError(f"Key {key} doesn't exist...")
                user[key] = value
            with open("./users.json",'w+') as file_data:
                users[id] = user
                json.dump(users, file_data)
            self.send_response(200)
            self.end_headers()           
        except Exception as error:
            print(repr(error))
            self.send_response(400, error)
            self.end_headers()


    def do_PATCH(self):
        if not self._valid_path():
            return

        data = self._read_data()
        id = data[0]
        try:
            user = deepcopy(users[id])
            for i in range(1, len(data)):
                key, value = data[i].split('=')
                if key not in user:
                    raise KeyError(f"Key {key} doesn't exist...")
                user[key] = value
            with open("./users.json",'w+') as file_data:
                users[id] = user
                json.dump(users, file_data)
            self.send_response(200)
            self.end_headers() 
        except KeyError as error:
            print(repr(error))
            self.send_response(400, error)
            self.end_headers()


    def do_DELETE(self):
        if not self._valid_path():
            return

        data = self._read_data()
        id = data[0]
        try:
            del users[id]
            with open("./users.json",'w+') as file_data:
                json.dump(users, file_data)
            self.send_response(200)
            self.end_headers()       
        except KeyError as error:
            print(repr(error))
            self.send_response(400, f"key {id} doesn't exist")
            self.end_headers()


    def _valid_path(self):
        if self.path != "/users/":
            self.send_response(404)
            self.end_headers()
            return False

        return True


    def _read_data(self):
        length = int(self.headers["Content-Length"])
        data = self.rfile.read(length).decode()
        data = re.split('[.&]', data)
        return data


#Server Initialization
server = HTTPServer(('127.0.0.1',8080), ServiceHandler)
print("server started...")
server.serve_forever()