from typing import Union

def even_or_not(
        number: int
) -> bool:
    if not isinstance(number, int):
        raise TypeError("arg have to be integer!!!")
    elif isinstance(number, int) and number % 2 == 0:
        return True
    elif isinstance(number, int) and not number % 2 == 0:
        return False
# print(even_or_not())

def spelling(
        sentense: str
) -> bool:
    if sentense[0].isupper() and sentense.endswith("."):
        return True
    else:
        return False
# print(spelling("Hello world."))


def calculator(
        number_1: Union[int, float],
        operator: str,number_2: Union[int, float]
) -> Union[int, float, str]:
    try:
        if operator == "+":
            return number_1 + number_2
        elif operator == "-":
            return number_1 - number_2
        elif operator == "/":
            return number_1 / number_2
        elif operator == "//":
            return number_1 // number_2
        elif operator == "*":
            return number_1 * number_2
        elif operator == "**":
            return number_1 ** number_2
    except ZeroDivisionError:
        return "u can't divide number to zero!!!"
# calculator(, "**", )

def nearest_number(
        argument_1: Union[tuple, list],
        target: Union[int, float] = 0
) -> Union[int, float]:
    return min(argument_1, key = lambda x: (abs(target - x)))
print(nearest_number([1, 404, 93, 5.12], 6))