# name = "Dmitry"
# print("Hello", name)
# age = 20
# print(type(age))
# print(id(age))
# age = "hello"
# print(type(age))
import random
import time

# a = b = c = 1
# print(a, b, c)

# a, b, c = 5, "Hello", 9.2
# print(a, b, c)
#
# PI = 3.14
# print(PI)
# PI = 2
# print(PI)
#
# print(type(2))

# a = "5"
# b = 2
# print(int(a) + b)

# a = 1
# b = 2
# print("a =", a)
# print("b =", b)
# # c = a
# # a = b
# # b = c
# # a = a + b  # a = 3
# # b = a - b  # b = 3 - 2 = 1
# # a = a - b  # a = 3 - 1 = 2
# a, b = b, a
# print("a =", a)
# print("b =", b)

# print("cnhj")
# print('sdff')

# s1 = "Hello"
# s2 = "Python"
# print(s1 + " " + s2)

# s1 = "Hello"
# s2 = "Python"
# s3 = s1 + " " + s2 + "!\t\t"
# print(s3)
# print(s3 * 5)


# num = 10
# num += 5  #num = num +5
# print(num)  #15
#
# num -= 3  #num = num - 3
# print(num)  #12


# # Задача
#
# num = 4321  #432
# a = num % 10
# # print(a)
# num = num // 10
# # print(num)
# b = num % 10
# print(b)
# num = num // 10
# # print(num)
# c = num % 10
# print(c)
# num = num // 10
# # print(num)
# d = num % 10
# # print(d)
#
# print(a * 1000 + b * 100 + c * 10 + d)

# num = 4321
# res = num % 10 * 1000
# print(res)


# Функции явного преобразования типов
# str()
# int()
# float()
# bool()

# num1 = '2.5'
# num2 = 3
# res = int(float(num1)) + num2
# print(res)

# print(int(3.8))
# a = round(3.8)
# print(a)
# print(type(a))
# b = round(3.89446546, 2)
# print(b)
# print(type(b))


# name = 'Виктор'
# age = 28
# print("Меня зовут", name, ". Мне", age, "лет.")
# print("Меня зовут " + name + ". Мне " + str(age) + " лет.")
# print("Меня зовут", name, ". Мне", age, "лет.", sep=" ", end=" ")
# print("Я учу Python.")

# name = input("Ваше имя: ")
# print(name)


# Число 5 в степени 2 равно 25

# num = input("Введите число: ")
# step = input("Введите степень: ")
# res = int(num) ** int(step)
# print("Число",num,"в степени",step,"равно",res)
# либо
# num = int(input("Введите число: "))
# step = int(input("Введите степень: "))
# res = num ** step
# print("Число",num,"в степени",step,"равно",res)


# b1 = True  #1
# b2 = False  #0
# print(b1 + 5)
# print(b2 + 5)

# print(bool("Python"))
# print(bool(""))  # False
# print(bool("0"))  # False
# print(bool(5))
# print(bool(False))  #False
# print(bool(None))  #False


# print(7 == 7)
# print(2 + 5 == 7)
# print(8 > 7)
# print(8 < 7)
# print(8 <= 8)
# print(8 >= 8)

# print(2 < 4 < 9)  # True True
# print(2 < 10 < 9)  # True && False
# print(3 * 3 <= 7 >= 2)  # False && True

# a = 10
# b = 5
# c = a == b
# print(a, b, c)

# print(5 - 3 == 2 and 1 + 3 == 4)  # True (True:True)
# print(5 - 3 == 2 and 1 + 3 < 4)  # False (True:False)

# print(5 - 3 == 2 or 1 + 3 == 4)  # True (True:True)
# print(5 - 3 == 2 or 1 + 3 < 4)  # True (True:False)

# print(not 9 - 5)
# print(not 5 - 5)


# cnt = 15
# if cnt < 10:
#     cnt += 1
# print(cnt)

# age = int(input("Введите свой возраст: "))
# if age >= 18:
#     print("Доступ на сайт разрешен")
# else:
#     print("Доступ запрещён")

# a = 45
# b = 35
# if a > b:
#     print("a > b")
# elif b > a:
#     print("b > a")
# else:
#     print("a == b")

# side1 = int(input("Введите первую сторону: "))
# side2 = int(input("Введите вторую сторону: "))
# side3 = int(input("Введите третью сторону: "))
# if side1 == side2 == side3:
#     print("Треугольник равносторонний")
# elif side1 == side2 or side1 == side3 or side2 == side3:
#     print("Треугольник равнобедренный")
# else:
#     print("Треугольник разносторонний")


