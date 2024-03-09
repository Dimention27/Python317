
tpl = tuple(input("Введите по порядку, без пробелов, элементы кортежа: "))
print(tpl)
stl = []
for i in tpl:
    if i not in stl:
        stl.append(i)
for i in stl:
    print("Количество ", i, "=", tpl.count(i))
