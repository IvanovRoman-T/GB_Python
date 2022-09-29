# Задание 5 Реализуйте алгоритм перемешивания списка.


from random import randrange


def shuffle(lst):
    result = []
    indexes = []
    for i in range(len(lst)):
        ind = randrange(len(lst))
        while ind in indexes:
            ind = randrange(len(lst))
        result.append(lst[ind])
        indexes.append(ind)
    return result


list_ = input("Введите элементы списка через пробел:\n").split()
print(' '.join(shuffle(list_)))
