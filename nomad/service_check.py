import requests

def check_service_availability():
    response = requests.get("http://localhost:4646")
    return response.status_code == 200
