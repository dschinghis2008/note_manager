username = input("введите имя пользователя: ")
content = input("введите описание: ")
status = input("введите статус: ")
created_date = input('введите дату создания заметки в формате "dd.mm": ')
issue_date = input('введите дату истечения заметки в формате "dd.mm": ')

title1 = input("введите первый заголовок: ")
title2 = input("введите второй заголовок: ")
title3 = input("введите третий заголовок: ")
list_of_titles = [title1, title2, title3]

note = {'Имя пользователя': username, 'Описание': content, 'Статус': status,
        'Дата создания': created_date, 'Дата истечения': issue_date,
        'Список заголовков': list_of_titles}
print("Поля заметки в виде словаря: ", note)
