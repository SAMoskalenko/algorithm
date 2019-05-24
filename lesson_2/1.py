# Написать программу, которая будет складывать, вычитать, умножать или делить два числа.
# Числа и знак операции вводятся пользователем. После выполнения вычисления программа не должна завершаться,
# а должна запрашивать новые данные для вычислений. Завершение программы должно выполняться при вводе символа '0'
# в качестве знака операции. Если пользователь вводит неверный знак (не '0', '+', '-', '*', '/'),
# то программа должна сообщать ему об ошибке и снова запрашивать знак операции.
# Также сообщать пользователю о невозможности деления на ноль, если он ввел 0 в качестве делителя.

# цикл

while True:
    first_number = int(input('Введите первое число: '))
    second_number = int(input('Введите второе число: '))
    operation = str(input('Введите вид операции или 0 для выхода: '))
    while operation not in '+-/;0':
        operation = str(input('Введите корректный вид операции или 0 для выхода: '))
    if operation == '+':
        print(first_number + second_number)
    elif operation == '-':
        print(first_number - second_number)
    elif operation == '*':
        print(first_number * second_number)
    elif operation == '/':
        if second_number != 0:
            print(first_number / second_number)
        else:
            print('Деление на 0 невозможно')
    elif operation == '0':
        break

# рекурсия

def recursion(operation):
    first_number = int(input('Введите первое число: '))
    second_number = int(input('Введите второе число: '))
    if operation == '0':
        return print('OK')
    while operation not in '+-/;0':
        operation = str(input('Введите корректный вид операции или 0 для выхода: '))
    if operation == '+':
        return print(first_number + second_number) + recursion(str(input('Введите вид операции или 0 для выхода: ')))
    elif operation == '-':
        return print(first_number - second_number) + recursion(str(input('Введите вид операции или 0 для выхода: ')))
    elif operation == '*':
        return print(first_number * second_number) + recursion(str(input('Введите вид операции или 0 для выхода: ')))
    elif operation == '/':
        if second_number != 0:
            return print(first_number / second_number) + recursion(str(input('Введите вид операции или 0 для выхода: ')))
        else:
            return print('Деление на 0 невозможно') + recursion(str(input('Введите вид операции или 0 для выхода: ')))


print(recursion(str(input('Введите вид операции или 0 для выхода: '))))