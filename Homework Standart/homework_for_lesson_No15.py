class Person:
    def __init__(self, firstname, lastname, age):
        self.firstname = firstname
        self.lastname = lastname
        self.age = age

    @staticmethod
    def talk(firstname, lastname, age):
        print(
            f'Hello, my name is {firstname} {lastname}, '
            f'I\'m {age} years old'
        )


class Dog:
    age_factor = 7

    def __init__(self, year_of_dog):
        self.year_of_dog = year_of_dog

    def human_age(self, multiplier_of_year=age_factor):
        return self.year_of_dog * multiplier_of_year


class TV:
    CHANNELS = ["BBC", "Discovery", "TV1000"]

    def __init__(self, select_channel=1):
        self.select_channel = select_channel

    @staticmethod
    def first_channel():
        print(TV.CHANNELS[0])

    @staticmethod
    def last_channel():
        print(TV.CHANNELS[-1])

    @staticmethod
    def turn_channel(number_of_channel):
        if number_of_channel <= len(TV.CHANNELS):
            print(TV.CHANNELS[number_of_channel-1])
        else:
            print("Wrong! Not find channel...")

    def next_channel(self):
        if self.select_channel != len(TV.CHANNELS):
            self.select_channel += 1
            print(TV.CHANNELS[self.select_channel-1])

        else:
            self.select_channel = 1
            print(TV.CHANNELS[0])

    def previous_channel(self):
        if self.select_channel != 1:
            self.select_channel -= 1
            print(TV.CHANNELS[self.select_channel-1])

        else:
            self.select_channel = len(TV.CHANNELS)
            print(TV.CHANNELS[-1])

    def current_channel(self):
        print(self.select_channel)

    @staticmethod
    def is_exist(name_or_number):
        if type(name_or_number) is int:
            if name_or_number in range(len(TV.CHANNELS)):
                print(TV.CHANNELS[name_or_number-1])
            else:
                print("Wrong! Not find channel...")

        if type(name_or_number) is str:
            if name_or_number in TV.CHANNELS:
                print(TV.CHANNELS.index(name_or_number))
            else:
                print("Wrong! Not find channel...")


#  For Task1
hero = Person('Victor', 'Frankenstein', 43)
father = Person('Alphonse', 'Frankenstein', 78)
print("Son: ", hero.firstname, hero.lastname, hero.age,
      "\nFather:", father.firstname, father.lastname, father.age)

#  For Task2
year_of_my_pet = Dog(12)
print("\nYears of my dog:", year_of_my_pet.human_age())

#  For Task3
print()
my_tv = TV()
my_tv.first_channel()
my_tv.last_channel()
my_tv.turn_channel(1)
my_tv.turn_channel(2)
my_tv.turn_channel(3)
my_tv.turn_channel(4)
my_tv.current_channel()
my_tv.next_channel()
my_tv.next_channel()
my_tv.next_channel()
my_tv.next_channel()
my_tv.previous_channel()
my_tv.previous_channel()
my_tv.previous_channel()
my_tv.previous_channel()
my_tv.previous_channel()
my_tv.is_exist("BBC")
my_tv.is_exist(3)
print()
tv_of_my_friends = TV()
tv_of_my_friends.current_channel()
tv_of_my_friends.previous_channel()
tv_of_my_friends.next_channel()
tv_of_my_friends.next_channel()
tv_of_my_friends.is_exist(5)
tv_of_my_friends.is_exist(2)
