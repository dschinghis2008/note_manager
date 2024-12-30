import datetime

notes = []
id_note = 1
cmd = ''


def add_note(id_):
    user = input('Имя пользователя:')
    title = input('Заголовок:')
    content = input('Описание:')
    status = input('Статус:')
    created_date = input('Дата создания в формате "dd.mm.yy":')
    issue_date = input('Дата истечения в формате "dd.mm.yy":')
    try:
        created_date = datetime.datetime.strptime(created_date, '%d.%m.%y')
        issue_date = datetime.datetime.strptime(issue_date, '%d.%m.%y')
    except ValueError:
        print('Ошибка в формате даты')
    note = {'id': id_, 'user': user, 'title': title, 'content': content, 'status': status,
            'created_date': created_date, 'issue_date': issue_date}
    notes.append(note)


while cmd != '3':
    cmd = input('Выберите:\n1 - для добавления новой заметки\n2 - для просмотра списка заметок' +
                '\n3 - для завершения работы\n')
    if cmd == '1':
        add_note(id_note)
        id_note = id_note + 1
    elif cmd == '2':
        for n in notes:
            print('№: ',n['id'])
            print('Пользователь: ', n['user'])
            print('Заголовок: ', n['title'])
            print('Описание: ', n['content'])
            print('Статус: ', n['status'])
            print('Дата создания: ', n['created_date'])
            print('Дата истечения: ', n['issue_date'])
