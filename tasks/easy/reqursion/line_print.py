"""
Написать рекурсивную функцию  line_print, которая принимает 1 аргумент - список

Функция печатает каждых элемент на новой строке.

Если элемент списка - список, то его элементы должны выводиться с отступом
относительно родительского на одну табуляцию

Например:

some_list = [1, 2, [1, 2, [5, 7], 3], 8]

line_print(some_list)
1
2
    1
    2
        5
        7
    3
8
"""


def line_print(some_list: list, tab=0):
    for i in some_list:
        if isinstance(i, list):
            line_print(i, tab + 1)
        else:
            print("    " * tab + str(i))
    tab = 0


some_list = [1, 2, [1, 2, [5, 7], 3], 8]
line_print(some_list)
