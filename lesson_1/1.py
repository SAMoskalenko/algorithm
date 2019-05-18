# Найти сумму и произведение цифр трехзначного числа, которое вводит пользователь.

num = int(input('Введите трехзначное число: '))
first_digit = num % 10
second_digit = num // 10 % 10
third_digit = num // 100
summ = first_digit + second_digit + third_digit
print(f'Сумма цифр вашего числа {num} равна {summ}')
