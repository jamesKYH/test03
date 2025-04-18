import requests
import json
from datetime import datetime

now = datetime.now()
minute = now.minute
todo_id = (minute + 1) % 60 or 1
url = f"https://jsonplaceholder.typicode.com/todos/{todo_id}"

response = requests.get(url)
data = response.json()

with open("test.json", "w") as f:
    json.dump(data, f, indent=2)

print(f"✅ Fetched todo ID {todo_id} and saved to test.json")