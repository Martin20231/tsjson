import json

with open ('accounts.json') as file:
    data = json.load(file)

print(json.dumps(data, indent=4))
