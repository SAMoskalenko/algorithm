# Найти сумму n элементов следующего ряда чисел: 1 -0.5 0.25 -0.125 ...Количество элементов (n) вводится с клавиатуры.

n = int(input('Введите количество элементов: '))
count = 0
summ = 0
count_num = 1
while count < n:
    summ += count_num
    count += 1
    count_num = count_num / (-2)
print(summ)

# рекурсия

def recursion(c, n, s):
    if c == 0:
        return s
    else:
        c -= 1
        s += n
        n = n / (-2)
        return recursion(c, n, s)


print(recursion(int(input('Введите количество элементов: ')), 1, 0))
