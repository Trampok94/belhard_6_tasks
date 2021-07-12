"""
Написать функцию multiply_dict_values, которая принимает словарь SOME_DICT,
у которого ключи - строки, а значения - целые числа.

Необходимо, чтобы функция вернула результат умножения всех значений из словаря
"""
SOME_DICT = {str(val): val for val in range(1, 50, 3)}


def multiply_dict_values(dict_1: dict) -> int:
    res = 1
    for i in dict_1.values():
        res *= i
    return res


print(multiply_dict_values(SOME_DICT))
