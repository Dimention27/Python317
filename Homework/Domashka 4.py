# Задача 1


a = 25
n = 0
p = int(input("Введите число от 1 до 100: "))
for i in range(1, 101):
    if p < a:
        print("Загаданное число больше")
        n += 1
    if p > a:
        print("Загаданое число меньше")
        n += 1
    if p == a:
        print("Вы угадали загаданное число c ", n, "раза")
        n += 1
    break
    if a == 0:
        print("Выход")



# Задача 2

# a = [0] * int(input("Количество элементов в списке: "))
# for i in range(len(a)):
#     a = int(input("-> "))
#     if a % 2:
#         print(a, end=" ")
#
# b = int(input("n = "))
# for i in range(b):
#     b = int(input("-> "))
#     if b % 2:
#         print(b)