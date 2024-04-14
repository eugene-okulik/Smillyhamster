# Задание 1
# Напишите программу. Есть две переменные, salary и bonus.
# Salary - int, bonus - bool.
# Спросите у пользователя salary. А bonus пусть назначается рандомом.
# Если bonus - true, то к salary должен быть добавлен рандомный бонус.

import random

salary = int(input("Введите ЗП: "))

bonus = random.choice([True, False])

if bonus:
    bonus_size = random.randint(1, 50000)
    salary += bonus_size
    print(f"Вам положен бонус в размере {bonus_size}. Всего к выплате {salary}")
else:
    print("Соррян, в этот раз без бонусов...")
