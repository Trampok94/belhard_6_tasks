"""
Написать функцию common_numbers, которая принимает 2 списка, которые содержат
целые числа.

Функция должна вернуть список общих чисел, который отсортирован по убыванию
"""


def common_numbers(l_1: list, l_2: list) -> list:
    l_res = list(set(l_1).intersection(set(l_2)))
    l_res.sort(reverse=True)
    return l_res


l_1 = [1, 2, 3, 4, 5]
l_2 = [4, 5, 6, 7, 8]

print(common_numbers(l_1, l_2))
