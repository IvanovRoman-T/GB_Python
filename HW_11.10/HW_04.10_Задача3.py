# Задайте последовательность чисел. Напишите программу,
# которая выведет список неповторяющихся элементов исходной последовательности.


# Было:
# def find_unique(lst):
#     result = []
#     for i in lst:
#         if lst.count(i) == 1:
#             result.append(i)
#     return result
#
#
# numbers = list(map(float, input("Введите список чисел через пробел:\n").split()))
# print(find_unique(numbers))


# Стало:
s = ''
numbers = list(map(float, input("Введите список чисел через пробел:\n").split(', ')))
print(list(filter(lambda x: numbers.count(x) == 1, numbers)))
