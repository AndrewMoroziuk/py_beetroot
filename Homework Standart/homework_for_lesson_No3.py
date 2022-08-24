# Task 1
# The greeting program.
while True:
    myself_data = [i for i in input('Введіть своє імя та поточний день тижня через пробіл: ').split(' ')]
    if len(myself_data) < 2 or myself_data[1] == '':
        print(f'Ви дещо пропустили, спробуйте ще раз:)', end='\n\n')
    else:
        print(f'Good day {myself_data[0]}! {myself_data[1]} is a perfect day to learn some python.', end='\n\n')

# Task 2
# Manipulate strings.
while True:
    myself_data = [i.capitalize() for i in input('Введіть своє імя та прізвище тижня через пробіл: ').split(' ')]
    if len(myself_data) < 2 or myself_data[1] == '':
        print(f'Ви дещо пропустили, спробуйте ще раз:)', end='\n\n')
    else:
        print(f"Привіт {' '.join(myself_data)}", end='\n\n')


# Task 3
# Using python as a calculator.
a, b = int(input("Введіть перше число: ")), int(input("Введіть друге число: "))
print(
    a + b,
    a - b,
    a * b,
    round(a / b, 2),
    a // b,
    a % b,
    a ** b, sep='\n')
