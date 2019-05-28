# Определить, какое число в массиве встречается чаще всего.

from random import randint

a = []
n = int(input('Введите длинну массива: '))
for i in range(n):
    a.append(randint(-10, 10))

print(a)

num = 0
count = 0

for x in a:
    n = 0
    for y in a:
        if y == x:
            n += 1
            if n > count:
                count = n
                num = x

print(f'Число {num} встречается чаще всего, {count} раз(а)')
