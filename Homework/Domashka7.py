import math

# Фигуры
x = 1
v = 2
n = 3

p = int(input("Выбор фигуры: \n1 - треугольник \n2 - прямоугольник \n3 - круг \n: "))
if p == 1:
    t = int(input("Введите сторону а = "))
    y = int(input("Введите сторону b = "))
    u = int(input("Введите сторону c = "))
    s = (t + y + u) / 2
    pl = (s * (s - t) * (s - y) * (s - u)) ** 0.5
    print("Площадь треугольника = ", round(pl, 2))
elif p == 2:
    z = int(input("Введите сторону а = "))
    q = int(input("Введите сторону b = "))
    S = z * q
    print("Площадь прямоугольника = ", S)
elif p == 3:
    radius = int(input("Введите радиус окружности = "))
    print("Площадь круга = ", math.pi * (radius ** 2))

