# Напишите программу, которая найдёт произведение пар чисел списка.
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.


def multiply_pairs(lst):
    result = []
    for i in range((len(lst) + 1) // 2):
        result.append(lst[i] * lst[-i - 1])
    return result


numbers = [2, 3, 4, 5, 6]
print(multiply_pairs(numbers))
