# one = "Три"
# two = "девицы"
# three = "под"
# four = "окном"
# five = "Пряли"
# six = "поздно"
# seven = "вечерком."
# eight = "«Кабы"
# nine = "я"
# ten = "была"
# eleven = "царица, —"
#
# number_one = 0
# number_two = 0
#
# fairy_tail = f"{one} {two} {three} {four} \n{five} {six} {seven} \n{eight} {nine} {ten} {eleven}..."
#
# def task2():
#     number_one = float(input("Задайте первое число: \n"))
#     number_two = float(input("Задайте второе число: \n"))
#
#
#
#
# task1 = int(input(f"Задание: \n"))
# if task == 1:
#     print(f"Заданеи первое: \n{fairy_tail}")
# elif task == 2:
from calendar import month

# number = 10
# print(number)
# # number = number + 10
# # print(number)
# number += 10
# print(number)




day = input("День рождения: \n")
month = input("Месяц рождения: \n")

def zodiac():
    if day > 0 and month > 0:
        if 21 <= day <= 31 and month == 3 or day <= 20 and month == 4:
            print(f"Знак зодиака: Овен")
        elif 21 <= day <= 30 and month == 4 or day <= 21 and month == 5:
            print(f"Знак зодиака: Телец")
        elif 22 <= day <= 31 and month == 5 or day <= 21 and month == 6:
            print(f"Знак зодиака: Близнецы")
        elif 22 <= day <= 31 and month == 6 or day <= 22 and month == 7:
            print(f"Знак зодиака: Рак")
        elif 23 <= day <= 30 and month == 7 or day <= 21 and month == 8:
            print(f"Знак зодиака: Лев")
        elif 22 <= day <= 31 and month == 8 or day <= 23 and month == 9:
            print(f"Знак зодиака: Дева")
        elif 24 <= day <= 30 and month == 9 or day <= 23 and month == 10:
            print(f"Знак зодиака: Весы")
        elif 24 <= day <= 31 and month == 10 or day <= 22 and month == 11:
            print(f"Знак зодиака: Скорпион")
        elif 23 <= day <= 30 and month == 11 or day <= 22 and month == 12:
            print(f"Знак зодиака: Стрелец")
        elif 23 <= day <= 31 and month == 12 or day <= 20 and month == 1:
            print(f"Знак зодиака: Козерог")
        elif 21 <= day <= 31 and month == 1 or day <= 19 and month == 2:
            print(f"Знак зодиака: Водолей")
        elif 20 <= day <= 28 and month == 2 or day <= 20 and month == 3:
            print(f"Знак зодиака: Рыбы")
        else:
            print("Не корректные данные")
    else:
        print("Не корректные данные")

try:
    day = int(day)
    month = int(month)
    zodiac()
except:
    print("Не корректное значение")

