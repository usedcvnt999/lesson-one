# Напишите функцию, которая принимает на вход массив чисел и возвращает новый массив,
# в котором каждый элемент исходного массива увеличен на 5.
# Например, для массива [10, 20, 30, 40, 50] результатом будет [15, 25, 35, 45, 55].


from typing import List

def int_input(placeholder: str) -> int:

    while True:
        input_one = input(placeholder)

        try:
            input_one = int(input_one)
        except ValueError:
            print('Не корректное значение...')

        if isinstance(input_one, int):
            return input_one


def plus_5(enter_arr: List[int]):
    """
    как работает......
    """
    new_arr = []

    for number in enter_arr:
        new_arr.append(number + 5)

    return new_arr



while True:
    number = int_input(placeholder=f'Введите размерность списка: ')
    array_one = []
    element = 0

    for elements in range(number):
        array_element = int_input(f"Елемент номер {element}: \n")
        if array_element == -1:
            continue
        array_one.append(array_element)
        element += 1
    print("Изначальный массив:\n", array_one)
    updated_arr = plus_5(enter_arr=array_one)
    print("Измененный массив:\n", updated_arr)
    if int_input("Хотите ли продолжить? (1 - да, 2 - нет):\n") == 2:
        exit(0)


# print(plus_5.__doc__)
