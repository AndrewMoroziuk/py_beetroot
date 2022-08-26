import os


def read_and_copy_text_by_sentence(text: str = None):
    if text is None:
        print("Нажаль нема тут чого тут читати...")
    else:
        print('Ось текст: ', text)
        list_sentence = [s.capitalize() for s in text.split('. ')]
        if os.path.isfile('./Result/Копія.txt'):
            os.remove('./Result/Копія.txt')
        with open('./Result/Копія.txt', 'w') as file_res:
            for row in list_sentence:
                file_res.write(row + '.\n')
