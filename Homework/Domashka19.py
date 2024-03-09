import re

pattern = 'my-p@ssw0rd'
password = input("Введите пароль: ")
result = re.findall(pattern, password)


def password_check(password):
    SpecialSym = ['-', '@', '_']
    if len(password) < 6:
        print('Пароль должна быть от 6 символов')

    elif len(password) > 18:
        print('Пароль слишком длинный')

    elif not any(char.isdigit() for char in password):
        print('Пароль должен содержать хотя бы 1 цифру')

    elif not any(char.islower() for char in password):
        print('Пароль должен содержать хотя бы 1 строчную букву')

    elif not any(char in SpecialSym for char in password):
        print('Пароль должен содержать специальные символы -@_')


def main():
    if result:
        print("Пароль соответствует")
    elif password_check(password):
        print("Пароль соответствует")
    else:
        print("Пароль не соответствует")


main()
