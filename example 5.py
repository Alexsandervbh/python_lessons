# Задание 5

Rating_list = [10, 9, 9, 8, 7, 6, 5, 5, 4, 3]
print(Rating_list)
number_retings = int(input("Введите значение рейтинга Rating_list: "))
Rating_list.append(number_retings)
Rating_list.sort(reverse=True)
print(Rating_list)

