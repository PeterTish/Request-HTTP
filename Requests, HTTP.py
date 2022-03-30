import requests
from pprint import pprint
# Task №1 Поиск самого умного супергероя




def search_superhero():
    '''Функция обращается к сайту, возвращает список json файл каждого супергероя из запроса'''
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



def smartest_superhero(search_superhero):
    '''
    Функция принимает функцию search_superhero (json файл каждого супергероя из запроса),
    составляет словарь имя : интеллект, словарь добавляется в список, список сортируется
    по возрастанию по величине интеллекта супергероя
    '''
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





# Task №2 Добавление файла на Яндекс Диск

import yadisk

# y = yadisk.YaDisk(token='')
# y.upload('Test.docx', '/Test.docx')

class YaUploader:
    def __init__(self, token: str):
        self.token = token

    def get_headers(self):
        return {
            'Content-Type': 'application/json',
            'Authorization': f'OAuth {self.token}'
        }

    def get_upload_link(self, disk_file_path):
        upload_url = "https://cloud-api.yandex.net/v1/disk/resources/upload"
        headers = self.get_headers()
        params = {"path": disk_file_path, "overwrite": "true"}
        response = requests.get(upload_url, headers=headers, params=params)
        pprint(response.json())
        return response.json()

    def upload_file(self, file_path: str):
        """Метод загружает файлы по списку file_list на яндекс диск"""
        href = self.get_upload_link(disk_file_path=path_to_file).get("href", "")
        response = requests.put(href, data=open(file_name, 'rb'))
        response.raise_for_status()
        if response.status_code == 201:
            print("Success")

# if __name__ == '__main__':
#     file_name = 'Test.docx'
#     path_to_file = 'Test.docx'
#     token = 'AQAAAABesawkAADLW4fcGKQ07URMrcKMoc7ae-E'
#     uploader = YaUploader(token)
#     result = uploader.upload_file(path_to_file)



# Task №3 Все вопросы за 2 дня по тэг Python

url = 'https://stackoverflow.com/'
params_dict = {'tag' : 'Python', 'date' : {'start' : '2022-03-28', 'end' : '2022-03-29'}}


response = requests.get(url, params=params_dict)
pprint(response.json())
