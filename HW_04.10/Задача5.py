# Даны два файла, в каждом из которых находится запись многочлена.
# Задача - сформировать файл, содержащий сумму многочленов.
# Коэффициенты могут быть как положительными, так и отрицательными.
# Степени многочленов могут отличаться.


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


def get_coefficients_from_polynomial(polynomial):
    a = polynomial.split()
    i = 0
    while i < len(a):
        if a[i] == '+':
            a.remove('+')
            i -= 1
        elif a[i] == '-':
            a.remove('-')
            a[i] = '-' + a[i]
            i -= 1
        else:
            a[i] = a[i].split('*')
            a[i][0] = int(a[i][0])
            if len(a[i]) == 2:
                if a[i][1] == 'x':
                    a[i][1] = 1
                else:
                    a[i][1] = int(a[i][1][2:])
            else:
                a[i].append(0)
        i += 1
    result = [0] * (a[0][1] + 1)
    for i in a:
        result[i[1]] = i[0]
    return result


def sum_polynomials_coefficients(p1, p2):
    result = []
    if len(p1) < len(p2):
        p1 = p1 + [0] * (len(p2) - len(p1))
    else:
        p2 = p2 + [0] * (len(p1) - len(p2))
    for i in range(len(p1)):
        result.append(p1[i] + p2[i])
    return result


p1_file = open("p1.txt", 'r')
p2_file = open("p2.txt", 'r')
p1_p2 = open("p1 + p2.txt", 'w')
p1 = p1_file.readline()
p2 = p2_file.readline()
p1_coefficients = get_coefficients_from_polynomial(p1)
p2_coefficients = get_coefficients_from_polynomial(p2)
p1_p2_coefficients = sum_polynomials_coefficients(p1_coefficients, p2_coefficients)
p1_p2.writelines(build_polynomial(p1_p2_coefficients))
# [6, -75, 60, -5, 9, 2]
