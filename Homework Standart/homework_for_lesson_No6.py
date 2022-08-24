# Task 1
# The greatest number
import random
lst = []
while len(lst) != 10:
    lst.append(random.randint(1, 10))
print(lst)

# Task 2
# Exclusive common numbers.
import random
lst1, lst2 = [], []
while len(lst1) != 10:
    lst1.append(random.randint(1, 10))
    lst2.append(random.randint(1, 10))
unions = (set(lst1) & set(lst2))
print(lst1)
print(lst2)
print(unions)

# Task 3
# Extracting numbers.
lst = []
i = 0
while i < 100:
    if i % 7 == 0 and i % 5 != 0:
        lst.append(i)
    i += 1
print(*lst, sep=', ')
