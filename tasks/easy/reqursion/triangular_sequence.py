"""
Написать функцию triangular_sequence, которая принимает n и выводит
следующую последовательность

1
22
333
4444
55555
...

Например:

n = 3:
1
22
333

n = 6:
1
22
333
4444
55555
666666
"""


def triangular_sequence(n, i=1):
    if i == n:
        print(str(n) * n)
    else:
        print(str(i) * i)
        return triangular_sequence(n, i + 1)


triangular_sequence(6)
