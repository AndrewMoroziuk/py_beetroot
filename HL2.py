work_day = 22
miss_day = int(input("Пропустив днів: "))
year = int(input("Роки: "))
count_chl = int(input("Кількість дітей: "))

math = 400 * (20 * year) + (30 * count_chl)

if miss_day == 0:
    print(math + 100)
else:
    print(math)
