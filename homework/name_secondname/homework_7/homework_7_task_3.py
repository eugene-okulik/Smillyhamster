# Задание №3
# С помощью функций из каждой строки с результатом число,
# прибавьте к полученному числу 10,  результат сложения распечатайте.

out1 = "результат операции: 42"
out2 = "результат операции: 514"
out3 = "результат работы программы: 9"
out4 = "результат: 2"

# поместил решение ДЗ №5 в функцию
def edit_string(some_string):
    out1_num = int(some_string[some_string.index(":") + 1 :].strip())
    print(out1_num + 10)


edit_string(out1)
edit_string(out2)
edit_string(out3)
edit_string(out4)
