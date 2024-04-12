# Задание №1
# Напишите программу, которая добавляет ‘ing’ к словам (к каждому слову) в тексте

string = ('Etiam tincidunt neque erat, quis molestie enim imperdiet vel. '
        'Integer urna nisl, facilisis vitae semper at, dignissim vitae libero')

# Делим строку на список подстрок, разделитель - пробел
split_string = string.split()


new_string = []
print(type(new_string))

# Проверяем подстроки на наличие точки и запятой, в зависимости от этого
# определяем место для вставки
for word in split_string:
    if word[-1] in ',.':
        word = word[:-1] + 'ing' + word[-1]
    else:
        word += 'ing'
    new_string.append(word)

# Объединяем элементы списка в строку, разделитель - пробел
new_string = ' '.join(new_string)
print(new_string)
