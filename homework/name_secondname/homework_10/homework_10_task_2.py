# Задание №2
# Создайте универсальный декоратор, который будет управлять тем,
# сколько раз запускается декорируемая функция


def repeat_me(some_func, count=4):
    def wrapper():
        for _ in range(count):
            print(some_func())

    return wrapper


@repeat_me
def example():
    text = "print me"
    return text


example()