# day = int(input("Введите день недели (цифрой): "))
# if 1 <= day <= 5:  # (day >= 1) and (day <= 5)
#     print("Рабочий день - ", end="")
#     if day == 1:
#         print("Понедельник")
#     if day == 2:
#         print("Вторник")
#     if day == 3:
#         print("Среда")
#     if day == 4:
#         print("Четверг")
#     if day == 5:
#         print("Пятница")
# elif day == 6 or day == 7:
#     print("выходной день - ", end="")
#     if day == 6:
#         print("Суббота")
#     if day == 7:
#         print("Воскресенье")
# else:
#     print("Такого дня недели не существует")


# m = int(input("Введите номер месяца: "))
# if m == 12 or m == 1 or m == 2:
#     print("Зима")
# elif 3 <= m <= 5:
#     print("Весна")
# elif 6 <= m <= 8:
#     print("Лето")
# elif 9 <= m <= 11:
#     print("Осень")
# else:
#     print("Ошибка ввода данных")


# n = int(input("Введите количество ворон: "))
# if 0 <=n <= 9:
#     print("На ветке", n, end=" ")
#     if n == 1:
#         print("ворона")
#     elif 2 <= n <= 4:
#         print("вороны")
#     else:
#         print("ворон")
# else:
#     print("Ошибка ввода")


# Занятие 3

# password = "qwerty"
#
# match password:
#     case 'admin':
#         print('Администратор')
#     case 'user':
#         print('Пользователь')
#     case 'moderator':
#         print('Модератор')
#     case _:
#         print('Пароль не верен')


# day = 'суббота'
# time = 8
#
# match day:
#     case "понедельник" | "вторник" | "среда" | "четверг" | "пятница" if time >=9:
#         print('Рабочий день')
#
#     case 'суббота' | 'воскресенье':
#         print("Выходной день")
#     case _:
#         print("Такого дня недели не существует")


# a, b = 10, 20
#
# minim = a if a < b else b
# print(minim)

# a, b = 10, 20
# print("a == b" if a == b else "a > b" if a > b else "b > a")

# Задача


# x = int(input('Делимое: '))
# y = int(input('Делитель: '))
# print(x / y if y != 0 else 'На ноль делить нельзя!')


# Исключения

# try:
#     n = int(input("Введите делимое: "))
#     m = int(input("Введите делитель: "))
#     print(n / m)
# except ValueError:
#     print("Нельзя вводить строки")
# except ZeroDivisionError:
#     print("Нельзя делить на ноль")


# try:  # попытаться выполнить
#     n = int(input("Введите делимое: "))
#     m = int(input("Введите делитель: "))
#     print(n / m)
# except (ValueError, ZeroDivisionError):  # исключение
#     print("Нельзя вводить строки и делить на ноль")
# else:  # когда в блоке try не возникло исключения
#     print("все нормально. Вы ввели числа", n, "и", m)
# finally:  # выполняется в любом случае
#     print("конец программы")


# Задача


# n = input("Введите первое число: ")
# m = input("Введите второе число: ")
#
# try:
#     n = int(n)  #2
#     m = int(m)  # пять
# except ValueError:
#     n = str(n)  # '2'
# finally:
#     print(n + m)


# Циклы
# i = 0
# while i < 5:
#     print("i =", i)
#     i += 1  # i = i + 1


# i = 2
# while i <= 20:
#     print("i =", i, end=" ")
#     i += 2
#
# i = 1
# while i <= 10:
#     print(i * 2)
#     i += 1


# i = 1
# while i <= 20:
#     if i % 2 == 0:
#         print(i, end=" ")
#     i += 1


# Задача

# try:
#     n = int(input("Укажите количество символов: "))
#     while n > 0:
#         print('*', end="")
#         n -= 1
# except ValueError:
#     print("Введите число!")
#
# num = int(input("Введите число: "))
# i = 0
# string = ""
# while i < num:
#     string += "*"
#     i += 1
# print(string)

# x = int(input('Количество: '))
# print('*' * x)


# Задача

# a = int(input('Начало диапазона: '))
# b = int(input('Конец диапазона: '))
# if a % 2 == 0:
#     a += 1
# sum1 = 0
# while a <= b:
#     sum1 += a
#     a += 2;
# print('Сумма нечетных: ', sum1)


# i = int(input("Start: "))  # 1
# j = int(input("End: "))  # 3
# sum1 = 0
# if i < j:
#     i, j = j, i
# while i <= j:
#     if i % 2 != 0:
#         sum1 += i  # 1 + 3
#     i += 1
#
# print(sum1)


# n = input("Введите целое число: ")
#
# while type(n) != int:
#     try:
#         n = int(n)
#     except ValueError:
#         print("Число не целое!")
#         n = input("Введите целое число: ")
# if n % 2 == 0:
#     print("Четное")
# else:
#     print("Нечетное")


# i = 0
# while i < 10:
#     if i == 3:
#         i += 1
#         continue
#     print(i, end=" ")
#     if i == 5:
#         break
#     i += 1
# print("\nЦикл завершен")


