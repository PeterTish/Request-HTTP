import requests
from pprint import pprint


# Task №1 Поиск самого умного супергероя
def most_intelligence():
    url = 'https://superheroapi.com/api/2619421814940190/search/'
    superheroes = [{'name': 'hulk'}, {'name': 'captain_america'}, {'name': 'thanos'}]
    s = []
    for hero in superheroes:
        res = requests.get(url + hero['name'])
        hero['intelligence'] = int(res.json()['results'][0]['powerstats']['intelligence'])
        s.append(hero)
        sorted_list = sorted(s, key=lambda hero: hero['intelligence'])
    print(f" The most intelligence superhero is {sorted_list[-1]['name']}")
    return sorted_list


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

if __name__ == '__main__':
    most_intelligence()
    file_name = 'Test.docx'
    path_to_file = 'Test.docx'
    token = 'AQAAAABesawkAADLW4fcGKQ07URMrcKMoc7ae-E'
    uploader = YaUploader(token)
    result = uploader.upload_file(path_to_file)



# /2.3/questions?fromdate=1648425600&todate=1648598400&order=desc&sort=activity&tagged=python&site=stackoverflow
# Task №3 Все вопросы за 2 дня по тэг Python
import json

url = 'https://api.stackexchange.com/2.3/questions'
params_dict = {'fromdate':1648425600, 'todate':1648598400, 'order':'desc', 'sort':'activity', 'tagged' : 'python', 'site':'stackoverflow'}

response = requests.get(url, params=params_dict)
# pprint(response.json())


# import requests
# import time
# from datetime import datetime, timedelta
#
# class StackOverFlow:
# def init(self):
# self.tags = ['python']
# now = datetime.now()
# data = now - timedelta(days=2)
# self.from_date = int(data.timestamp())
# self.questions = []

# def load_info(self, number_of_pages: int = 30):
#     """Загружает топ самых активно обсуждаемых вопросов на Stack Overflow за последние 2 дня.
#     В качестве параметра принимает колличество вопросов, возвращаемое методом (по умолчинию 30)"""
#     url = 'https://api.stackexchange.com/2.2/questions'
#     params = {
#         'pagesize': str(number_of_pages),
#         'fromdate': str(self.from_date),
#         'order': 'desc',
#         'sort': 'activity',
#         'tagged': ';'.join(self.tags),
#         'site': 'stackoverflow'
#     }
#     reply = requests.get(url, params=params).json()
#     self.questions = [
#         {
#             'title': item['title'],
#             'link': item['link'],
#             'tags': item['tags'],
#             'creation_date': time.ctime(item['creation_date'])
#         }
#         for item in reply['items']
#     ]
#     self.questions.sort(key=lambda x: x['creation_date'])
#     return reply
#
# def print_questions(self):
#     """Выводит на экран соновную информацию прочитанных ранее вопросов"""
#     dividing_line = f'__________________________________________\n'
#     print(dividing_line)
#     for item in self.questions:
#         print(f'Зааголовок: {item["title"]}\n'
#               f'Ссылка: {item["link"]}\n'
#               f'Тэги: {", ".join(item["tags"])}\n'
#               f'Время публикации: {item["creation_date"]}\n'
#               f'{dividing_line}')
#     print(f'Топ {len(self.questions)} самых обсуждаемых вопросов за последние 2 дня на Stack Overflow\n'
#           f'(Отсортерованно по дате)')
# def main():
# stackoverflow = StackOverFlow()
# stackoverflow.loadinfo(100)
# stackoverflow.print_questions()