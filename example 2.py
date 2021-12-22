# Задание 2

a = input("Укажите значение через пробел:  ").split(" ")
max_index = len(a) -1

for index in range(0, max_index, 2):
    next_index = index +1
    a[index], a[next_index] = a[next_index], a[index]

print(a)