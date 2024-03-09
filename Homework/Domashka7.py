import math

print("Выбор фигуры: \n1 - треугольник \n2 - прямоугольник \n3 - круг")
choice = int(input(": "))


def triangle(a, b):
    return (a * b) / 2


def rectangle(e, d):
    return e * d


def circle(y):
    return math.pi * (y ** 2)


if choice == 1:
    z = int(input("Основание: "))
    q = int(input("Высота: "))
    S = triangle(z, q)
    print("Площадь:", S)

if choice == 2:
    r = int(input("Сторона 1: "))
    t = int(input("Сторона 2: "))
    w = rectangle(r, t)
    print("Площадь:", w)

if choice == 3:
    y = int(input("Радиус окружности: "))
    v = circle(y)
    print("Площадь:", v)

# def triangle(a, b):
#     z = int(input("Основание: "))
#     q = int(input("Высота: "))
#     S = triangle(z, q)
#     print("Площадь:", S)
#     return (a * b) / 2
#
#
# def rectangle(e, d):
#     r = int(input("Сторона 1: "))
#     t = int(input("Сторона 2: "))
#     w = rectangle(r, t)
#     print("Площадь:", w)
#     return e * d
#
#
# def circle(y):
#     y = int(input("Радиус окружности: "))
#     v = circle(y)
#     print("Площадь:", v)
#     return math.pi * (y ** 2)