# i = 0
# while True:
#     print(i)
#     if i == 5:
#         break
#     i += 1


# while True:
#     n = int(input("Введите положительное число: "))
#     if n < 0:
#         break

# m = 1
# while True:
#     n = int(input("Введите положительное число: "))
#     if n == 0:
#         break
#     m *= n
# print("Произведение равно: ", m)


# i = 0
# while i < 10:
#     if i == 9:
#         i += 1
#         continue
#     print(i)
#     i += 1
# else:
#     print("Цикл окончен, i =", i)


# i = 1
# while i < 5:
#     print("Внешний цикл: i =", i)
#     j = 1
#     while j < 4:
#         print("\tВнутренний цикл: j =", j)
#         j += 1
#     i += 1


# Задача

# i = 1
# while i < 10:
#     j = 1
#     while j < 10:
#         print(i, '*', j, '=', i * j, '\t\t', end='')
#         j += 1
#     print()
#     i += 1


# Занятие 4


# for element in collection:
#   тело цикла

# for i in "Hello", "red", "blue", "yellow", 20, 0.3:
#     print(i)

# print(range(5))

# range(start, stop, step)

# for i in range(5, 100, 5):
#     print(i, end=" ")
# print()
# # или
# i = 5
# while i < 100:
#     print(i, end=" ")
#     i += 5

# Задача 10

# a = int(input("Введите целое число: "))
# for i in range(1, a + 1):
#     if a % i == 0:
#         print(i, end=" ")

# Задача 11

# for i in range(11, 100, 11):
#     print(i, end=" ")
#
# for i in range(3):
#     print(i, end=" ")
#     if i == 1:
#         break
# else:
#     print('\ndone')


# for i in range(3):
#     print("+++", i)
#     for j in range(2):
#         print("------", j)

# Задача 12

# w = int(input("Введите ширину прямоугольника: "))
# h = int(input("Введите высоту прямоугольника: "))
# for i in range(h):
#     for j in range(w):
#         print("*", end="")
#     print()

# Задача 13

# w = int(input('W = '))
# h = int(input('H = '))
# for i in range(h):
#     for j in range(w):
#         if i == 0 or j == 0 or i == h - 1 or j == w - 1:
#             print('*', end='')
#         else:
#             print(' ', end='')
#     print()


# letter = [i for i in "Hello"]
# print(letter)

# num = [i for i in range(30) if i % 2 == 0]
# print(num)


# Списки (list)

# nums = [8, 3, 9, 4, 1, "Hello", 2.3]
# print(nums)
# print(type(nums))
#
# print(nums[0])
# print(nums[3])
# print(nums[-1])
#
# nums[-2] = 2
# nums[1] += 100
# print(nums)
# print(len(nums))

# s = []
# print(s)
# # или
# b = list()
# print(b)
#
# c = list("Hello")
# print(c)

# s = [5] * 6
# print(s)
#
# a = [1, 2, 3]
# b = [4, 5]
# c = a + b
# print(c)


# n = list(range(10))
# print(n)


# [выражение for переменная in последовательность]

# n = 5
# a = [i ** 2 for i in range(1, n + 1)]
# print(a)

# n = 5
# a = [i * 3 for i in "Hello"]
# print(a)

# a = [0] * int(input("Количество элементов в списке: "))
# print(a)
# for i in range(len(a)):
#     a[i] = int(input("-> "))
# print(a)

# короткий способ

# a = [input("-> ") for i in range(int(input("Количество элементов в списке: ")))]
# print(a)

# num = [8, 3, 9, 4, 1]
# print(num * 2)
# for i in range(len(num)):  # 0 1 2 3 4
#     print(num[i], end=" ")
# print()
# # или
# for i in num:  # 8 3 9 4 1
#     print(i, end=" ")


# Задача
#  Сумма отрицательных элементов

# a = [int(input('-->')) for i in range(int(input('n: ')))]
# summa = 0
# for i in a:
#     if i < 0:
#         summa += i
# print(summa)


# Задача

# a = list(range(21, 41))
# print(a)
# print()
# b = [i for i in range(21, 41)]
# print(b)


# a = list(range(21, 41))
# print(a)
# even = 0
# odd = 0
# for i in a:
#     if i % 2 == 0:
#         odd += 1
#     else:
#         even += i
# print('Четных: ', odd, 'Нечетных: ', even)


# Задача
# Найти среднее арифметическое всех ненулевых элементов

# a = [int(input('-> ')) for num in [0] * int(input('Count: '))]
#
# count = sum1 = 0
# for i in a:
#     if i != 0:
#         count += 1
#         sum1 += i
# print('Среднее: ', sum1 / count)


# Задача
# Выведите все элементы списка, которые больше предыдущего элемента

