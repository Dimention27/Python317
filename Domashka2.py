k = int(input("Введите число от 1 до 99: "))
if 1 <= k <= 99:
    print(k, end=" ")
    if k == 2 or k == 3 or k == 4 or k == 22 or k == 23 or k == 24 or k == 32 or k == 33 or k == 34 or k == 42 or \
        k == 43 or k == 44 or k == 52 or k == 53 or k == 54 or k == 62 or k == 63 or k == 64 or k == 72 or k == 73 or \
        k == 74 or k == 82 or k == 83 or k == 84 or k == 92 or k == 93 or k == 94:
        print("копейки")
    elif k == 1 or k == 21 or k == 31 or k == 41 or k == 51 or k == 61 or k == 71 or k == 81 or k == 91:
        print("копейка")
    else:
        print("копеек")
else:
    print(k)