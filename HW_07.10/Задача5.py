# Дан список чисел. Создайте список, в который попадают числа,
# описываемые возрастающую последовательность. Порядок элементов менять нельзя.
# [1, 5, 2, 3, 4, 6, 1, 7] => [1, 2, 3] или [1, 7] или [1, 6, 7] и т.д.
# Входные и выходные данные хранятся в отдельных текстовых файлах.


def is_it_increasing_sequence(nums):
    for i in range(len(nums) - 1):
        if nums[i] >= nums[i + 1]:
            return False
    return True


def go_to_next(indexes, length, num_of_try):
    if indexes == list(range(length - len(indexes), length)):
        return False
    if indexes[-num_of_try] + 1 > length - num_of_try:
        return go_to_next(indexes, length, num_of_try + 1)
    k = indexes[len(indexes) - num_of_try]
    for i in range(len(indexes)):
        if not i < len(indexes) - num_of_try:
            indexes[i] = k + i - (len(indexes) - num_of_try) + 1
    return indexes


def f(nums):
    for length in range(2, len(nums) + 1):
        indexes = [i for i in range(length)]
        while True:
            print(indexes)
            seq = [nums[x] for x in indexes]
            if is_it_increasing_sequence(seq):
                with open("ex5_result.txt", "a") as file:
                    file.writelines(" ".join(list(map(str, seq))) + "\n")
            indexes = go_to_next(indexes, len(nums), 1)
            if not indexes:
                break


with open("ex5_input.txt", "w") as file:
    file.writelines("1 5 2 3 4 6 1 7")
with open("ex5_input.txt", "r") as file:
    numbers = list(map(int, file.readline().split()))
with open("ex5_result.txt", "w") as file:
    file.writelines("")
f(numbers)
