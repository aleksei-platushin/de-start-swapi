import requests
import os


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

    def get_sw_info(self, sw_type: str):
        response = self.get(sw_type)
        if response:
            return str(response.text)
        return ''


def save_sw_data():
    sw = SWRequester('https://swapi.dev/api/')
    categories = sw.get_sw_categories()
    os.makedirs('data', exist_ok=True)
    for category in categories:
        data = sw.get_sw_info(category)
        if data:
            file_path = os.path.join('data', f'{category}.txt')
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(f'{data}\n')


if __name__ == '__main__':
    save_sw_data()
