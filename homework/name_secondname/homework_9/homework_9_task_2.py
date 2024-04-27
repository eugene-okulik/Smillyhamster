# Задача 2
# отфильтровать список и вывести его
#  вывести самую высокую температуру
#  вывести самую низкую температуру
#  вывести среднюю температуру

temperatures = [
    20, 15, 32, 34, 21, 19, 25, 27, 30, 32, 34, 30, 29, 25, 27,
    22, 22, 23, 25, 29, 29, 31, 33, 31, 30, 32, 30, 28, 24, 23
]
new_temperatures_filter = list(
    filter(lambda temperature: temperature > 28, temperatures)
)
print("Отфильтрованный список жарких дней", new_temperatures_filter)
print("Самая высокая температура в новом списке", max(new_temperatures_filter))
print("Самая низкая температура в новом списке", min(new_temperatures_filter))
print(
    "Средняя температура в новом списке",
    int(sum(new_temperatures_filter) / len(new_temperatures_filter)),
)
