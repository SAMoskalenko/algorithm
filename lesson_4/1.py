# Проанализировать скорость и сложность одного любого алгоритма, разработанных в рамках домашнего задания первых трех уроков.
# Примечание: попробуйте написать несколько реализаций алгоритма и сравнить их.

import timeit, sys

sys.setrecursionlimit(100000)


def cicle(n):
    count = 0
    summ = 0
    count_num = 1
    while count < n:
        summ += count_num
        count += 1
        count_num = count_num / (-2)


def recursion(c, n, s):
    if c == 0:
        return s
    else:
        c -= 1
        s += n
        n = n / (-2)
        return recursion(c, n, s)


print(timeit.timeit("cicle(100)", setup="from __main__ import cicle", number=10000))
print(timeit.timeit("recursion(100, 1, 0)", setup="from __main__ import recursion", number=10000))

# Время исполнения решеия через цикл: 0.11691813999999999
# Время исполнения решеия через рекурсию: 0.20063559400000003

# Сложность в обоих вариантах линейная, но в случае цикла алгоритм работает приблизительно в 2 раза быстрее