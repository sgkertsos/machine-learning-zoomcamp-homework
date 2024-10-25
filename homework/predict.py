import requests

url = 'http://localhost:9696/score'

client_id = 'xyx-123'

client = {
    "job": "student",
    "duration": 280,
    "poutcome": "failure"
}

response = requests.post(url, json=client).json()

print(response)