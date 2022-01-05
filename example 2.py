# Задание 2.
# Создать текстовый файл (не программно), сохранить в нем несколько строк, выполнить подсчет
# количества строк, количества слов в каждой строке.

def count_info():
    try:
        with open('file1.txt', 'r', encoding="utf-8") as file:
            list = file.readlines()
            for x in range(len(list)):
                new_l = list[x].split()
                print(f'Количество строк в файле {len(list)}. В {x + 1}-ой строке {len(new_l)} слов(а)')
    except FileNotFoundError:
        return 'Файл не найден.'


count_info()