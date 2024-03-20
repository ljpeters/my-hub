import http.client
import json

body = '{"method":"setPilot","params":{"state":true}}'
headers = {'Content-type': 'application/json'}

connection = http.client.HTTPConnection('localhost', 8000, timeout=10)
connection.request(
    "POST",
    "/sendUDP/192.168.68.103/on?port=38899",
    json.dumps(body),
    headers
)
# connection.request("GET", "/")
response = connection.getresponse()
print("Status: {} and reason: {}".format(response.status, response.reason))
print(response.msg)
print(response.read().decode())
connection.close()