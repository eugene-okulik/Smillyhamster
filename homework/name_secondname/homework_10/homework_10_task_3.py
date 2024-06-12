# Задание №3
# Программа спрашивает у пользователя 2 числа (вне функции)
#
# Создайте декоратор, который декорирует функцию calc и управляет тем какая операция будет произведена:
#
# если числа равны, то функция calc вызывается с операцией сложения этих чисел
# если первое больше второго, то происходит вычитание второго из певрого
# если второе больше первого - деление первого на второе
# если одно из чисел отрицательное - умножение

num_1 = int(input('Введите число: '))
num_2 = int(input('И еще одно: '))


def operation(func):
    def wrapper(*args):
        a, b = args[0], args[1]
        if a < 0 or b < 0:
            func(a, b, '*')
        elif a == b:
            func(a, b, '+')
        elif a > b:
            func(a, b, '-')
        elif a < b:
            func(a, b, '/')

    return wrapper


@operation
def calc(first, second, operation):
    if operation == '+':
        print(first + second)
    elif operation == '-':
        print(first - second)
    elif operation == '/':
        print(first / second)
    elif operation == '*':
        print(first * second)


calc(num_1, num_2)