# a = [int(input('-->')) for i in range(int(input('n: ')))]
# print(a)
# for i in range(1, len(a)):
#     if a[i] > a[i - 1]:  # a[0] = 7 > a[0 - 1] = 2
#         print(a[i], end=" ")

# a = [9, 1, 3, 4, 5]
# print(a)
# a[0], a[-1] = a[-1], a[0]
# print(a)


#  Список[start:stop:step]

# a = [9, 4, 3, 1, 5, 17]
# print(a)
# print(a[1:4])
# print(a[::-1])
# print(a[:])

# Задача
# Создать срезы из списка

# [1, 2, 3, 4, 5, 6, 7]
# a = list(range(1, 8))
# print(a)
# print(a[::-1])
# print(a[::2])
# print(a[1::2])
# print(a[0:1])
# print(a[-1:])
# print(a[3:4])
# print(a[4:])
# print(a[-3:])
# print(a[-3:1:-1])
# print(a[2:5])


# Задача

# s = []
# n = int(input('Количество элементов списка: '))
# for num in range(n):
#     x = int(input('Введите число кратное 3:  '))
#     if x % 3 == 0:
#         s.append(x)
#     else:
#         print(x, 'не делится на 3 без остатка')
#         print(s)

# Задача

# a = [1, 2, 3]
# b = [11, 12, 13, 2, 4]
# c = []
# if len(b) > len(a):
#     for i in range(len(a)):
#         c.append(a[i])
#         c.append(b[i])
#     for i in range(len(a), len(b)):
#         c.append(b[i])
# else:
#     for i in range(len(b)):
#         c.append(a[i])
#         c.append(b[i])
#     for i in range(len(b), len(a)):
#         c.append(b[i])
# print(c)


# b = [11, 13, 12, 13, 2, 4, 13]
# b.remove(13)  # удаляет элемент из списка по значению, если элементов с заданным значением несколько,
# # то удаляется только первый
# print(b)
# a = 0
# if a in b:
#     b.remove(a)
# print(b)
#
#
# last = b.pop()  # с пустыми скобками - удаляет последний элемент из списка, с заданным индексом в скобках -
# # удаление по индексу
# print(b)
# print(last)
#
# b.clear()
# print(b)  # очищает список

# a = [9, 2, 7, 2, 4, 2, 3, 2]
# num = a.count(2)  # количество заданных значений в списке
# print(num)
# ind = a.index(2, 2, -1)  # возвращает первый индекс искомого значения. Также можно указать значения start и end
# print(ind)


# a = [9, 2, 7, 2, 4, 2, 3, 2]
# b = a.copy()
# print("a: ", a)
# print("b: ", b)
# a.append(20)
# print("a: ", a)
# print("b: ", b)


# a = [9, 2, 7, 2, 4, 2, 3, 2]
# print(a)
# a.reverse()  # перестраивает элементы списка в обратном порядке
# print(a)
# a.sort(reverse=True)  # сортирует список, по умолчанию - по возрастанию
# # reverse=True - по убыванию
# print(a)
#
#
# b = ["Виталий", "Сергей", "Александр", "Анна"]
# b.sort(key=len, reverse=True)
# print(b)

# c = sorted(a)
# print(c)
# print(a)


# Генерация случайных данных

# import random
#
# print(random.random())
# print(random.randint(2, 9))  # с 2 по 9 (включительно)
# print(random.randrange(2, 9, 2))


# from random import randint, randrange
#
# print(randint(2, 9))
# print(randrange(1, 9, 2))


# from random import *
#
# print(randint(2, 9))
# print(randrange(1, 9, 2))

# import random as r
#
# print(r.random())
# print(r.randint(2, 9))
# print(r.randrange(2, 9, 2))
# print(r.uniform(10.5, 25.5))
# print(round(r.uniform(10.5, 25.5), 3))
#
#
# city = ["Москва", "Новосибирск", "Воронеж", "Сочи", "Екатеринбург"]
# print(r.choice(city))
# print(r.choices(city, k = 3))
# r.shuffle(city)
# print(city)

# import random as r

# mas = [r.randint(0, 100) for i in range(10)]
# print(mas)

# lst = [5, 3, 2, 4, 1]
# print(len(lst))
# print(max(lst))
# print(min(lst))
# print(sum(lst))


# s = [8, 9, 6, 4, 7, 8, 2, 3]
# res = []
# for i in s:
#     if i % 2 == 0:
#         res.append(i)
#
# print(res)


# x = list("1a2b3c4c")
# print(x)
# print('a' in x)
# print('w' in x)
# print('a' not in x)

# lst = []
# if len(lst) == 0:
#     print("Список пустой")

# Задача

