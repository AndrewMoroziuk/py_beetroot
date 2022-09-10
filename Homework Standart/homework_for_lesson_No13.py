# Task 1
def declaration_of_local_variables():
    alfa = 42
    string = '42'
    lists = [[0, 3], [69, 'LoL']]


print('Number of local variables: ',
      declaration_of_local_variables.__code__.co_nlocals)


# Task 2
def fun():
    return "- Hi!:)"


def fun_in_fun(functions):
    print("- Hello!\n" + functions)


fun_in_fun(fun())


# Task 3
def fun_one(): return print('All numbers is positive')


def fun_two(): return print('Some each numbers is negative')


def choose_func(lst_number, fun_1, fun_2):
    if min(lst_number) >= 0:
        return fun_1()
    return fun_2()


list_number = [int(x) for x in input().split()]
choose_func(list_number, fun_one, fun_two)
