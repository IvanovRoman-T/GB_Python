# Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.


def factorize(num):
    factors = []
    while num % 2 == 0:
        factors.append(2)
        num /= 2
    for i in range(3, int(num) + 1, 2):
        if num == 1:
            break
        if num % i == 0:
            factors. append(i)
            num /= i
    return factors


number = int(input("Введите натуральное число: "))
print(f"Простые делители числа {number}: {factorize(number)}")
