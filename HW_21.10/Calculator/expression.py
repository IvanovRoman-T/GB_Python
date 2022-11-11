def get_number(num):
    num = num.replace(' ', '')
    if 'i' in num:
        if '+' in num:
            num = num.split('+')
            if num[1] == 'i':
                num[1] = '1i'
            if num[1] == '-i':
                num[1] = '-1i'
            try:
                return [float(num[0]), float(num[1][:-1])]
            except ValueError:
                return ['', '']
        elif '-' in num:
            num = [num[:num.rfind('-')], num[num.rfind('-'):]]
            if num[0] == '':
                num[0] = '0'
            if num[1] == 'i':
                num[1] = '1i'
            if num[1] == '-i':
                num[1] = '-1i'
            try:
                return [float(num[0]), float(num[1][:-1])]
            except ValueError:
                return ['', '']
        else:
            if num == 'i':
                num = '1i'
            elif num == '-i':
                num = '-1i'
            try:
                return [0.0, float(num[:-1])]
            except ValueError:
                return ['', '']
    else:
        try:
            return [float(num), 0.0]
        except ValueError:
            return ['', '']


def get_expression(expr):
    expr = expr.replace(' ', '')
    expression = [get_number(expr[expr.find('(') + 1:expr.find(')')]),
                  expr[expr.find(')') + 1],
                  get_number(expr[expr.rfind('(') + 1:expr.rfind(')')])]
    return expression


def form_number(num):
    if num[1] == 0:
        if num[0] % 1 != 0:
            return str(num[0])
        else:
            return str(int(num[0]))
    if num[0] == 0:
        if num[1] % 1 != 0:
            return f"{num[1]}i"
        else:
            if num[1] == 1 or num[1] == -1:
                return f"{str(num[1])[:-3]}i"
            else:
                return f"{int(num[1])}i"
    if num[1] > 0:
        sgn = '+'
    else:
        sgn = '-'
    num[1] = abs(num[1])
    if num[0] % 1 != 0:
        a = str(num[0])
    else:
        a = str(int(num[0]))
    if num[1] % 1 != 0:
        b = f"{num[1]}i"
    else:
        if num[1] == 1:
            b = "i"
        else:
            b = f"{int(num[1])}i"
    return f"{a} {sgn} {b}"


def form_answer(expr, res):
    num1 = form_number(expr[0])
    num2 = form_number((expr[2]))
    result = form_number(res)
    return f"({num1}) {expr[1]} ({num2}) = {result}"
