# Напишите программу, которая по заданному номеру четверти,
# показывает диапазон возможных координат точек в этой четверти (x и y).


num = int(input('Введите номер четверти: '))
if not 1 <= num <= 4:
    print('Нет такой четверти')
    exit(0)

if num == 1:
    print('x от 0 до +бесконечности \ny от 0 до +бесконечности')
elif num == 2:
    print('x от -бесконечности до 0 \ny от 0 до +бесконечности')
elif num == 3:
    print('x от -бесконечности до 0 \ny от -бесконечности до 0')
else:
    print('x от 0 до +бесконечности \ny от -бесконечности до 0')