# Задание 1 Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.


def sum_of_digits(number):
    result = 0
    for i in number:
        if i.isdigit():
            result += int(i)
    return result


num = input("Введите вещественное число: ")
print(sum_of_digits(num))
