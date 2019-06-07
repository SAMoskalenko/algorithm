# Найти максимальный элемент среди минимальных элементов столбцов матрицы.

from random import randint

n = int(input('Введите ширину матрицы: '))
m = int(input('Введите высоту матрицы: '))

a = []
for x in range(m):
    b = []
    for i in range(n):
        b.append(randint(-10, 10))
    a.append(b)

print(a)

b = a[0]
for i in a:
    for x in range(len(i)):
        if i[x] < b[x]:
            b[x] = i[x]

max = b[0]

for i in b:
    if i > max:
        max = i

print(f'Максимальный элемент среди минимальных элементов столбцов матрицы равен {max}')
