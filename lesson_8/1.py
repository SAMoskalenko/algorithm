# Определение количества различных подстрок с использованием хэш-функции.
# Пусть дана строка S длиной N, состоящая только из маленьких латинских букв.
# Требуется найти количество различных подстрок в этой строке.

import random
import string

S = ''.join(random.choice(string.ascii_lowercase) for _ in range(int(input('введите длинну строки '))))
s = set()
for i in range(len(S)):
    if i == 0:
        n = len(S) - 1
    else:
        n = len(S)
    for j in range(n, i, -1):
        s.add(hash(S[i:j]))

print('Количество различных подстрок в строке: ', len(s))