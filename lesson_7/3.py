# Массив размером 2m + 1, где m – натуральное число, заполнен случайным образом. Найдите
# в массиве медиану. Медианой называется элемент ряда, делящий его на две равные части: в
# одной находятся элементы, которые не меньше медианы, в другой – не больше медианы.
# Задачу можно решить без сортировки исходного массива. Но если это слишком сложно, то
# используйте метод сортировки, который не рассматривался на уроках.


from random import randint

a = [randint(-100, 100) for i in range(int(input('Введите значение ')) * 2 + 1)]

print(a)

e = 0

while e <= (len(a) // 2 + 1):
    min = a[0]
    n = 0
    i = 0
    while i < len(a):
        if a[i] < min:
            min = a[i]
            n = i
        i += 1
    a.pop(n)
    e += 1

print(min)
