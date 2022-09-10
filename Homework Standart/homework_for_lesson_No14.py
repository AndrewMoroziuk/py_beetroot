# Task 1
def logger(func):
    return print(func.__name__)


@logger
def add(x, y):
    return x + y


@logger
def square_all(*args):
    return [arg ** 2 for arg in args]

# Task 2

