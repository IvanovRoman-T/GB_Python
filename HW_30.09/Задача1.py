# Задайте список из нескольких чисел. Напишите программу,
# которая найдёт сумму элементов списка, стоящих на нечётной позиции.


def sum_odd_positions(lst):
    result = 0
    for i in range(1, len(lst), 2):
        result += lst[i]
    return result


numbers = [2, 3, 5, 9, 3]
print(sum_odd_positions(numbers))
