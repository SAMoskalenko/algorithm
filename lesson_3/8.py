# Матрица 5x4 заполняется вводом с клавиатуры кроме последних элементов строк.
# Программа должна вычислять сумму введенных элементов каждой строки и записывать ее в последнюю ячейку строки.
# В конце следует вывести полученную матрицу.

a = []
for x in range(4):
    b = []
    for i in range(5):
        if i < 4:
            b.append(int(input('Введите значение ячейки: ')))
        else:
            summ = 0
            for y in b:
                summ += y
            b.append(summ)
    a.append(b)

for i in a:
    for y in i:
        print(y, end=' ')
    print()