# from random import randint
# n1 = int(input("Введите размер первого списка: "))
# n2 = int(input("Введите размер второго списка: "))
# a = [randint(0, 10) for i in range(n1)]
# b = [randint(0, 10) for j in range(n2)]
# print("Первый список: ", a)
# print("Второй список: ", b)
# c = a + b
# print("Третий список: ", c)
# c = []
# for i in range(len(a)):
#     if a[i] not in c:
#         c.append(a[i])
# for i in range(len(b)):
#     if b[i] not in c:
#         c.append(b[i])
#     print("Элементы обоих списков без повторений", c)
# c = []
# for i in range(len(a)):
#     if a[i] in b and a[i] not in c:
#         c.append(a[i])
#     print("Элементы общие для двух списков: ", c)
# c = [min(a), min(b), max(a), max(b)]
# print(c)

# Задача

# import random
# n = int(input("Размер списка: "))
# s = []
# while len(s) < n:
#     num = random.randrange(n)
#     if num not in s:
#         s.append(num)
# print(s)
#
# # или
#
# from random import randint
# a = []
# n1 = int(input('Введите размер первого списка'))
# while len(a) < n1:
#     i = randint(0, n1 - 1)
#     if i not in a:
#         a.append(i)
# print(a)


# m = [
#     [1, 2, 3, 4],
#     [5, 6, 7, 8],
#     [9, 10, 11, 12]

# print(m)
# print(m[1][2])

# for row in range(len(m)):
#     # print(m[row])
#     for col in range(len([1, 2, 3, 4])):
#         print(m[row][col], end="\t\t")
#     print()

# или

# for row in m:
#     for x in row:
#         print(x, end="\t")
#     print()

# w, h = 5, 3
# matrix = [[0 for x in range(w)] for y in range(h)]
# print(matrix)

# или

# matrix = []
# for y in range(h):
#     new_row = []
#     for x in range(w):
#         new_row.append(0)
#     matrix.append(new_row)
#
# for row in matrix:
#     for x in row:
#         print()


# for x, y in [[1, 2], [3, 4], [5, 6], [7, 8]]:
#     print(x, "+", y, "=", x + y)


# from random import randint
#
# w, h = 5, 3
# matrix = [[randint(10, 100) for x in range(w)] for y in range(h)]
#
# for row in matrix:
#     for x in row:
#         print(x, end="\t")
#     print()

# Задача

# from random import randint
#
# w, h = 3, 4
# n = 0
# matrix = [[randint(-20, 10) for x in range(w)] for y in range(h)]
#
# for row in matrix:
#     for x in row:
#         print(x, end="\t")
#         if x < 0:
#             n += 1
#     print()
# print("Количество отрицательных чисел: ", n)

# from random import randint
#
# w, h = 3, 4
# n = 1
# matrix = [[randint(0, 4) for x in range(w)] for y in range(h)]
#
# for row in matrix:
#     for x in row:
#         print(x, end="\t")
#         if x != 0:
#             n += x
#     print()
# print("n = ", n)


# from random import randint
#
# w = h = 6
# n = 1
# matrix = [[randint(1, 100) for x in range(w)] for y in range(h)]
# for row in matrix:
#     for x in row:
#         print(x, end="\t")
#     print()
#
# s = []
# m = 101
# for i in range(w):
#     if m > matrix[i][i]:
#         m = matrix[i][i]
# print(m)
#
# # или
#
# s = []
# for i in range(w):
#     s.append(matrix[i][i])
# print(min(s))


# import math
#
# num1 = math.sqrt(4)
# num2 = math.ceil(3.2)
# num3 = math.floor(3.8)
#
# print(num1)
# print(num2)
# print(num3)


# I'll' be back!!!


# a = [1, 2, 3]
# b = [11, 22, 33]
# c = []
# for i in range(len(a)):
#     print(i)
#     c.append(a[i])
#     c.append(b[i])
# print(c)


# a = [1, 2, 3, 4, 5]
# b = [11, 22, 33]
# c = []
#    if len(a) > len(b):
#     a, b = b, a
#
#     for i in range(len(a)):
#         c.append(a[i])
#         c.append(b[i])
#     for i in range(len(a), len(b)):
#         c.append(b[i])
# print(c)


# a = [1, 2, 3, 4, 5]
# print(a)
# n = 2
# if n in i:
#     a.remove(n)     # удаление по значению, выбрасывает исключение ValueError - если элемента не существует
# print(a)


# a = [1, 3, 2, 3, 4, 3, 5]
# print(a)
# last = a.pop()  # удаляет последний элемент из списка и возвращает удаленный элемент
# print(last)
# print(a)
# second = a.pop(1) # удаляет элемент по заданному индексу(IndexError)
# print(second)
# print(a)
# a.clear()  # очищает список
# print(a)

# Задача


# a = [1, 5, 3, 2, 3, 4, 3, 5]
# print(a)
# num = a.count(3)  # возвращает кол-во заданных значений в списке
# print(num)
# ind = a.index(3, 3)  # возвращает индекс заданного значения
# print(ind)
# a.reverse()  # перестраивает элементы списка в обратном порядке
# print(a)
# a.sort(reverse=True)  # сортировка списка
# print(a)

