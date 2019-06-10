# Отсортируйте по возрастанию методом слияния одномерный вещественный массив,
# заданный случайными числами на промежутке [0; 50). Выведите на экран исходный и
# отсортированный массивы.

from random import randint


def sort(list_a):
    if len(list_a) > 1:
        middle = len(list_a) // 2
        print('middle: ', middle)
        left = list_a[:middle]
        right = list_a[middle:]

        sort(left)
        sort(right)

        l, r, n = 0, 0, 0

        while l < len(left) and r < len(right):
            if left[l] < right[r]:
                list_a[n] = left[l]
                l += 1
            else:
                list_a[n] = right[r]
                r += 1
            n += 1

        while l < len(left):
            list_a[n] = left[l]
            l += 1
            n += 1

        while r < len(right):
            list_a[n] = right[r]
            r += 1
            n += 1

        print('list_a: ', list_a)
        return list_a

a = [randint(0, 50) for i in range(int(input('Введите длинну массива ')))]

print(a)
print(sort(a))