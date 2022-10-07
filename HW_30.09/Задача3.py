# Задайте список из вещественных чисел. Напишите программу,
# которая найдёт разницу между максимальным и минимальным значением дробной части элементов.


def f(lst):
    min_ = 1
    max_ = 0
    for i in lst:
        k = i - int(i)
        if k != 0:
            if k > max_:
                max_ = k
            if k < min_:
                min_ = k
    return max_ - min_


numbers = [1.1, 1.2, 3.1, 5, 10.01]
print(round(f(numbers), 2))
