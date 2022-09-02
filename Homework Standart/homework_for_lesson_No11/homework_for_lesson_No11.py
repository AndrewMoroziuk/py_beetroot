import glob


def print_name_files(path=''):
    """
    Функція для функції 'write_file'.
    Виводить на екран список файлів з директорії.
    """
    list_files = {}
    names_files = glob.glob(path + '*.txt')

    if len(names_files) == 0:
        print('Немає файлів')
        return 0

    len_row = [len(i) for i in names_files]  # довжина назвів файлів
    max_len_row = max(len_row) + 2  # довжина найдовшого файла + два пробіла
    print('|  № ' + '| Назва файлу'.ljust(max_len_row), '|', '\n|----+'
          + '-'*max_len_row + '|')

    num_key = 1
    for file in names_files:
        list_files[num_key] = file
        print('|', str(num_key).rjust(2), '|',
              file.ljust(max_len_row - 1) + '|')
        num_key += 1

    print('|----+' + '-'*max_len_row + '|')

    return list_files


def read_file():
    """
    Вибираємо і читаємо файл.
    """
    while True:
        list_files = print_name_files()
        if list_files == 0:
            return print("Немає файлів для перегляду")

        try:
            my_choice = int(input('Виберіть номер файла для читання: '))
        except ValueError:
            print('\n! Має бути передано число !\n')
            continue

        if my_choice > len(list_files):
            print('\n! Немає такого номеру !\n')
            continue

        selected_file = list_files[my_choice]
        with open(selected_file, 'r') as file:
            print(file.read())

        if input(" (y) Прочитати ще один файл?: ").lower() != 'y':
            break


def write_file():
    """
    Записуємо новий текстовий файл.
    """

    while True:
        file_name = input('Назва нового файлу: ')
        text_for_write = input('Введіть текст, для запису: ')

        with open(f'./{file_name}.txt', 'w') as my_file:
            my_file.write(f'{text_for_write}')

        if input(' (y) Створит ще файл?: ').lower() != 'y':
            break


def phone_book():
    my_phone = dict()
    my_phone['name'] = input('Назва: ')
    my_phone['second_name'] = input('Прізвище: ')
    my_phone['phone'] = input('Номер тел.: ')
    my_phone['city'] = input('Назва міста: ')


def main():
    while True:
        select_options = input("\nВведіть 'r' - прочитати / "\
                               "'w' - редагувати/створити файл."\
                               "Для виходу будь яку клавішу:")

        if select_options == 'r':
            read_file()
        elif select_options == 'w':
            write_file()
        else:
            break


if __name__ == '__main__':
    main()