# s = ["Виталий", "Сергей", "Александр", "Анна"]
# print(s)
# s.sort(key=len)
# print(s)
# print(len("Александр"))

# a = [1, 5, 3, 2, 3, 4, 3, 5]
# print(a)
# # a.sort()
# n = sorted(a)
# print("n=", n)
# print(a)


# a = [1, 2, 3]
# b = a.copy()  # возвращает копию списка
# print("a =", a, id(a))
# print("b =", b, id(b))
# a.append(20)
# b.append(120)
# print("a =", a, id(a))
# print("b =", b, id(b))

# Генерация случайных чисел

# import random
#
# print(random.random())   # от 0 до 1 (не включительно)
# print(random.randint(0, 9))  # от 0 до 9 (включительно)
# print(random.randrange(9))  # randrange(start, stop, step)  randrange(0, 9)
# print(random.uniform(10.5, 25.5), 2)


# mas = [random.randint(0, 100) for i in range(10)]
# print(mas)
# print(len(mas))
# print(min(mas))

# Задача

# mas = [random.randint(10, 100) for i in range(10)]
# print(mas)
# summa = max(mas)
# print("Max:", max(mas))
# mas.remove(summa)
# mas.insert(0, summa)
# print(mas)

# Задача

# mas = [random.randint(-20, 20) for i in range(10)]
# print(mas)
# mas.sort(reverse=True)
# print(mas)

# Задача

# mas = [random.randint(0, 100) for i in range(10)]
# print(mas)
# mini = min(mas)
# print("Min:", min(mas))
# ind = mas.index(mini)
# print("Index min:", ind)
# print(mas[ind:])
# или
# del mas[:ind]
# print(mas)


# lst = []
# # if len(lst) == 0:
# if not lst:
#     print("Список пустой")


# lst = [5, 6, 8, 9, 7]
# print(5 in lst)


# Задача

# import random
#
# n1 = int(input("Введите размер первого списка: "))
# n2 = int(input("Введите размер второго списка: "))
# a = [random.randint(0, 10) for i in range(n1)]
# b = [random.randint(0, 10) for j in range(n2)]
# c = a + b
# print("Первый список: ", a)
# print("Второй список: ", b)
# print("Третий список: ", c)
#
# c = []
# for i in range(len(a)):
#     if a[i] not in c:
#         c.append(a[i])
# for i in range(len(b)):
#     if b[i] not in c:
#         c.append(b[i])
# print("Элементы обоих списков без повторений:", c)
#
# c = []
# for i in range(len(a)):
#     if a[i] in b and a[i] not in c:
#         c.append(a[i])
# print("Элементы обоих списков без повторений:", c)
#
# c = [min(a), min(b), max(a), max(b)]
# print(c)


# m = [
#     [1, 2, 3, 4],
#     [5, 6, 7, 8],
#     [9, 10, 11, 12]
# ]
# print(m)
# # print(len(m))
# # print(m[1][2])
# print()
#
# for row in range(len(m)):
#     # print(m[row])
#     for col in range(len(m[row])):
#         print(m[row][col], end="\t")
#     print()

# или

# for row in m:
# print(row)
# for x in row:
#     print(x, end="\t")
# print()


# Генератор списка


# w, h = 5, 3
# matrix = [[0 for x in range(w)]for y in range(h)]
# print(matrix)

# или

# matrix = []
# for y in range(h):
#     new_row = []
#     for x in range(w):
#         new_row.append(0)
#     matrix.append(new_row)
#
# for row in matrix:
#     # print(row)
#     for x in row:
#         print(x, end="\t")
#     print()


# for x, y in [[1, 2], [3, 4], [5, 6], [7, 8]]:
#     print(x, "+", y, "=", x + y)


# w, h = 5, 3
# matrix = [[random.randint(1, 100) for x in range(w)]for y in range(h)]
# print(matrix)
# print()
# for row in matrix:
#     # print(row)
#     for x in row:
#         print(x, end="\t")
#     print()

# Задача
#
# import random
# w, h = 3, 4
# count = 0
# matrix = [[random.randint(-20, 20) for x in range(w)] for y in range(h)]
# for row in matrix:
#     # print(row)
#     for x in row:
#         print(x, end="\t\t")
#         if x < 0:
#             count += 1
#     print()
# print("Количество отрицательных элементов:", count)


# Modules

# import math
#
# print(math.sqrt(4))
# print(math.pi)
# print(math.ceil(3.2))
# print(math.floor(3.2))

# import math as m
#
# print(m.ceil(3.2))
# print(m.floor(3.2))

# from math import ceil, floor
#
# print(ceil(3.2))
# print(floor(3.2))


