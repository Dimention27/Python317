
n = [int(input("-> ")) for i in range(int(input("Введите элементы списка: \n n = ")))]
k = int(input("Введите индекс: \n k = "))
c = int(input("Введите значение: \n c = "))
n.insert(k, c)
print(n)
