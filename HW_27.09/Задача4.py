# Задание 4 Задайте список из N элементов, заполненных числами из промежутка [-N, N].
# Найдите произведение элементов на позициях a и b.
# Значения N, a и b вводит пользователь с клавиатуры.


def create_list(n):
    result = [0]
    for i in range(1, n + 1):
        result.insert(0, -i)
        result.append(i)
    return result


num = int(input("Введите целое число n: "))
a, b = map(int, input("Введите 2 целых числа от 1 до 2n+1: ").split())
lst = create_list(num)
print(lst)
print(lst[a - 1] * lst[b - 1])
