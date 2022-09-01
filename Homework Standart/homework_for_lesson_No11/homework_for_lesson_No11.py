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
        create_or_upload = input(' (n) Створити\n (r) Редагувати')
        if create_or_upload not in ('n', 'r'):
            break
        elif create_or_upload == 'n':
            file_name = input('Назва нового файлу: ')
            text_for_write = input('Введіть текст, для запису: ')

            with open(f'./{file_name}.txt', 'w') as my_file:
                my_file.write(f'{text_for_write}')
        else:
            list_files = print_name_files()
            if list_files == 0:
                return print('Немає файлів для перегляду')

            my_choice = int(input('Виберіть номер файла для редагування: '))
            if my_choice > len(list_files):
                return print('Помилка. Нема файлу за таким номером')

            selected_file = list_files[my_choice]
            with open(selected_file, 'rw') as file:
                print(file.read())

        repeat_write_file = input(' (y) Створит ще файл?').lower()


def read_file():
    """
    Вибираємо і читаємо файл.
    """
    repeat_read_file = 'y'
    while repeat_read_file == 'y':
        list_files = print_name_files()
        if list_files == 0:
            return print('Немає файлів для перегляду')

        my_choice = int(input('Виберіть номер файла для читання: '))
        if my_choice > len(list_files):
            return print('Помилка. Нема файлу за таким номером')

        selected_file = list_files[my_choice]
        with open(selected_file, 'r') as file:
            print(file.read())

        repeat_read_file = input(" (y) Прочитати ще один файл?").lower()


def main():
    while True:
        select_options = input("\nЯку дію бажаєте виконати:\n"
                  "'r' - прочитати файл або 'w' - створити файл.\n"
                  "(Для виходу будь яку клавішу)")
        if select_options == 'r':
            read_file()
            continue
        elif select_options == 'w':
            write_file()
            continue
        else:
            break


if __name__ == '__main__':
    main()
