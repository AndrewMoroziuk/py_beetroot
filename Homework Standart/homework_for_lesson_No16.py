#  Task 1
class Person:

    def __init__(self, firstname, lastname, age, sex ):
        self.firstname = firstname
        self.lastname = lastname
        self.age = age
        self.sex = sex

    def output(self):
        raise TypeError("I'm an abstract animal class of human, men:)")


class Teach(Person):

    def __init__(self, firstname, lastname, age, sex, salary, experience):
        super().__init__(firstname, lastname, age, sex)
        self.salary = salary
        self.experience = experience

    def output(self):
        print('firstname:', self.firstname, 'lastname:', self.lastname,
              'age:', self.age, 'sex:', self.sex,
              'salary:', self.salary, 'experience:', self.experience)


class Student(Person):

    def __init__(self, firstname, lastname, age, sex, school_class, items):
        super().__init__(firstname, lastname, age, sex)
        self.school_class = school_class
        self.items = items

    def output(self):
        print('firstname:', self.firstname, 'lastname:', self.lastname, 'age:',
              self.age, 'sex:', self.sex,
              'school_class:', self.school_class, 'items:', self.items)


teacher_1 = Teach('Steven', 'Conley', 48, 'male', 1800, 13)
teacher_2 = Teach('Derrick', 'Fisher', 36, 'male', 1500, 8)
school_boy = Student('Kell', 'Hardy', 15, 'male', 10, {'Math': 10,
                                                       'History': 8})
school_girl = Student('Max', 'Bree', 12, 'female', 6, {'Math': 10,
                                                       'History': 8})
teacher_1.output()
teacher_2.output()
school_boy.output()
school_girl.output()


#  Task 2
class Mathematician:

    @staticmethod
    def square_nums(list_of_number):
        print([element ** 2 for element in list_of_number])
            

m = Mathematician()
m.square_nums([7, 11, 5, 4])
#  Task 2


# Task 3
class Product:
    def __init__(self, type, name, price):
        self.type = type
        self.name = name
        self.price = price


class ProductStore:

    def __init__(self, income):
        self.item = []
        self.income = income
        self.costs = 0

    def getgoods(self):
        print()
        for good in self.item:
            print('--- goods: ', good)

    def getincome(self):
        print('--- income: ', self.income, '$')

    def getcosts(self):
        print('--- costs: ', self.costs, '$')

    def getbalance(self):
        print('--- balance', self.income - self.costs, '$')

    def add(self, product, amount):

        self.item.append({'type': product.type,
                          'product': product.name,
                          'amount': product.price + amount})
        self.costs += float(product.price)
        self.getgoods()

    def set_discont(self, identification, percent):
        for element in self.item:
            if element['product'] == identification:
                element['amount'] = element['amount'] - (element['amount']
                                                         * (percent/100))
        self.getgoods()

    def sell_produtc(self, product, count):
        counter = 0
        for element_of_list in self.item:
            if element_of_list['product'] == product:
                counter += 1

        if counter >= count:
            while count != 0:
                for element_of_list in self.item:
                    if element_of_list['product'] == product:
                        self.item.remove(element_of_list)
                        self.income += element_of_list['amount']
                        count -= 1

            self.getgoods()
        else:
            print("РќРµРґРѕСЃС‚Р°С‚РЅСЊРѕ С‚РѕРІР°СЂС–РІ РЅР° СЃРєР»Р°РґС–")


beetroot_product_1 = Product('Sport', 'T-Shirt', 200)
beetroot_product_2 = Product('Food', 'Banana', 10)
beetroot_store = ProductStore(0)
beetroot_store.add(beetroot_product_1, 10)
beetroot_store.add(beetroot_product_2, 3)
beetroot_store.add(beetroot_product_2, 3)
beetroot_store.sell_produtc('Banana', 1)
beetroot_store.set_discont('T-Shirt', 10)
beetroot_store.sell_produtc('T-Shirt', 1)
beetroot_store.getgoods()
beetroot_store.getincome()
beetroot_store.getcosts()
beetroot_store.getbalance()
# Task 3


# Task 4
class CustomException(Exception):

    def __init__(self, msg):
        self.msg = msg
        self.log = open("./logs.txt", 'w')
        self.log.close()

    def callerror(self):
        with open("./logs.txt", 'a') as log:
            log.write(self.msg + '\n')


error = CustomException("Error")
error.callerror()  # Створює текстовий файл з Логами
error.callerror()
error.callerror()
error.callerror()
# Task 4











