# Задание №1
# Создайте универсальный декоратор, который можно будет применить к
# любой функции. Декоратор должен делать следующее: он должен
# распечатывать слово "finished"после выполнения декорированной функции.

def finish_me(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        print("finished")
        return result

    return wrapper


@finish_me
def example(text):
    print(text)
    print()


example('print me')
