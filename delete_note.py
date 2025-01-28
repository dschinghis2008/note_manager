import datetime

notes = []
id_note = 1
cmd = ''


def delete_note(del_type, del_str, notes):
    set_for_remove = set()
    index_for_remove = 0
    for n in notes:
        if del_type == '1':
            if n['user'].upper() == del_str.upper():
                set_for_remove.add(index_for_remove)
        if del_type == '2':
            if n['title'].upper() == del_str.upper():
                set_for_remove.add(index_for_remove)
        index_for_remove = index_for_remove + 1
    if set_for_remove:
        for s in set_for_remove:
            notes.pop(s)
    return print('Удалено ', len(set_for_remove), ' позиций'), notes


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

    note = {'id': id_, 'username': user, 'title': title_, 'content': content, 'status': status,
            'created_date': created_date, 'issue_date': issue_date}
    notes.append(note)

if __name__ == '__main__':
    while cmd != '4':
        cmd = input('Выберите:\n1 - для добавления новой заметки\n2 - для просмотра списка заметок' +
                    '\n3 - для удаления заметки\n4 - для завершения работы\n')
        if cmd == '1':
            add_note(id_note)
            id_note = id_note + 1
        elif cmd == '2':
            for n in notes:
                print('№: ', n['id'])
                print('Пользователь: ', n['username'])
                print('Заголовок: ', n['title'])
                print('Описание: ', n['content'])
                print('Статус: ', n['status'])
                print('Дата создания: ', n['created_date'])
                print('Дата истечения: ', n['issue_date'])
        elif cmd == '3':
            del_type = input('Выберите:\n1 - для удаления по имени пользователя\n2 '
                             + '- для удаления по заголовку\n3 - для возврата в основное меню: ')
            if del_type == '1':
                del_str = input('Задайте имя пользователя: ')
                delete_note(del_type, del_str)
            elif del_type == '2':
                del_str = input('Задайте заголовок: ')
                delete_note(del_type, del_str)
