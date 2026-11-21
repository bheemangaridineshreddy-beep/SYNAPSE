import requests

url = "http://127.0.0.1:5000/scan_qr"

data = {
    "roll_number": "STU001"
}

response = requests.post(url, json=data)

print(response.status_code)
print(response.json())