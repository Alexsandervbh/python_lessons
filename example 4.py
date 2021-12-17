# Задание 4

number = int(input("Введите целое положительное число: "))
r = -1
while number > 10:
    d = number % 10
    number //= 10
    if d > r:
        r = d
print(r)

