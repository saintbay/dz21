import requests
import os
import requests

url = "https://jsonplaceholder.typicode.com/posts"
response = requests.get(url)
data = response.json()

output_folder = "json_files"
os.makedirs(output_folder, exist_ok=True)

for i, item in enumerate(data):
    with open(os.path.join(output_folder, f"file_{i}.json"), "w") as file:
        file.write(str(item))