# from math import *
#
# print(ceil(3.2))
# print(floor(3.2))

# Задача

# from math import pi
#
# radius = int(input("Введите радиус окружности: "))
# print("Длина окружности: ", round(2 *pi * radius, 2))


# Задача

# from math import sqrt
# a = int(input("Введите первый катет: "))
# b = int(input("Введите второй катет: "))
# print(sqrt(a ** 2 + b ** 2))


# import time
# import locale
#
# locale.setlocale(locale.LC_ALL, "ru")
#
# seconds = time.time()
# print(seconds)
# print(time.ctime())
# res = time.localtime()
# print(res)
# print(res.tm_mday, ".0", res.tm_mon, ".", res.tm_year, sep="")
#
# print(time.strftime("Today is %B %d, %Y"))
# print(time.strftime("Сегодня: %B %d, %Y"))
# print(time.strftime("%B %d, %Y", time.localtime(712391864)))
# print(time.strftime("%d/%m/%Y, %H:%M:%S"))
#
# pause = 5
# print("Программа запущена")
# time.sleep(pause)
# print(pause, "секунд")

# start = time.monotonic()
# time.sleep(5)
# finish = time.monotonic()
# res = finish - start
# print(res)


# print()
#
#
# def hello(name):
#     print("Hello", name)
#
#
# hello("Irina")
# hello("Ivan")


# def get_sum(a, b):
#     print(a + b)
#
#
# get_sum(2, 5)


# def maximum(one, two):
#     if one > two:
#         return one
#     else:
#
#
#
#
# m = maximum(9, 6)
# print(m)


# Задача

# def cube(a):
#     return a * a * a
#
# for i in range(1, 11):
#     print(i, "в кубе =", cube(i))


# Задача

# Вариант 1

# def change(lst):
#     lst[0], lst[-1] = lst[-1], lst[0]
#     return lst
#
#
# print("Исходные данные:")
# print(change([1, 2, 3]))
# print(change([9, 12, 33, 54, 105]))
# print(change(["с", "л", "о", "н"]))

# Вариант 2

# def change(lst):
#     start = lst.pop()
#     end = lst.pop(0)
#     lst.append(end)
#     lst.insert(0, start)
#     return lst
#
# print("Исходные данные:")
# print(change([1, 2, 3]))
# print(change([9, 12, 33, 54, 105]))
# print(change(["с", "л", "о", "н"]))


# def func(x, y):
#     if x > y:
#         return True
#     else:
#         return False
#
# print(func(10, 5))
# print(func(5, 10))
# a = 5
# b = 10
# if func(a, b):
#     print("Первое число больше второго")
# else:
#     print("Второе число больше первого")


# Задача на ввод пароля
#
# def check_password(password):
#     has_upper = False
#     has_lower = False
#     has_num = False
#
#     for ch in password:
#         if "A" <= ch <= "Z":
#             has_upper = True
#         if "a" <= ch <= "z":
#             has_lower = True
#         if "0" <= ch <= "9":
#             has_num = True
#
#     if len(password) >= 8 and has_upper and has_lower:
#         return True
#     return False
#
#
# p = input("Введите пароль: ")
# if check_password(p):
#     print("Это надёжный пароль")
# else:
#     print("Это ненадёжный пароль")


# def get_sum(a, b, c=0, d=1):
#     return a + b + c + d
#
#
# print(get_sum(1, 5, 2, 7))
# print(get_sum(1, 5, 2)) # 9
# print(get_sum(1, 5))
# print(get_sum(1, 5, d=2)) # 8


# Задача

# def digit_sum(n, even=True):  # 9874023
#     s = 0
#     while n > 0:
#         cur_digit = n % 10
#         if even and cur_digit % 2 == 0:
#             s += cur_digit
#         if not even and cur_digit % 2 != 0:
#             s += cur_digit
#         n //= 10
#     return s
#
#
# print("Сумма чётных цифр:")
# print(digit_sum(9874023))
# print(digit_sum(38271))
# print(digit_sum(123456789))
#
# print("Сумма нечётных цифр:")
# print(digit_sum(9874023, even=False))
# print(digit_sum(38271, even=False))
# print(digit_sum(123456789, even=False))


# def display_info(name, age):
#     print("Name:", name, "\nAge:", age)
#
#
# display_info("Ira", 23)
# display_info(23, "Ira")
# display_info(age=23, name="Ira")


# a = "Hello"
# b = "Hello"
# print(a, id(a))
# print(b, id(b))
# print(a == b)   # True
# print(a is b)   # True
#
# lst1 = [1, 2, 3]
# lst2 = [1, 2, 3]
# print(lst1, id(lst1))
# print(lst2, id(lst2))
# print(lst1 == lst2)   # True
# print(lst1 is lst2)   # False


# Изменяемые объекты - list
# Незменяемые объекты - int, float, bool, str, tuple

