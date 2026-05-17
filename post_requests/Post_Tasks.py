import requests
new_post = {
    "Name": "Kanzul",
    "body": "Python API practice",
    "userId": 1
}
response = requests.post(
    "https://jsonplaceholder.typicode.com/posts",
    json=new_post 
)
print("Status:", response.status_code)

### Task 1: Change title "title":"My First API Project" Print only title from response.

new_post["title"] = "My First API Project"
response = requests.post(
    "https://jsonplaceholder.typicode.com/posts",
    json=new_post
)
print("Title:", response.json()["title"])

### Task 2: Change:"userId":5 Print only: print(data["userId"])

new_post["userId"] = 5
response = requests.post(
    "https://jsonplaceholder.typicode.com/posts",
    json=new_post
)           
print("User ID:", response.json()["userId"])

###Task 3 Add a new field: "category":"Education" Print whole response.
new_post["category"] = "Education"
response = requests.post(
    "https://jsonplaceholder.typicode.com/posts",
    json=new_post
)
print("Whole Response:", response.json())


# Update data:
new_post["title"] = "Updated Title"
new_post["userId"] = 10
new_post["Name"] = "Eman"
new_post["body"] = "Learning API with python"
response = requests.post(
    "https://jsonplaceholder.typicode.com/posts",
    json=new_post
)
print("Status:", response.status_code)
print("Updated Response:", response.json())