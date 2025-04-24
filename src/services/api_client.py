import json
import httpx
from config import API_KEY, BASE_URL


class ApiClient:
    """Class that makes HTTP requests to the RetailCRM API"""

    def __init__(self):
        self.headers = {
            "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.0.0 Safari/537.36",
            "accept": "application/json",
            "X-API-KEY": API_KEY
        }

    def get(self, endpoint):
        with httpx.Client() as client:
            response = client.get(f"{BASE_URL}{endpoint}", headers=self.headers)
            return response

    def post(self, endpoint, data, key):
        form_data = {
            "apiKey": API_KEY,
            key: json.dumps(data)
        }
        headers = {
            "Content-Type": "application/x-www-form-urlencoded"
        }

        with httpx.Client() as client:
            response = client.post(f"{BASE_URL}{endpoint}", data=form_data, headers=headers)
            return response
