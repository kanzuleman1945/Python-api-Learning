#Task 1: Print only the first user's:name, email

import requests
response = requests.get("https://jsonplaceholder.typicode.com/users/1")
print("status code:", response.status_code)
data = response.json()
print("name:", data["name"])
print("email:", data["email"])

#Task 2: print names of first 5 users using a loop.

response = requests.get("https://jsonplaceholder.typicode.com/users")
print("status code:", response.status_code)
data = response.json()
for i in range(5):
    print("name of user", i+1, ":", data[i]["name"])
    print("email of user", i+1, ":", data[i]["email"])

#Task 3 Change URL:https://jsonplaceholder.typicode.com/posts Print: title of first post

response = requests.get("https://jsonplaceholder.typicode.com/posts")
print("status code:", response.status_code)
data = response.json()
print(type(data))
print("title of first post:", data[0]["title"])