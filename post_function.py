import requests
import json

with open('text.json', 'r') as archivo:
    data = json.load(archivo)

result = requests.post("http://127.0.0.1:5000", json = data).json()

with open('result.json', 'w') as f:
    json.dump(result, f)