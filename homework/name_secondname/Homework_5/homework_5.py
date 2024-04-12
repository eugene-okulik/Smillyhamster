# Задание 1
# С помощью распаковки создайте из этого списка переменные, содержащие соответствующие данные
person = ['John', 'Doe', 'New York', '+1372829383739', 'US']
name, last_name, city, phone, country = person
print(f"name = {name} \nlast_name = {last_name} \ncity = {city} \nphone = {phone} \ncountry = {country}")

# Отделяем варианты решения друг от друга
print("-" * 35, "\n")

# Задание 2
# С помощью срезов и метода index получите из каждой строки с результатом число, прибавьте к полученному числу 10, результат сложения распечатайте.
out1 = 'результат операции: 42'
out2 = 'результат операции: 514'
out3 = 'результат работы программы: 9'

out1_pos = out1.index(':') + 1
out2_pos = out2.index(':') + 1
out3_pos = out3.index(':') + 1

out1_num = int(out1[out1_pos:].strip())
out2_num = int(out2[out2_pos:].strip())
out3_num = int(out3[out3_pos:].strip())

print(out1_num + 10)
print(out2_num + 10)
print(out3_num + 10)

# Отделяем варианты решения друг от друга
print("-" * 35, "\n")


# Задание 3
# Распечатайте текст, который будет использовать данные из этих списков
students = ['Ivanov', 'Petrov', 'Sidorov']
subjects = ['math', 'biology', 'geography']
students_list = ', '.join(students)
subjects_list = ', '.join(subjects)

print(f"Students {students_list} study these subjects: {subjects_list}")

# Финальный сепаратор
print("=" * 35, "\n")
