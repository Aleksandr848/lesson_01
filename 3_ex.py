number = input('Введите число: ') # получаем число в формате "строка"
double_number = number + number # конкатенация двух строковых значений
triple_number = number + number + number # конкатенация трёх строковых значений

sum_number = int(number) + int(double_number) + int(triple_number) # переводим строку в число и находим сумму

print(sum_number)
