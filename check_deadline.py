import datetime

now = datetime.datetime.now()
issue_date = datetime.datetime(2025, 1, 31)
print('Сейчас: ', now.strftime('%d.%m.%y'))
print('Дата действия заметки: ', issue_date.strftime('%d.%m.%y'))
print('Дата действия заметки истекла? ', now > issue_date)
