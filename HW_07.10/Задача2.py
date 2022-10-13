'''
Создайте программу для игры с конфетами человек против человека.
Условие задачи: На столе лежит 2021 конфета. Играют два игрока делая ход друг после друга.
Первый ход определяется жеребьёвкой. За один ход можно забрать не более чем 28 конфет.
Все конфеты оппонента достаются сделавшему последний ход. Сколько конфет нужно взять первому игроку,
чтобы забрать все конфеты у своего конкурента?
a) Добавьте игру против бота
b) Подумайте как наделить бота ""интеллектом""
'''


from random import randrange


def player_move(candies):
    inp = 0
    while not 0 < inp < 29 and not 1 < inp < candies:
        a = input("Введите колличество конфет, которое хотите взять: ")
        try:
            inp = int(a)
        except ValueError:
            print("Некорректный ввод")
        else:
            if inp > candies:
                print("Вы не можете взять больше конфет, чем есть на столе")
            elif not 0 < inp < 29:
                print("Вы не можете взять меньше 1 или больше 28 конфет")
    return inp


def bot_move(candies):
    if candies % 29 == 0:
        return randrange(1, 29)
    else:
        return candies % 29


def game(mode, candies):
    if mode == '1':
        i = 0
        while candies > 0:
            print(f"На столе сейчас {candies} конфет(а)")
            print(f"Ход Игрока {i + 1}")
            candies -= player_move(candies)
            if candies == 0:
                print(f"Поздравляю, Игрок {i + 1}, вы победили!!!")
            i = (i + 1) % 2
    if mode == '2':
        while candies > 0:
            print(f"На столе сейчас {candies} конфет(а)")
            print(f"Ход Игрока")
            candies -= player_move(candies)
            if candies == 0:
                print(f"Поздравляю, Игрок, вы победили!!!")
            else:
                b = bot_move(candies)
                print(f"Бот взял {b} конфет")
                candies -= b
                if candies == 0:
                    print("К сожалению, бот вас обыграл.")


m = 0
while m != "1" and m != "2":
    m = input("Введите 1, чтобы играть друг с другом, или 2, чтобы играть против бота: ")
num_of_candies = int(input("Введите начальное количество конфет: "))
game(m, num_of_candies)
