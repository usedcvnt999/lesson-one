# Домашнее задание (4)
# Дан кортеж состоящий из разных типов данных:
from operator import index

data_tuple = ('h', 6.13, 'C', 'e', 'T', True, 'k', 'e', 3, 'e', 1, 'g')
#
# 0 ) Найти в интернете информацию о том как работает sort(), reverse()
#
# 1 ) Создать два пустых списка letters и numbers
#
# 2 ) Пройтись циклом for по кортежу data_tuple, добавить
#     все строки в список letters, а всё остальное в numbers.
#
# 3 ) Из списка numbers удалить число 6.13 и переместить True
#     в конец списка letters, затем вставить число 2 между 3 и 1
#
# 4 ) Отсортировать numbers, реверсировать
#     letters и изменить пару букв в letters.
#
# 5 ) Измените список numbers в список квадратов своих же чисел
#
# 6 ) Преобразовать списки numbers и letters в кортежи
#
# (В итоге):
# кортеж letters должен выглядеть так:
# (True, 'G', 'e', 'e', 'k', 'T', 'e', 'c', 'h')
#
# кортеж numbers должен выглядеть так:
# (1, 4, 9)
# 1
letters = []
numbers = []



print("\n#2")
for i in data_tuple:
    if isinstance(i, str):
        letters.append(i)
    else:
        numbers.append(i)
print(letters)
print(numbers)

print("\n#3")
numbers.remove(6.13)
numbers.reverse()
numbers.insert(1, 2)
letters.append(numbers.pop(3))
print(numbers)
print(letters)

print("\n#4")
numbers.sort()
print(numbers)
letters.reverse()
letters[1] = "H"
letters[2] = "a"
letters[3] = "n"
letters[4] = "z"
letters[5] = "y"
print(letters)


print("\n#5")
for i in numbers:
    numbers[index(i)-1] = i**2
print(numbers)


print("\n#6")
numbers = tuple(numbers)
letters = tuple(letters)
print(letters)
print(numbers)
