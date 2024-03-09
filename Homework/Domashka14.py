def outer(a, b, c):
    def inner(i, j):
        return i * j

    s = 2 * (inner(a, b) + inner(a, c) + inner(b, c))
    return s


print(outer(2, 4, 6))
print(outer(5, 8, 2))
print(outer(1, 6, 8))

