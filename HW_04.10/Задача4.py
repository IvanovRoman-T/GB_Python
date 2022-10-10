# Задана натуральная степень k. Сформировать случайным образом список коэффициентов
# (значения от 0 до 100) многочлена и записать в файл многочлен степени k.


import random


def create_random_coefficients(k):
    result = []
    for i in range(k + 1):
        result.append(random.randrange(-100, 101))
    return result


def build_polynomial(coefficients):
    result = ""
    for i in range(len(coefficients) - 1, 1, -1):
        if coefficients[i] != 0:
            if len(result) == 0:
                if coefficients[i] == 1:
                    result += f"x^{i}"
                elif coefficients[i] == -1:
                    result += f"-x^{i}"
                else:
                    result += f"{coefficients[i]}*x^{i}"
            else:
                if coefficients[i] == 1:
                    result += f" + x^{i}"
                elif coefficients[i] == -1:
                    result += f" - x^{i}"
                else:
                    if coefficients[i] > 0:
                        result += " + "
                    else:
                        result += " - "
                    result += f"{abs(coefficients[i])}*x^{i}"
    if len(coefficients) > 1:
        if coefficients[1] != 0:
            if coefficients[1] == 1:
                result += f" + x"
            elif coefficients[1] == -1:
                result += f" - x"
            else:
                if coefficients[1] > 0:
                    result += " + "
                else:
                    result += " - "
                result += f"{abs(coefficients[1])}*x"
    if len(result) == 0:
        result += f"{coefficients[0]}"
    else:
        if coefficients[0] != 0:
            if coefficients[0] > 0:
                result += " + "
            else:
                result += " - "
            result += f"{abs(coefficients[0])}"
    return result


k = int(input("Введите степень многочлениа: "))
file = open('Вывод задачи 4.txt', 'w')
a = build_polynomial(create_random_coefficients(k))
file.writelines(a)
print(a)
