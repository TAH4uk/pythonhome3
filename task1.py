# Задача 1. Создайте файл. Запишите в него N первых элементов последовательности Фибоначчи.

fib = int(input("Введите число первых N элементов последовательности Фибоначчи: "))

def fibonacci(n):
    a, b = 1, 1
    for i in range(n):
        yield a
        a, b = b, a + b

data = str(list(fibonacci(fib)))

with open("fib.txt", "w") as file:
    file.writelines(data)