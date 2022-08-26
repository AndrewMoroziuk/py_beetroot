import os
from typing import List


def read_and_copy_text_by_sentence(text: str = None):
    name_res_file = 'Копія.txt'
    if text is None:
        print("Нажаль нема тут чого тут читати...")
    else:
        print('Ось текст: ', text)

        for symbol in '?!;':
            text = text.replace(symbol, str(symbol) + '.')

        list_sentence = [s.capitalize() for s in text.split('. ')]

        if os.path.isfile(f'./Result/{name_res_file}'):
            os.remove(f'./Result/{name_res_file}')

        with open(f'./Result/{name_res_file}', 'w') as file_res:
            for row in list_sentence:
                file_res.write(row + '\n')


def count_row(text: str):
    c_count = int()
    if os.path.isfile('./Result/Копія.txt'):
        with open('./Result/Копія.txt', 'r') as file:
            c_rows = len(file.readlines())
        print('Кількість рядків у файлі: ', c_rows)


def count_chr(text: str):
    c_count = int()
    if os.path.isfile('./Result/Копія.txt'):
        with open('./Result/Копія.txt', 'r') as file:
            c_chr = len(file.read())
        print('Кількість слів у файлі: ', c_chr)
