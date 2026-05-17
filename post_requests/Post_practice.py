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
data = response.json()
print(data)