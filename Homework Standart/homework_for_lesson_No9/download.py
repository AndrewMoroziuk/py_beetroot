import os


def read_and_copy_text_by_sentence(text: str = None):
    if text is None:
        print("Нажаль нема тут чого тут читати...")
    else:
        print('Ось текст: ', text)
        text = text.replace('?', '?.')
        list_sentence = [s.capitalize() for s in text.split('. ')]
        if os.path.isfile('./Result/Копія.txt'):
            os.remove('./Result/Копія.txt')
        with open('./Result/Копія.txt', 'w') as file_res:
            for row in list_sentence:
                file_res.write(row + '.\n')


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
