import itertools


# Task 1 TasK 2
class InRange:
    def __init__(self, cursorer, end, steep=1):
        self.cursor = cursorer
        self.end = end
        self.steep = steep
        self.index = 0
        self.lister = [x for x in range(self.cursor, self.end, self.steep)]

    def __iter__(self):
        self.a = itertools.count(start=1)
        return self

    def __next__(self):
        if self.cursor >= self.end:
            raise StopIteration
        self.cursor += self.steep
        self.index += 1
        return self.cursor - self.steep, self.a.__next__()


for value, number in InRange(1, 20, 3):
    print(f'Значення {value}, порядковий номер {number}')

print()

a = InRange(1, 20, 3)
print(f'Значення {a.lister[3]}')




