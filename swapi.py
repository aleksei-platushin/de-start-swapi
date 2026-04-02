# swapi.py
import requests


class APIRequester:
    def __init__(self, base_url: str):
        self.base_url = base_url

    def get(self) -> requests.Response:
        try:
            response = requests.get(self.base_url)
            response.raise_for_status()
            return response
        except requests.HTTPError as httperror:
            print(f"HTTP error occurred: {httperror}")
            return response
        except requests.RequestException as e:
            print(f'Ошибка запроса: {e}')

