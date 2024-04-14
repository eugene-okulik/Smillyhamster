# Задание №2
# Вывести каждый ключ словааря с новой строки, количество в значении

words = {'I': 3, 'love': 5, 'Python': 1, '!': 50}

for key, value in words.items():
    print(key * value)
