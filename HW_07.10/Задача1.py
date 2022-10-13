# Напишите программу, удаляющую из текста все слова, содержащие ""абв"".


with open("ex1.txt", 'w') as file:
    file.writelines("абв фыовйзцщ ырфвабврл цфыщвшзщфышвх")
with open("ex1.txt", 'r') as file:
    string = file.readline().split()
result = list(filter(lambda x: "абв" not in x, string))
with open("ex1_result.txt", 'w') as file:
    file.writelines(" ".join(result))
