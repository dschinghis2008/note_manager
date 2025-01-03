import datetime

notes = []
id_note = 1
cmd = ''


def search_doubles():
    result = ''
    titles = []
    for note in notes:
        titles.append(note['title'])  # коллекция заголовков

    set_titles = set(titles)  # коллекция заголовков без дублей
    if len(set_titles) == len(notes):
        result = 'Дубли не найдены'
    else:
        for t in set_titles:
            if titles.count(t) > 1:
                result = result + t + '; '
        result = 'Повторяющиеся заголовки: ' + result
    return result


def add_note(id_):
    user = input('Имя пользователя:')
    title_ = input('Заголовок:')
    content = input('Описание:')
    status = input('Статус:')
    created_date = input('Дата создания в формате "dd.mm.yy":')
    issue_date = input('Дата истечения в формате "dd.mm.yy":')
    if user == '' or title_ == '' or content == '' or status == '' or created_date == '' or issue_date == '':
        return print('Не должно быть пустых полей!')

    try:
        created_date = datetime.datetime.strptime(created_date, '%d.%m.%y')
        issue_date = datetime.datetime.strptime(issue_date, '%d.%m.%y')
    except ValueError:
        print('Ошибка в формате даты')

    note = {'id': id_, 'user': user, 'title': title_, 'content': content, 'status': status,
            'created_date': created_date, 'issue_date': issue_date}
    return note


while cmd != '4':
    cmd = input('Выберите:\n1 - для добавления новой заметки\n2 - для просмотра списка заметок' +
                '\n3 - для поиска дублей заголовков\n4 - для завершения работы\n')
    if cmd == '1':
        notes.append(add_note(id_note))
        id_note += 1
    elif cmd == '2':
        for n in notes:
            print('№: ', n['id'])
            print('Пользователь: ', n['user'])
            print('Заголовок: ', n['title'])
            print('Описание: ', n['content'])
            print('Статус: ', n['status'])
            print('Дата создания: ', n['created_date'])
            print('Дата истечения: ', n['issue_date'])
    elif cmd == '3':
        print(search_doubles())
