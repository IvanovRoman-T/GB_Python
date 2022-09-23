# Напишите программу для. проверки истинности утверждения
# ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.


print('  X | Y | Z | ¬(X ⋁ Y ⋁ Z) | ¬X ⋀ ¬Y ⋀ ¬Z')
for x in 0, 1:
    for y in 0, 1:
        for z in 0, 1:
            res1 = int(not(x or y or z))
            res2 = int(not x and not y and not z)
            print(f'  {x}   {y}   {z}{9 * " "}{res1}{15 * " "}{res2}')