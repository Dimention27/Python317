res = ['madam', 'fire', 'tomato', 'book', 'kiosk', 'mom']
palindrome = list(filter(lambda x: (x == "".join(reversed(x))), res))
print(res)
print(palindrome)