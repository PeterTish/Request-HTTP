import requests
from pprint import pprint
# Task №1 Поиск самого умного супергероя

token = 2619421814940190


def search_superhero():
    superhero_list = []


    hulk = 'https://superheroapi.com/api/2619421814940190/search/Hulk'
    captain_america = 'https://superheroapi.com/api/2619421814940190/search/Captain America'
    thanos = 'https://superheroapi.com/api/2619421814940190/search/Thanos'

    response_hulk = requests.get(hulk)
    response_captain_america = requests.get(captain_america)
    response_thanos = requests.get(thanos)

    json_hulk = response_hulk.json()
    json_captain_america = response_captain_america.json()
    json_thanos = response_thanos.json()

    # pprint(json_hulk)
    # pprint(json_captain_america)
    # pprint(json_thanos)

    superhero_list.append(json_hulk['results'])
    superhero_list.append(json_captain_america['results'])
    superhero_list.append(json_thanos['results'])
    return superhero_list

# if __name__ == '__main__':
#     search_superhero()

def smartest_superhero(function):
    intelligence_dict = {}
    intelligence_list = []
    sorted_list = []
    for i in search_superhero():
        for a in i:
            name = a['name']
            intelligence = a['powerstats']['intelligence']

            if name != 'Red Hulk' and name != 'She-Hulk':
                intelligence_dict = {'name' : name, 'intelligence': int(intelligence)}
                intelligence_list.append(intelligence_dict)

                sorted_list = sorted(intelligence_list, key=lambda x: x['intelligence'])

    return f'Самый умный супергерой {sorted_list[-1]["name"]}'

# if __name__ == '__main__':
#     print(smartest_superhero(search_superhero))


# Task №2 Поиск самого умного супергероя

class YaUploader:
    def __init__(self, token: str):
        self.token = token

    def upload(self, file_path: str):
        """Метод загружает файлы по списку file_list на яндекс диск"""
        # Тут ваша логика
        # Функция может ничего не возвращать


if __name__ == '__main__':
    # Получить путь к загружаемому файлу и токен от пользователя
    path_to_file = ...
    token = ...
    uploader = YaUploader(token)
    result = uploader.upload(path_to_file)















