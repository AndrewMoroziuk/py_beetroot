# Task 1
class Animal:
    def talk(self):
        # pass
        raise TypeError("I'm an abstract animal class, dude")


class Dog(Animal):
    def talk(self):
        print('woof woof')


class Cat(Animal):
    def talk(self):
        print('meow meow')


maus = Animal()
cat = Cat()
dog = Dog()


def to_vote(pet):
    pet.talk()


to_vote(cat)
to_vote(dog)
#to_vote(maus)  # Викликає помилку, в якій описаний власне повідомлення
# Task 1


# Task 2
class Library:
    counter = 0

    def __init__(self, name):
        self.name = name
        self.books = []
        self.author = []

    def __str__(self):
        return f'Ми викликали оператор print класу {self.name}'

    def __repr__(self):
        return self.__str__()

    def new_book(self, name, year, author):
        book = Book(name, year, author)
        self.books.append({'name': name, 'year': year, 'author': author})
        Library.counter += 1

    def group_author(self, author):
        author_group_list = []
        for dict_ in self.books:
            if dict_['author'] == author:
                author_group_list.append(dict_)
        print(sorted(author_group_list, key=lambda x: x['author']))

    def group_year(self, year):
        year_group_list = []
        for dict_ in self.books:
            if dict_['year'] == year:
                year_group_list.append(dict_)
        print(sorted(year_group_list, key=lambda x: x['year']))


class Author:
    def __init__(self, name, state, birthday, books):
        self.name = name
        self.state = state
        self.birthday = birthday
        self.books = []

    def __str__(self):
        return f'Ми викликали оператор print класу {self.name}'

    def __repr__(self):
        return self.__str__()


class Book:
    def __init__(self, name, year, author):
        self.name = name
        self.year = year
        self.author = author

    def __str__(self):
        return f'Ми викликали оператор print класу {self.name}'

    def __repr__(self):
        return self.__str__()


author_1 = Author("Viliam", 'Virginya', '12.12.1202', ['kod', 'vins'])
author_2 = Author("Genre", 'New Yourk', '22.09.1988', ['koser', 'bigO'])
library = Library("Own")
print(Library.counter)
library.new_book('Kod', 1788, author_1.name)
library.new_book('bigO', 1999, author_2.name)
library.new_book('bigO', 1999, 'Vitali')
# print(library.books)
library.group_author('Genre')
print(library.books)
library.group_year(1788)
print(library)
print(Library.counter)
# Task 2


# Task 3
class Fraction:
    def __init__(self, one, two):
        self.one = float(one)
        self.two = float(two)
        self.result = self.one / self.two

    def __repr__(self):
        return f'{self.result}'

    def __add__(self, other):
        if hasattr(other, 'result'):
            return self.result + other.result
        return self.result + other

    def __eq__(self, other):
        return self.result == getattr(other, "value", other)


x = Fraction(1, 2)
y = Fraction(1, 4)
print(x, type(x))
print(y)
print(x + y)
print(Fraction(0.75, 1))
print(type((x + y)))
print(type(Fraction(0.75, 1)))
print((x + y) == Fraction(0.75, 1))

