# Задание 2 Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.


def f(n):
    result = [1]
    for i in range(2, n + 1):
        result.append(result[-1] * i)
    return result


num = 0
while num <= 0:
    num = int(input("Введите натуральное число: "))
print(f(num))
