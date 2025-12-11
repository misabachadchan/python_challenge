import json

data = {
    "name": "John",
    "age": 22,
    "email": "john@example.com"
}

with open("info.json", "w") as f:
    json.dump(data, f, indent=4)

with open("info.json", "r") as f:
    print(json.load(f))
