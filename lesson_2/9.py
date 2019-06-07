# Среди натуральных чисел, которые были введены, найти наибольшее по сумме цифр. Вывести на экран это число и сумму его цифр.

massive = []
while True:
    num = int(input('Введите число или 0 если хотите выйти: '))
    if num != 0:
        massive.append(num)
    else:
        break

max = 0
element = 0

for el in massive:
    el_summ = 0
    pr_el = el

    while el > 0:
        el_summ += el % 10
        el = el // 10
    if el_summ > max:
        max = el_summ
        element = pr_el

print(f'Для массива {massive} элементом с максимальной суммой чисел является {element} сумма равна {max}')
