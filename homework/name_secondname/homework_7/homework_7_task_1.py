# Задание №1 - "Угадайка"
# Немного усложнил - добавил рандом и подсказки

import random

# Получаем рандомное число
digit = random.randint(0, 100)
count = 0

# Во время отладки выводил заветное рандомное число
print(digit)

# Проверяем и в случае неудачи - немного подсказываем
while True:
    count += 1
    user_input = int(input(f"Попытка №{count}\nВведите число: "))
    if user_input == digit:
        print(f"Успешный успех на попытке №{count}! 🎉🎉🎉🎉🎉\n")
        break
    elif user_input > digit:
        print("Промазал! Загаданное число меньше... \n\nДавай еще попытку!")
        continue
    elif user_input < digit:
        print("Промазал! Загаданное число больше... \n\nДавай еще попытку!")

print("Приходите еще в наше казино! 😄")
