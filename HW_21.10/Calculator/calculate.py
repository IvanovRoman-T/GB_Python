from expression import form_answer


def sum_(a, b):
    result = [a[0] + b[0], a[1] + b[1]]
    return result


def diff_(a, b):
    result = [a[0] - b[0], a[1] - b[1]]
    return result


def mult_(a, b):
    result = [a[0] * b[0] - a[1] * b[1], a[0] * b[1] + a[1] * b[0]]
    return result


def quot_(a, b):
    result = [(a[0] * b[0] + a[1] * b[1]) / (b[0] * b[0] + b[1] * b[1]),
              (- a[0] * b[1] + a[1] * b[0]) / (b[0] * b[0] + b[1] * b[1])]
    return result


def operation(expr):
    if expr[1] == '+':
        return form_answer(expr, sum_(expr[0], expr[2]))
    elif expr[1] == '-':
        return form_answer(expr, diff_(expr[0], expr[2]))
    elif expr[1] == '*':
        return form_answer(expr, mult_(expr[0], expr[2]))
    elif expr[1] == '/':
        return form_answer(expr, quot_(expr[0], expr[2]))
    else:
        return ''
