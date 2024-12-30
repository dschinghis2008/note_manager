import datetime

username = 'd2024'
title = 'note manager'
content = 'python project'
status = 'processed'
created_date = datetime.datetime.strptime('22.12.2024','%d.%m.%Y')
issue_date = datetime.datetime.strptime('31.12.2024','%d.%m.%Y')

print('Имя пользователя: ', username)
print('Заголовок: ', title)
print('Описание: ', content)
print('Статус: ', status)
print('Дата создания: ', created_date)
print('Дата истечения: ', issue_date)
