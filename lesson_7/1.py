# Отсортируйте по убыванию методом пузырька одномерный целочисленный массив, заданный
# случайными числами на промежутке [-100; 100). Выведите на экран исходный и
# отсортированный массивы. Сортировка должна быть реализована в виде функции. По
# возможности доработайте алгоритм (сделайте его умнее).

from random import randint


def sort(list_a):
    n = 1
    while n < len(list_a):
        check = 0
        for i in range(len(list_a) - n):
            if list_a[i] > list_a[i + 1]:
                list_a[i], list_a[i + 1] = list_a[i + 1], list_a[i]
                check += 1
        if check == 0:
            break
        n += 1
    return list_a


a = [randint(-100, 100) for i in range(int(input('Введите длинну массива ')))]

print(a)
print(sort(a))
