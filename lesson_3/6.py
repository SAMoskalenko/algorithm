# В одномерном массиве найти сумму элементов, находящихся между минимальным и максимальным элементами.
# Сами минимальный и максимальный элементы в сумму не включать.

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

# при расчетах не учитывается возможная повторяемость элементов

for i in range(0, len(a)):
    if min > a[i]:
        min_num = i
        min = a[i]
    if max < a[i]:
        max_num = i
        max = a[i]

print(max_num)
print(min_num)
summ = 0

if min_num < max_num:
    for i in range(min_num + 1, max_num):
        summ += a[i]
else:
    for i in range(max_num + 1, min_num):
        summ += a[i]

print(f'Сумму элементов, находящихся между минимальным и максимальным элементами равна {summ}')
