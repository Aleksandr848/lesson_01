revenue = int(input('Какова выручка фирмы? '))
costs = int(input('Какие издержки у фирмы? '))
profit = revenue - costs
if revenue > costs:
    print(f'Фирма работает с прибылью. Рентабельность - {round(profit / revenue, 2)}')
elif costs > revenue:
    print('Фирма работает в убыток.')
else:
    print('Фирма работает в "ноль"')

if revenue > costs:
    staff = int(input('Введите количество работников фирмы: '))
    print(f'Прибыль фирмы в расчете на одного сотрудника - {round(profit / staff,2)}')
