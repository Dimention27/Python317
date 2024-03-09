students = {}
n = int(input("Количество студентов: "))
s = 0
for key in range(n):
    name = input(str(key + 1) + "-й студент: ")
    point = int(input("Балл: "))
    students[name] = point
    s += point

average = s / n
print("Средний балл: ", average, ". Студенты с баллом выше среднего: ")

for key in students:
    if students[key] > average:
        print(key)