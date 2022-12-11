import requests
from datetime import datetime,date,timedelta
import os

class Task1():
    """
    Задача №1
        Кто самый умный супергерой?
        Есть API по информации о супергероях с информацией по всем супергероям. Нужно определить кто самый умный(intelligence)
        из трех супергероев- Hulk, Captain America, Thanos.
    """
    def __init__(self, url='https://akabab.github.io/superhero-api/api/all.json'):
        self.url = url
        self.full_statistic = None
    def refresh_hero_statistic(self):
        r = requests.get(self.url)
        if r.status_code==200:
            self.full_statistic = r.json()
        return r.status_code
    def get_most_intelligence(self, heroes=['Hulk', 'Captain America', 'Thanos']):
        out = []
        if self.full_statistic is None:
            self.refresh_hero_statistic()
        for hero in self.full_statistic:
            if hero['name'] in heroes:
                out.append((hero['name'],hero['powerstats'].get('intelligence')))
        return sorted(out, key=lambda hero_name: hero_name[1], reverse=True)[0][0]
class YaUploader:
    """
    Задача №2
        У Яндекс.Диска есть очень удобное и простое API. Для описания всех его методов существует Полигон.
        Нужно написать программу, которая принимает на вход путь до файла на компьютере и сохраняет на Яндекс.Диск
        с таким же именем.

        Все ответы приходят в формате json;
        Загрузка файла по ссылке происходит с помощью метода put и передачи туда данных;
        Токен можно получить кликнув на полигоне на кнопку "Получить OAuth-токен".
        HOST: https://cloud-api.yandex.net:443

        Важно: Токен публиковать в github не нужно, переменную для токена нужно оставить пустой!

        Шаблон для программы
            class YaUploader:
                def __init__(self, token: str):
                    self.token = token

                def upload(self, file_path: str):
                    '''Метод загружает файлы по списку file_list на яндекс диск'''
                    # Тут ваша логика
                    # Функция может ничего не возвращать


            if __name__ == '__main__':
                # Получить путь к загружаемому файлу и токен от пользователя
                path_to_file = ...
                token = ...
                uploader = YaUploader(token)
                result = uploader.upload(path_to_file)
    """

    base_url = 'https://cloud-api.yandex.net/v1/disk'
    def __init__(self, token: str):
        self.session = requests.session()
        self.session.headers = {'Accept': 'application/json',
                       'Authorization': 'OAuth '+ token}

    def get_files(self,path=''):
        r = self.session.get(f'{self.base_url}/resources/files')
        print(r.status_code)
        print(r.text)


    def upload(self, file_path: str):
        file_url = self.session.get(f'{self.base_url}/resources/upload?path={file_path}&overwrite=true').json()
        with open(file_path,'rb') as file:
            restp = self.session.post(file_url['href'], files={'file': file})
        return restp.status_code

class Task3:
    '''
    *Задача №3(необязательная)
        Самый важный сайт для программистов это stackoverflow. И у него тоже есть API Нужно написать программу,
        которая выводит все вопросы за последние два дня и содержит тэг 'Python'. Для этого задания токен не требуется.
    '''
    base_url = 'https://api.stackexchange.com/2.3/search'
    #https://api.stackexchange.com/2.3/search?fromdate=1670544000&order=desc&sort=activity&tagged=Python&site=stackoverflow
    def __init__(self):
        pass

    def __date__(self,time_delta):
        pass
    def get_questions(self,tags=['python'],time_delta=0):
        pass

if __name__=="__main__":

    #task1 = Task1()
    #print(task1.get_most_intelligence())

    # Task#2
    '''path_to_file = "homework.py"
    token = os.getenv('token')
    uploader = YaUploader(token)
    uploader.upload(path_to_file)'''

    #Task3
    dt = datetime.today() - timedelta(days=2)
    print(dt.timestamp())






