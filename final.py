username = input("введите имя пользователя: ")
content = input("введите описание: ")
status = input("введите статус: ")
created_date = input('введите дату создания заметки в формате "dd.mm.yyyy": ')
issue_date = input('введите дату истечения заметки в формате "dd.mm.yyyy": ')

title1 = input("введите первый заголовок: ")
title2 = input("введите второй заголовок: ")
title3 = input("введите третий заголовок: ")
list_of_titles = [title1, title2, title3]

note = [username, content, status, created_date, issue_date, list_of_titles]
print("Поля заметки в виде списка: ", note)
