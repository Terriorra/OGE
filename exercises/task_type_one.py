import os
import sys
from random import choice
from random import sample


def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    base_path = getattr(sys, '_MEIPASS', os.path.dirname(os.path.abspath(__file__)))
    return os.path.join(base_path, relative_path)


def create_dict(words: list[str]) -> dict:
    '''
    Создать словарь по длине слов
    :param words: список слов
    :return: словарь
    '''
    dict_new = {}
    for word in words:
        if len(word) not in dict_new:
            dict_new[len(word)] = [word]
        else:
            dict_new[len(word)].append(word)

    return dict_new

###################################
# Загрузка данных
###################################


path = resource_path('city')

with open(path, 'r', encoding='utf-8') as f:
    city = f.read().split('\n')

path = resource_path('rivers')

with open(path, 'r', encoding='utf-8') as f:
    rivers = f.read().split('\n')

path = resource_path('mountains')

with open(path, 'r', encoding='utf-8') as f:
    mountains = f.read().split('\n')

path = resource_path('lakes')

with open(path, 'r', encoding='utf-8') as f:
    lakes = f.read().split('\n')

###################################
# Создание словарей
###################################
dict_city = create_dict(city)
dict_river = create_dict(rivers)
dict_mountain = create_dict(mountains)
dict_lakes = create_dict(lakes)

###################################
# Создание заданий
###################################

# Оценивать объём памяти, необходимый для хранения текстовых данных
# Количественные параметры информационных объектов

codind = [[['Windows-1251', 'КОИ-8', 'UTF-8'], ['8 битами', '1 байтом']],
          [['Unicode', 'UTF-16'], ['16 битами', '2 байтами']],
          [['UTF-32'], ['32 битами', '4 байтами']]]

dict_list = [dict_city,
             dict_river,
             dict_mountain,
             dict_lakes]

def create_task():
    dict_choice = choice([0, 1, 2, 3])  # выберем словарь
    coding_choice = choice([0, 1, 2])  # выберем кодировку

    # получим словарь
    dict_now = dict_list[dict_choice]
    # получим список длины слов
    keys_list = list(dict_now.keys())
    keys_list = sample(keys_list, choice(range(4, min(6, len(keys_list)))))
    # получим слова для предложения
    word = [choice(dict_now[i]) for i in keys_list]

    # Выберем ответ
    ant = choice(word)
    weight = (len(ant) + 2) * [8, 16, 32][coding_choice]
    weight = [f'{weight} бит', f'{weight // 8} байт']

    # составить предложение
    sentense = f"{', '.join(word)} — {['города', 'реки', 'горные вершины', 'озёра'][dict_choice]} России."

    ask = (f'В кодировке {choice(codind[coding_choice][0])} каждый символ кодируется'
           f' {choice(codind[coding_choice][1])}. Ученик написал текст (в нем нет лишних пробелов):\n\n'
           f'«{sentense}»\n\n'
           f'Ученик вычеркнул из списка одно из названий. Заодно он вычеркнул ставшие лишними запятые '
           f'и пробелы — два пробела не должны идти подряд. \nПри этом размер нового предложения в данной кодировке '
           f'оказался на {choice(weight)} меньше, чем размер исходного предложения. '
           f'\nНапишите в ответе вычеркнутое название.')


    return ask, ant
