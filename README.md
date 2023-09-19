## Authers
1. Yegon
2. Griffins
---
## Requirements

- Python 3.8 and above.
- The `requests` library (install using `pip install requests` if not already installed)
----
## Usage

1. Clone or download this repository to your local machine.
 #### git clone https://github.com/KIPROTYCH/Group-Z.git

2. Open a terminal and navigate to the directory containing the above directory.

3. Run the script by executing the following command:
#### python3 api.py

----
## Codes Description:
----
### $ import requests 
This line imports the requests library for making HTTP requests to interact with web services and APIs.

### $ import json
This line imports the json module, which provides functions to encode and decode JSON data

### $ URL = "http://data.cityofnewyork.us/resource/uvks-tn5n.json"
This line defines a variable named URL and assigns it the value of the API endpoint URL.

### $ response = requests.get(URL)
This line sends an HTTP GET request to the URL specified in the URL variable using the requests.get() method. The response from the API is stored in the response variable.

### $ json_content = json.loads(response.text)
This line converts the JSON response from the API (which is stored in response.text) into a Python data structure. The json.loads() function is used to parse the JSON text, and the resulting Python data is stored in the json_content variable.

### $ print(json.dumps(json_content, indent=4))
This line prints the JSON data obtained from the API in a more human-readable format. It uses json.dumps() to serialize the Python data back into a JSON-formatted string, with an indentation of 4 spaces for better readability. The result is then printed to the console.

----