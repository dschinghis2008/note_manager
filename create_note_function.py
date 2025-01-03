import datetime


def create_note(id_):
    user = input('Имя пользователя:')
    title_ = input('Заголовок:')
    content = input('Описание:')
    status = input('Статус:')
    if user == '' or title_ == '' or content == '' or status == '':
        return print('Не должно быть пустых полей!')
    created_date = datetime.datetime.now()  # даты по умолчанию - now и now + неделя
    issue_date = created_date + datetime.timedelta(days=7)
    note = {'id': id_, 'user': user, 'title': title_, 'content': content, 'status': status,
            'created_date': created_date, 'issue_date': issue_date}
    return note


note = create_note(1)
print(note)
