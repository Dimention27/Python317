
# Задача 2
# for i in range(1, 10, 2):
#     print("++++++++++++++++")
#     for j in range(1):
#         print("----------------")

# Задача 1
# i = int(input("Количество символов: "))
# j = input("Тип символа: ")
# print("0 - горизонтальная")
# print("1 - вертикальная")
# o = int(input("Ориетация линии: "))
# if o == 0:
#     print(j * i)
# else:
#     print(('\n' + j) * i)


# Задача 3

# a = int(input("-> "))
# b = int(input("-> "))
# c = int(input("-> "))
# if (a >= b) and (a >= c):
#     maximum = a
# elif (b >= a) and (b >= c):
#     maximum = b
# else:
#     maximum = c
# print("Максимальное значение: ", maximum)


# Задача 4

print("Выберите операцию: \n"
      '1 - "r" - применяет унарный минус к операнду \n'
      '2 - "+" - сложение \n'
      '3 - "-" - вычитание \n'
      '4 - "/" - деление \n'
      '5 - "*" - умножение \n'
      '6 - "%" - деление по модулю (остаток от деления) \n'
      '7 - "<" - минимальное из двух чисел \n'
      '8 - ">" - максимальное из двух чисел \n')
p = 1
q = 2
w = 3
e = 4
r = 5
t = 6
u = 7
i = 8
a = int(input("Введите цифру: "))
b = int(input("Введите первое число: "))
c = int(input("Введите второе число: "))
if a == 1:
    print()
elif a == 2:
    print(b + c)
elif a == 3:
    print(b - c)
elif a == 4:
        print(b / c)
elif a == 5:
    print(b * c)
elif a == 6:
    print(b % c)
elif a == 7:
    if b > c:
        print(c)
    else:
        print(b)
elif a == 8:
    if b < c:
        print(c)
    else:
        print(b)

# Не понятно стало с унарным минусом, как лучше это реализовать( не разобрался) ) и также с запретом на деление на 0

