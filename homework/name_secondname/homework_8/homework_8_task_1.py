# Задание 2
# Напишите функцию-генератор, которая генерирует список чисел фибоначчи
# Распечатайте из этого списка пятое число, двухсотое число, тысячное число, стотысячное число


# Сама функция-генератор, теперь бесконечная
def fib(limit=100001):
    a, b = 0, 1
    count = 1
    while True:
        yield b
        a, b = b, a + b
        count += 1


for count, num in enumerate(fib(), start=1):
    if count in (5, 200, 1000, 100000):
        print(num)
    if count > 100000:
        break
