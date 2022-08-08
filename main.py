import requests
import json

parload = {'quert': 'Cyrus'}
response = requests.get("https://api.urbanathletes.co.id/fitness/v1/branch")
# print(response.json())
# print(json.dumps(response.json()))

branchData = response.json()['data']['rows']

# print(branchData)
print(json.dumps(branchData))
for branch in branchData:
  print(branch['name'])