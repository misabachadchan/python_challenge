import json

with open("info.json", "r") as f:
    data = json.load(f)

data["city"] = "Bengaluru"

with open("info.json", "w") as f:
    json.dump(data, f, indent=4)
