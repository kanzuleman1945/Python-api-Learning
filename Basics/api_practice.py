# This code demonstrates how to make a GET request to a public API using the requests library in Python.
# Impport Library
import requests
response = requests.get("https://jsonplaceholder.typicode.com/users/1")
# Check the status code of the response
print("status code:", response.status_code)
# Print the headers and the JSON data from the response
#print("headers:", response.headers)
data = response.json()
print(type(data))
#print(data)
print(data["name"])

# Output:
# 200

