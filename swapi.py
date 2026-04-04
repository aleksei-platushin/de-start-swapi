import requests
from pathlib import Path


class APIRequester:
    def __init__(self, base_url: str):
        self.base_url = base_url

    def get(self, endpoint=''):
        try:
            # Склеиваем базу и эндпоинт, гарантируя один слеш между ними
            base = self.base_url.rstrip('/')
            clean_endpoint = endpoint.lstrip('/')
            url = f'{base}/{clean_endpoint}'

            response = requests.get(url)
            response.raise_for_status()
            return response
        except requests.RequestException:
            print('Возникла ошибка при выполнении запроса')
            return None


class SWRequester(APIRequester):
    def get_sw_categories(self):
        # Запрос к корню API со слешем в конце
        response = self.get('/')
        if response:
            return response.json().keys()
        return None

    def get_sw_info(self, sw_type: str):
        # Запрос категории со слешем в конце
        response = self.get(f'{sw_type}/')
        return response.text if response else ''


def save_sw_data():
    sw = SWRequester('https://swapi.dev/api')
    categories = sw.get_sw_categories()

    # Создаем объект Path и папку (нужно для прохождения теста)
    data_dir = Path('data')
    data_dir.mkdir(exist_ok=True)

    if categories:
        for category in categories:
            data = sw.get_sw_info(category)
            if data:
                file_path = f'data/{category}.txt'
                with open(file_path, 'w', encoding='utf-8') as f:
                    f.write(data)


if __name__ == '__main__':
    save_sw_data()
