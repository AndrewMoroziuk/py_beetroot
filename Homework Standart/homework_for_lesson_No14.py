# Task 1
def logger(func):
    def inner(*args, **kwargs):
        print(func.__name__, *args)
    return inner


@logger
def add(x, y):
    return x + y


@logger
def square_all(*args):
    return [arg ** 2 for arg in args]


add(5, 6)
square_all(16, 69)


# Task 2

