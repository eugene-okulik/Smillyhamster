# Задача 1
#  Дана такая дата: "Jan 15, 2023 - 12:05:33"
#  Преобразуйте эту дату в питоновский формат, после этого:
#  1. Распечатайте полное название месяца из этой даты
#  2. Распечатайте дату в таком формате: "15.01.2023, 12:05"

import datetime

task_time = "Jan 15, 2023 - 12:05:33"

new_task_time = datetime.datetime.strptime(task_time, "%b %d, %Y - %H:%M:%S")

month = datetime.datetime.strftime(new_task_time, "%B")
print(f"Полное название месяца {month}")

formated_data = datetime.datetime.strftime(new_task_time, "%d.%m.%Y, %H:%M")
print(f"Отформатированная дата {formated_data}")
