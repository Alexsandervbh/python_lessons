# Задание 3
seasons = {'Winter-Зима': (1, 2, 12),
           'Sping-Весна': (3, 4, 5),
           'Summer-Лето': (6, 7, 8),
           'Autumn-Осень': (9, 10, 11)}
month = int(input('write a month: '))
for key in seasons.keys():
    if month in seasons[key]:
        print(key)



