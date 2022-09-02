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

    print('| №  |Назва файлу|\n+----+-----------+')
    num_key = 1
    for file in names_files:
        list_files[num_key] = file
        print('|', str(num_key).rjust(2), '|', file.ljust(10), '|')
        num_key += 1
    print('+----+-----------+')

    return list_files


def write_file():
    """
    Записуємо новий текстовий файл.
    """
    repeat_write_file = 'y'
    while repeat_write_file == 'y':
        file_name = input('Назва нового файлу: ')
        text_for_write = input('Введіть текст, для запису: ')

        with open(f'./{file_name}.txt', 'w') as my_file:
            my_file.write(f'{text_for_write}')

        repeat_write_file = input('Створит ще файл? (y/n): ').lower()


def read_file():
    """
    Вибираємо і читаємо файл.
    """
    repeat_read_file = 'y'
    while repeat_read_file == 'y':
        list_files = print_name_files()
        if list_files == 0:
            return

        my_choice = int(input('Виберіть номер файла для читання: '))
        selected_file = list_files[my_choice]
        with open(selected_file, 'r') as file:
            print(file.read())

        repeat_read_file = input("Прочитати ще один файл? (y/n): ").lower()


def main():
    welcome = "Яку дію бажаєте виконати:\nВведіть 'r' - прочитати або " \
              "'w' - редагувати/створити файл.\n"\
              "Для виходу будь яку клавішу: "

    repeat_main = 'y'
    while repeat_main == 'y':
        select_options = input(welcome)

        if select_options == 'r':
            read_file()
        if select_options == 'w':
            write_file()
        if select_options not in ('w', 'r'):
            break

        repeat_main = input(select_options).lower()


if __name__ == '__main__':
    main()
