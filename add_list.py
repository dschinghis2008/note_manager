import datetime

username = input("введите имя пользователя: ")
title = input("введите заголовок: ")
content = input("введите описание: ")
status = input("введите статус: ")
created_date = input('введите дату создания заметки в формате "dd.mm.yy": ')
created_date = datetime.datetime.strptime(created_date, '%d.%m.%y')
issue_date = input('введите дату истечения заметки в формате "dd.mm.yy": ')
issue_date = datetime.datetime.strptime(issue_date, '%d.%m.%y')

title1 = input("введите первый заголовок: ")
title2 = input("введите второй заголовок: ")
title3 = input("введите третий заголовок: ")
list_of_titles = [title1, title2, title3]

print('Имя пользователя: ', username)
print('Заголовок: ', title)
print('Описание: ', content)
print('Статус: ', status)
print('Дата создания: ', created_date)
print('Дата истечения: ', issue_date)
print('список заголовков: ', list_of_titles)
