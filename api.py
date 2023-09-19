import requests
import json

URL = "http://data.cityofnewyork.us/resource/uvks-tn5n.json"
response = requests.get(URL)
json_content = json.loads(response.text)

print(json.dumps(json_content, indent=4))