# Задание 3 Задайте список из n чисел последовательности (1+1/n)^n и выведите на экран их сумму,
# округлённую до трёх знаков после точки.


def f(n):
    result = []
    for i in range(1, n + 1):
        result.append((1 + 1 / i) ** i)
    return result


def sum_of_list(lst):
    result = 0
    for i in lst:
        result += i
    return result


num = 0
while num <= 0:
    num = int(input("Введите натуральное число: "))
sequence = f(num)
print(sequence)
print(round(sum_of_list(sequence), 3))
