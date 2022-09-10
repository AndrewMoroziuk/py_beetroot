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
def stop_words(fun):
    stopwords = ['pepsi', 'BMW']

    def inner(name):
        row = fun(name)
        for word in stopwords:
            row = row.replace(word, '***')
        print(row)

    return inner


@stop_words
def create_slogan(name):
    return f"{name} drinks pepsi in his brand new BMW!"


create_slogan('Andrew')


# Task 3
def arg_rules(fun):
    def inner(name):
        row = fun(name)
        if len(row) >= 15 and type(row) is str and '05' in row and '@' in row:
            return row
        return False

    return inner


@arg_rules
def create_slogan(name):
    return f"{name} drinks pepsi in his brand new BMW!"


print(create_slogan('S@SH05'))
