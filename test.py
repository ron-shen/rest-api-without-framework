import re

url_path = ["^/users+/$", 
            "^/users/+\d+/$"
            ]

# import re


test_string = "/users/"
result = re.match(url_path[0], test_string)
print(result)


