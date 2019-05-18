# Пользователь вводит две буквы. Определить, на каких местах алфавита они стоят и сколько между ними находится букв.

first_letter = ord(input('Введите первую букву: '))
second_letter = ord(input('Введите вторую букву: '))

a = ord('a')

if first_letter > second_letter:
    low = second_letter
    high = first_letter
else:
    low = first_letter
    high = second_letter

print(f'{chr(first_letter)} стоит на {first_letter - a + 1} месте, \n'
      f'{chr(second_letter)} стоит на {second_letter - a + 1} месте \n'
      f'между ними {high - low} букв')