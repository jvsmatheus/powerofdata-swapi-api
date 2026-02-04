import requests

BASE_URL = "https://swapi.dev/api"
TIMEOUT = 5

class SwapiClient:

    def get(self, resource: str):
        url = f"{BASE_URL}/{resource}/"
        response = requests.get(url, timeout=TIMEOUT)

        response.raise_for_status()
        return response.json()