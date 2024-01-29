from random import randint

tpl = tuple(randint(0, 9) for i in range(10))
print(tpl)
stl = []
for i in tpl:
    if i not in stl:
        stl.append(i)
for i in stl:
    print("Количество ", i, "=", tpl.count(i))


# get = tuple(input("Введите по порядку, без пробелов, элементы кортежа: "))
# print(get)
# get_lst = list(get)
# for i in get:
#     if i in get_lst:
#         print("Количество",i,"=",get_lst.count(i))
#         for j in range(get.count(i)):
#            get_lst.remove(i)
