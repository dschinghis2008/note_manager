import datetime

username = input("введите имя пользователя: ")
title = input("введите заголовок: ")
content = input("введите описание: ")
status = input("введите статус: ")
str_dt = input('введите дату создания заметки в формате "dd.mm.yy": ')
created_date = datetime.datetime.strptime(str_dt, '%d.%m.%y')
str_dt = input('введите дату истечения заметки в формате "dd.mm.yy": ')
issue_date = datetime.datetime.strptime(str_dt, '%d.%m.%y')

print('Имя пользователя: ', username)
print('Заголовок: ', title)
print('Описание: ', content)
print('Статус: ', status)
print('Дата создания: ', created_date)
print('Дата истечения: ', issue_date)
