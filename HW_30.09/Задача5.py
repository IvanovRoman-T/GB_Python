# Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.


def fib(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    elif n > 0:
        return fib(n - 1) + fib(n - 2)
    else:
        return fib(n + 2) - fib(n + 1)


def create_list_of_fib(n):
    result = []
    for i in range(-n, n + 1):
        result.append(fib(i))
    return result


num = int(input("Введите число: "))
print(create_list_of_fib(num))
