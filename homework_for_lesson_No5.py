# Task 1
# The Guessing Game.
import random
x = random.randint(1, 10)
while True:
    s = int(input("Введіть число від 1 до 10 включно: "))
    if s == x:
        print(f"Вітаю! Ти вгадав чило {x}!")
        break
    else:
        print("Спробуй ще раз!")

# Task 2
# The birthday greeting program.
name = input("Ваше ім'я: ")
year = int(input("Ваш вік: "))
print(f'Привіт, {name}, на твій наступний день народження тобі виповниться {year + 1 } років')

# Task 3
# Words combination
import random
s = input('Ваш рядок: ')
lst = []
for k in range(5):
    new_s = ''
    for i in range(len(s)):
        x = random.randint(1, len(s) - 1)
        new_s += s[x]
    lst.append(new_s)
print(*lst, sep=', ')
