# В одномерном массиве целых чисел определить два наименьших элемента.
# Они могут быть как равны между собой (оба являться минимальными), так и различаться.

from random import randint

a = []
n = int(input('Введите длинну массива: '))
for i in range(n):
    a.append(randint(-10, 10))

print(a)

for i in range(1, n):
    if a[i] > a[i-1]:
        a[i-1], a[i] = a[i], a[i-1]

for i in range(1, n):
    if a[i] > a[i-1]:
        a[i-1], a[i] = a[i], a[i-1]

print(f'Минимальные числа в массиве {a[n-2]} и {a[n-1]}')