# lst1 = [1, 2, 3]
# print(lst1, id(lst1))
# lst1.append(4)
# print(lst1, id(lst1))

# Кортежи (tuple)

# lst = [10, 20, 30]
# tpl = (10, 20, 30)
# print(lst.__sizeof__())
# print(tpl.__sizeof__())


# a = "red", "blue", "green"
# print(a)
# print(type(a))


# a = 1, 2, 3, 4, 5
# print(a)
# print(type(a))


# a = tuple("Hello")
# a = tuple([1, 5, 8, 9, 6])
# print(a)
# print(type(a))
# print(a[0])
# print(a[1:3])
# a[2] = 12
# print(a)

# ---------------------------------------------------------------------------------------------------
# Занятие 9

from random import randint

# s = [i for i in range(5)]
# s = tuple(i for i in range(5))
# s = tuple(input("-> ") for i in range(5))
# s = tuple(randint(20, 40) for i in range(5))
# print(s)

# Задача

# res = tuple(2 ** i for i in range(1, 13))
# print(res)


# t1 = tuple("hello")
# t2 = tuple("world")
# t3 = t1 + t2
# print(t3)
# print(t3 * 2)
# print(t3.count('l'))
# print(t3.count('a'))
# print(t3.index('l'))


# Задача

# def slicer(tpl, el):
#     if el in tpl:
#         if tpl.count(el) > 1:
#             first = tpl.index(el)  # 1
#             second = tpl.index(el, first + 1)  # 4
#             return tpl[first:second]
#         else:
#             a = tpl.index(el)
#             return tpl[tpl.index(el):]
#     else:
#         return tuple()
#
#
# print(slicer((1, 2, 3), 8))
# print(slicer((1, 8, 3, 4, 8, 8, 9, 2), 8))
# print(slicer((1, 2, 8, 5, 1, 2, 9), 8))


# Задача


# t = (10, 11, [1, 2, 3], [4, 5, 6], ['hello', 'world'])
# print(t.id(t))
# t[4][0] = 'new'
# t[4].append('hi')
# print(t, id(t))


# t = (1, 2, 3)
# # x = t[0]
# # y = t[1]
# # z = t[2]
# # распаковка кортежа
# x, y, z = t
# print(x, y, z)


# def get_user():
#     name = "Tom"
#     age = 22
#     is_married = False
#     return name, age, is_married
#
#
# user = get_user()
# print(user)
# print(user[0])
# print(user[1])
# print(user[2])


# def func(lst):
#     return sum(lst), len(lst)
#
#
# a, b = func([2, 9, 6, 5, 8, 7, 5, 8, 7, 1, 4, 5, 4])
# print("Сумма:", a)
# print("Количество:", b)
#
# for i in "red", "blue", "green":
#     print(i)


# lst = [1, 2, 3, 4, 5]
# print(lst)
# tpl = tuple(lst)
# print(tpl)
# lst1 = list(tpl)
# print(lst1)


# Задача

# countries = (
#     ("Германия", 80.2, (("Берлин", 3.326), ("Гамбург", 1.718))),
#     ("Франция", 66, (("Париж", 2.2), ("Марсель", 1.6))),
# )
# print(countries)
#
# for country in countries:
#     country_name, country_population, cities = country
#     print("\nСтрана: ", country_name, ", Население: ", country_population, sep="")
#     for city in cities:
#         city_name, city_population = city
#         print("\tГород: ", city_name, ", Население: ", city_population, sep="")


# Множество (set) - неупорядоченная коллекция, которая содержит только уникальные элементы

# s = {'banana', 'apple', 'orange'}
# print(s)
# print(type(s))
# for i in s:
#     print(i)


# s = ['banana', 'apple', 'orange', 'banana', 'apple']
# print(s)
# st = set(s)
# print(st)
# s1 = list(st)
# print(s1)


# a = []
# print(type(a))
#
# a = set()
# print(type(a))

# s = {i for i in range(5)}
# print(s)


# a = set("Hello")
# print(a)
# # print('o' in a)
# # print('a' in a)
# a.add("a")
# print(a)
# el = "e"
# if el in a:
#     a.remove(el)  # KeyError
# print(a)
# a.discard("o")
# print(a)
# a.pop()
# print(a)
# a.clear()
# print(a)


# ________________________________________________________________________________________________
# Занятие 10
# Надо зарегаться в GIT HUB

# git init - создание репозитория(один раз для одного репозитория)
# git status - просмотр состояния репозитория
# git add -A  - отслеживание изменений
#       -A,  --all - все файлы, которые находятся в папке и всех подпапках
#       main.py - один файл
#       . - все файлы из текущей директории
#
# git config --global user.name "new user"
#       --local
# git config --global user.email "test@mail.ru"
# git commit -m "first commit" - создание контрольной точки состояния репозитория
# .gitignore -























