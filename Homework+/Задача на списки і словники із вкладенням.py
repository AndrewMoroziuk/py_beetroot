from collections import OrderedDict


from data import list_and_dict as data   # імпорт змінну зі списком вкладених словників з іншого файлу в цій директорії


it_book = list()
iteration = -1
for data_key, data_val in data.items():
    for j in data_val:
        it_book.append(OrderedDict())  # використаю відсортований список, щоб результат збігався в точності з прикладом
        iteration += 1  # ітерація в списку по словнику, котрий ми додали перед цим
        for key, val in j.items():
            it_book[iteration][key] = val
            it_book[iteration]['department'] = data_key
            it_book[iteration].move_to_end('department')  # 'department' в кінець словника (хоча це все необов'язково)


print(it_book)