# Подсчитать, сколько было выделено памяти под переменные в ранее разработанных программах в рамках первых трех уроков.
# Проанализировать результат и определить программы с наиболее эффективным использованием памяти.
#
# Примечание: Для анализа возьмите любые 1-3 ваших программы или несколько вариантов кода для одной и той же задачи.
# Результаты анализа вставьте в виде комментариев к коду. Также укажите в комментариях версию Python и разрядность вашей ОС.


from memory_profiler import profile
from random import randint

@profile()
def erat(x, n):
    a = [0] * n
    for i in range(n):
        a[i] = i
    a[1] = 0
    m = 2
    while m < n:
        if a[m] != 0:
            j = m * 2
            while j < n:
                a[j] = 0
                j = j + m
        m += 1
    b = []
    for i in a:
        if a[i] != 0:
            b.append(a[i])
    return b[x - 1]

@profile()
def cicle(x, n):
    count = 1
    for i in range(3, n):
        num = i
        lcount = 0
        for y in range(2, i):
            if num % y != 0:
                lcount += 1
            if lcount == (i - 2):
                count += 1
        if count == x:
            break
    return num


if __name__ == '__main__':
    erat(10, 5000)
    cicle(10, 5000)

# Python 3.7
# 64x
# использовано 11.8 MiB памяти для решения через решето Эратосфена, количество памяти не увеличивалось в течении действия программы
# использовано 11.8 MiB памяти для решения через цикл, количество памяти не увеличивалось в течении действия программы