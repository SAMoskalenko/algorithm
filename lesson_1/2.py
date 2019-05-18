# Выполнить логические побитовые операции «И», «ИЛИ» и др. над числами 5 и 6.
# Выполнить над числом 5 побитовый сдвиг вправо и влево на два знака. Объяснить полученный результат.

first_number = 5
second_number = 6

print(f'Побитовое "И" {first_number & second_number}')
print(f'Побитовое "ИЛИ" {first_number | second_number}')
print(f'Побитовое "ИСКЛЮЧАЮЩЕЕ ИЛИ" {first_number ^ second_number}')
print(f'Побитовое "ОТРИЦАНИЕ ПЯТЕРКИ" {~ first_number}')
print(f'Побитовое "ОТРИЦАНИЕ ШЕСТЕРКИ" {~ second_number}')
print(f'Побитовое "И" {first_number << 2}')
print(f'Побитовое "И" {first_number >> 2}')
