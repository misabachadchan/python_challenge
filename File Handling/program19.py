import json

with open("average.json", "r") as f:
    data = json.load(f)

scores = data["scores"]
avg = sum(scores) / len(scores)

print("Average:", avg)
