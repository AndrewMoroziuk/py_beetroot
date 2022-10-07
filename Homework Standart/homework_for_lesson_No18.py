# Task 1
import email_validate as e


class Email:
    def __init__(self, address):
        self.address = address
        self.validate()

    def validate(self):
        if e.validate(self.address):
            return print(f"Validate E-mail '{self.address}' is successfully")
        return print(f"Validate E-mail '{self.address}' is error")

my_post = Email('andryhamorozyuk7@gmail.com')


# Task 2
class Boss:
    def __init__(self, name):
        self.__name = name

    @property
    def name(self):
        return self.__name


class Worker:
    def __init__(self, name):
        self.__name = name

    def rename(self, name_boss):
        self.__name = name_boss.name

    @property
    def name(self):
        return self.__name


my_boss = Boss('Savchenko Sergii')
print(my_boss.name)

i_am = Worker('Moroziuk Andrii')
print(i_am.name)
i_am.rename(my_boss)
print(i_am.name)


# Task 3
class TypeDecorators:  # Декоратор типів

    @staticmethod
    def to_int(func):
        def decorator(arg):
            arg = arg.strip()
            if arg.isnumeric():
                return int(arg)
            return f'{arg} не є числом!'

        return decorator

    @staticmethod
    def to_bool(func):
        def decorator(arg):
            arg = arg.strip().title()
            if arg == 'True':
                return True
            elif arg == 'False':
                return False
            return f'{arg} не є прапором булевої логіки!'
        return decorator


@TypeDecorators.to_int
def do_nothing(string: str) -> str:
    return string


@TypeDecorators.to_bool
def do_something(string: str) -> str:
    return string


a = ' 45 '
print(do_nothing(a), type(do_nothing(a)))
assert do_nothing('25') == 25

print()

b = ' true'
print(do_something(b), type(do_something(b)))
assert do_something(b) is True


