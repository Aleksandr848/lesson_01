time = int(input('Введите время в секундах: '))

hours = int(time / 3600)
time = time % 3600 # считаем сколько осталось секунд после первого действия

minutes = int(time / 60)
seconds = time % 60 # считаем сколько осталось секунд после второго действия

print(f'Итого: {hours}:{minutes}:{seconds}')
