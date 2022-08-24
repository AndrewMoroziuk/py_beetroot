# Task 1
# Make a program that has some sentence (a string) on input and returns a dict containing all unique words as keys and
# the number of occurrences as values.

# -- 1 спосіб
# row = 'cas mis cas year dj dj year year mis year '
row = input()
book = dict()
row = row.strip()
for s in row.split(' '):
    book.update({s: row.count(s)})
for k, v in book.items():
    print(f'Всього слів "{k}" в стрічці: {v}')

# -- 2 спосіб
# s = 'cas mis cas year dj dj year year mis year '
s = input()
s = s.strip()
row = {i: s.count(i) for i in s.split(" ")}
for k, v in row.items():
    print(f'Всього слів "{k}" в стрічці: {v}')

# +++++++++++++++++++++++++++++++++++++++++++++++++++++++
# Task 2
# Compute the total price of the stock where the total price is the sum of the price of an item multiplied by the
# quantity of this exact item.
suma = int()
stock = {
    "banana": 6,
    "apple": 0,
    "orange": 32,
    "pear": 15
}
prices = {
    "banana": 4,
    "apple": 2,
    "orange": 1.5,
    "pear": 3
}
for fruit, kil in stock.items():
    suma += kil * prices.get(fruit)
print(suma)

# Task 4
# Створити лист із днями тижня.
# В один рядок (ну або як завжди) створити словник виду: {1: “Monday”, 2:...
# Також в один рядок або як вдасться створити зворотній словник {“Monday”: 1,
import calendar as cl

week = {i + 1: cl.day_name[i] for i in range(0, 7)}
week1 = {cl.day_name[i]: i + 1 for i in range(0, 7)}
print(week)
print(week1)
