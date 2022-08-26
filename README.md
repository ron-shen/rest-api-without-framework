# rest-api-without-framework
Learn REST API

# Methods
```
Get all users: curl -X GET 127.0.0.1:8080/users/
Get a specific user: curl -X GET 127.0.0.1:8080/users/{id}/
Create a new user: curl -X POST -d "key=value" 127.0.0.1:8080/users/
Update an existing user (whole update to the resource): curl -X PUT -d "id.key=value" 127.0.0.1:8080/users/
Update an existing user (partial update to the resource): curl -X PATCH -d "id.key=value" 127.0.0.1:8080/users/
Delete an existing user: curl -X DELETE -d "id" 127.0.0.1:8080/users/
```

# Examples
```
curl -X GET 127.0.0.1:8080/users/
curl -X GET 127.0.0.1:8080/users/1/
curl -X POST -d "username=Kobe&location=Canada&company=ABC" 127.0.0.1:8080/users/
curl -X PUT -d "1.username=Tom&location=US&role=Sales" 127.0.0.1:8080/users/
curl -X PATCH -d "1.role=Manager" 127.0.0.1:8080/users/
curl -X DELETE -d "1" 127.0.0.1:8080/users/
```

# HTTP headers
Request headers: Can be used in an HTTP request to provide information about the request context. Clients can add some header fields like Accept and Host

Reponse headers: Can be used in an HTTP response and that doesn't relate to the content of the message. Response header fields like Age, Location or Server are used to give a more detailed context of the response.

Representation headers: Provide fields describing how to interpret the representation data enclosed in the payload body. e.g. Content-Encoding, Content-Language, Content-Type, Content-Length...

HTTP request message
--- | 
Request Line |
Headers | 
CRLF (indicate the end of header) |
Message Body |

HTTP response message
--- | 
Status Line |
Headers | 
CRLF (indicate the end of header) |
Message Body |

reference: https://www.rfc-editor.org/rfc/rfc9110.html#representation.data.and.metadata



