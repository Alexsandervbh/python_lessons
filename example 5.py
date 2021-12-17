# Задание 5

revenue = int(input("Ведите выручку >>> "))
costs = int(input("Ведите затраты >>> "))

profit = revenue - costs
if  revenue > costs:
    print(f"Выручка фирмы составила {profit} ")
    print(f"Рентабельность фирмы составила  {int(profit / revenue * 100)}%")
    people = int(input("Колличество сотрудников >>> "))
    print(f"Прибыль фирмы в расчете на одного человека  {profit / people:.2f}")
else:
    print(f"Фирма отработала в убыток.")