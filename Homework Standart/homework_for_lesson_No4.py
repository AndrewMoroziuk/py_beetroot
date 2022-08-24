# Task 1
# String manipulation
s = input("Ведіть строку: ")
if len(s) < 2:
    print("Помилка")
else:
    print(s[0:2] + s[len(s)-2:])


# Task 2
# The valid phone number program.
flag = True
x = '+38' + input('Введіть номер телефону у форматі +38XXXXXXXXXX: ')

for i in x[1:]:
    if i.isdigit() != True:
        flag = False
        break

if len(x) == 13 and flag == True:
    print(f'Формат телефоного номеру вірний!\n{x}')
else:
    print('Формат телефоного номеру невірний!')


# Task 3
# The math quiz program.
fi = 1
rez = input('Чи правильний розвязок виразу 65!:' )
for i in range(65,1,-2):
    x = i * (i-1)
    fi *= x

if int(rez) == fi:
    print(f"{fi}\nЧудово!")
else:
    print(f"{fi}\nСпробуй ще раз!")

# Task 4
# The name check
name = 'андрій'
write = input()
if write.lower() == name:
    print(f"Чудово, {name.title()}!")
else:
    print(f"Спробуй ще раз!")