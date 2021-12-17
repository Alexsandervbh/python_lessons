# Задание 6

start = int(input("Пробежал в первый день >>> "))
finish = int(input("Необходимо пробежать >>> "))
day = 1
print(f"В день {day} пробежал {start:.2f}")
while start < finish:
    start *= 1.1
    day += 1
    print(f"В день {day} пробежал {start:.2f}")
print(f"На {day} день, спортсмен достиг результата.")