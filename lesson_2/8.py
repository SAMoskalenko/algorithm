# Посчитать, сколько раз встречается определенная цифра в введенной последовательности чисел.
# Количество вводимых чисел и цифра, которую необходимо посчитать, задаются вводом с клавиатуры.

import random

symbol = int(input('Введите искомую цифру: '))
number = int(input("Введите колтичество символов в последжовательности: "))
massive = [0] * number
for i in range(number):
    massive[i] = random.randint(0, 9)

count = 0
result = 0

while count < number:
    if massive[count] == symbol:
        result += 1
    count += 1

print(f'В последовательности {massive} символ {symbol} встречается {count} раз(а)')
