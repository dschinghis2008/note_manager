import datetime


def get_now():
    return datetime.datetime.now()


def get_issue_date():
    dt_format = ''
    f = input('Выберите формат даты:\n1 "dd.mm.yy"\n2 "yyyy-mm-dd"')
    if f == '1':
        dt_format = '%d.%m.%y'
    elif f == '2':
        dt_format = '%Y-%m-%d'
    else:
        dt_format = '%d.%m.%Y'

    str_dt = input('Введите дату истечения заметки в формате "' + dt_format + '":')
    return datetime.datetime.strptime(str_dt, dt_format)


now = get_now()
issue_date = get_issue_date()
print('Сейчас: ', now.strftime('%d.%m.%y'))
print('Дата действия заметки: ', issue_date.strftime('%d.%m.%Y'))
check_deadline = now > issue_date
print('Дата действия заметки истекла? ', check_deadline)
if check_deadline:
    print('Дата заметки истекла ', now - issue_date, ' назад')
else:
    print('До истечения даты: ', issue_date - now)
