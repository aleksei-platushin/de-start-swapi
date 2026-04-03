# swapi.py
import requests
# from urllib3.exceptions import InsecureRequestWarning
# requests.packages.urllib3.disable_warnings(category=InsecureRequestWarning)


class APIRequester:
    def __init__(self, base_url: str):
        self.base_url = base_url

    def get(self, endpoint=''):
        try:
            url = f'{self.base_url}{endpoint}'
            response = requests.get(url)
            response.raise_for_status()
            return response
        except requests.RequestException as e:
            print(f'Ошибка при выполнении запроса: {e}')
            return None


class SWRequester(APIRequester):
    def get_sw_categories(self) -> list:
        response = self.get()
        if response:
            categories_data = response.json()
        return list(categories_data.keys())

    def get_sw_info(self, sw_type):
        response = self.get(sw_type)
        if response:
            return response.text
        return ''
    
    def save_data():
        pass


sw = SWRequester('https://swapi.dev/api/')
categories = sw.get_sw_categories()
print(f'Доступные категории: {categories}')
info = sw.get_sw_info(categories[0])
print(info)
