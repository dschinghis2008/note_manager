import datetime


def create_note(id_):
    user = input('Имя пользователя:')
    title_ = input('Заголовок:')
    content = input('Описание:')
    status = input('Статус:')
    if user == '' or title_ == '' or content == '' or status == '':
        return print('Не должно быть пустых полей!')
    created_date = datetime.datetime.now()
    issue_date = input('Дата истечения заметки в формате "dd.mm.yy" или Enter чтобы задать текущую дату + неделя:')
    if issue_date == '':
        issue_date = created_date + datetime.timedelta(days=7)
    else:
        try:
            issue_date = datetime.datetime.strptime(issue_date, '%d.%m.%y')
        except ValueError:
            print('Неверный формат даты истечения заметки')

    note = {'id': id_, 'user': user, 'title': title_, 'content': content, 'status': status,
            'created_date': created_date, 'issue_date': issue_date}
    return note

if __name__ == '__main__':
    note = create_note(1)
    print(note)
