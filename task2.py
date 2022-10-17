# Задача 2. В файле находятся названия фруктов. Выведите все фрукты, названия которых начинаются на заданную букву.

fr = open('fr.txt', encoding='utf-8')
text = fr.readlines()
fr.close()

sym = input("Введите букву: ")

for line in text:
    if line[0] == sym:
        print(line)