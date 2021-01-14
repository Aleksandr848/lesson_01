number = input('Введите целое положительное число: ')
while len(number) < 2:
    number = input('Введите число больше или равно 10: ')
int_number = int(number)
max_numeral = 0 # Присваиваем для начала максимальной цифре значение 0
while int_number > 0:
    last_numeral = int_number % 10 # последняя цифра
    int_number = int(int_number / 10) # удаляем последнюю цифру у числа
    if last_numeral >= max_numeral:
        max_numeral = last_numeral # Если последняя цифра больше или равно максимальной цифре, то её значение становится максимальным
print(f'Максимальная цифра в числе {number} - {max_numeral}.')