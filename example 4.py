text = input("Введите текст: ").split()

for index,value in enumerate(text, start = 1):
 print(f"{index}, {value[:10]}")
