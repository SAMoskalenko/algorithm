# В массиве найти максимальный отрицательный элемент. Вывести на экран его значение и позицию в массиве.

from random import randint

a = []
n = int(input('Введите длинну массива: '))
for i in range(n):
    a.append(randint(-10, 10))

print(a)

b = []
position = 0

for i in a:
    if i < 0:
        b.append(i)

if len(b) > 0:
    max_neg = b[0]
    for i in b:
        if i > max_neg:
            max_neg = i

    for i in range(0, len(a)):
        if a[i] == max_neg:
            position = i + 1

    print(f'Максимальный отрицательный элемент в массиве {max_neg}, расположен на позиции под номером {position}')
else:
    print('Отрицательных элементов нет')
