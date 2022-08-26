import random
import sys

# Task 1


def oops():
    rand = random.random()
    if rand >= 0.5:
        raise KeyError()
    else:
        raise IndexError()


def err_ext():
    try:
        oops()
    except IndexError:
        print('Uups... IndexError')
    except:
        print('Uups... See you error?')


err_ext()


# Task 2
try:
    integer_one = int(input("Prime number: "))
    integer_two = int(input("Second number: "))
    result = integer_one**2 / integer_two
except:
    '''
    Вирішив гарно вивести помилку.  Щоб не гадати, яка буде помилка, перехоплюю
    її і через метод  exc_info() читаю інфо про неї, а саме його перший елемент
    Після, шукаю індекси лапків і роблю надріз рядка, що вивести лише тип 
    помилки.  Гарно і лаконічно, хоч можливо є уже елегантніше рішення:)
    '''
    err = str(sys.exc_info()[0])
    idx = list()
    for i in range(0, len(err)-1):
        if err[i] == "'":
            idx.append(i)
    err = err[idx[0]+1:idx[1]]
    print("Помилка типу:", err)
