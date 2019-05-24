# В массиве случайных целых чисел поменять местами минимальный и максимальный элементы.

from random import randint

a = []
n = int(input('Введите длинну массива: '))
for i in range(n):
    a.append(randint(-10, 10))

print(a)

min = 0
min_num = 0
max = 0
max_num = 0

for i in range(0, len(a)):
    if min > a[i]:
        min_num = i
    if max < a[i]:
        max_num = i

a[min_num], a[max_num] = a[max_num], a[min_num]

print(a)
