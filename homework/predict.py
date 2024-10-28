import requests

url = 'http://localhost:9696/score'

client_id = 'xyx-123'

client = {
    "job": "management",
    "duration": 400,
    "poutcome": "success"
}

response = requests.post(url, json=client).json()

print(response)