# Task 1
# A simple function.
def movie(name: str):
    print(f'My favorite movie is named "{name}"')


movie("Аватар")


# Task 2
# Creating a dictionary.

def make_country(**kwargs):
    for key, value in kwargs.items():
        print(f'{key} має столицю: місто {value}')


make_country(Україна="Київ", Франція="Париж")


# Task 3
# A simple calculator.

def calc(operator: str, *args: float):
    x = 0
    q = args[0]
    for i in args[1:]:
        if operator == '+': x += i
        if operator == '-': x -= i
        if operator == '*':
            x = q * i
            q = x
        if operator == '/':
            x = q / i
            q = x
    print(x)


calc('*', 100, 2, 32)
