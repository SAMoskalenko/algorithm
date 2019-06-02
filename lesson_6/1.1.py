# Подсчитать, сколько было выделено памяти под переменные в ранее разработанных программах в рамках первых трех уроков.
# Проанализировать результат и определить программы с наиболее эффективным использованием памяти.
#
# Примечание: Для анализа возьмите любые 1-3 ваших программы или несколько вариантов кода для одной и той же задачи.
# Результаты анализа вставьте в виде комментариев к коду. Также укажите в комментариях версию Python и разрядность вашей ОС.


from memory_profiler import profile

from collections import deque

@profile()
def function():
    mas = 'A2'
    mbs = 'C4F'

    ma = []
    mb = []

    for s in mas:
        ma.append(s)

    for s in mbs:
        mb.append(s)

    a = '0x'
    b = '0x'

    for i in ma:
        a += i

    for i in mb:
        b += i

    a, b = int(a, 16), int(b, 16)
    c, d = hex(a + b), hex(a * b)

    summ = deque()
    mult = deque()

    for i in range(2, len(c)):
        summ.append(c[i].upper())

    for i in range(2, len(d)):
        mult.append(d[i].upper())

    print(f'Для чисел {ma} и {mb} сумма равна {summ}, произведение равно{mult}')

if __name__ == '__main__':
    function()

# Python 3.7
# 64x
# использовано 10.7 MiB памяти, количество памяти не увеличивалось в течении действия программы