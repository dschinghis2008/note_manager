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


def display_notes(notes):
    if len(notes) == 0:
        return print('У вас нет сохраненных заметок')
    else:
        sort = input('Введите "y" если необходимо отсортировать по дате дедлайна: ')
        if sort == 'y':
            notes = sort_by_dt_issue(notes)
        for n in notes:
            print_dict(n)


def sort_by_dt_issue(list_notes):  # сортировка перестановкой
    index = 0
    flag_sort = False
    index_min = 0

    note = {}

    while index < len(list_notes):
        min_dt = datetime.datetime.strptime('01.01.2100', '%d.%m.%Y')
        for i in range(index, len(list_notes)):
            if list_notes[i]['issue_date'] < min_dt:
                min_dt = list_notes[i]['issue_date']
                index_min = i
                flag_sort = True
                note = list_notes[i]

        if flag_sort:
            list_notes[index_min] = list_notes[index]
            list_notes[index] = note
        index += 1
        flag_sort = False

    return list_notes


def upd_issue_date(dt):
    end = '1'
    new_dt = ''
    while end != 'stop':
        try:
            new_dt = input('Введите дату истечения заметки в формате "dd.mm.yy": ')
            new_dt = datetime.datetime.strptime(new_dt, '%d.%m.%y')
        except ValueError:
            print('Неверный формат даты. Будет оставлено старое значение: ', dt)
            new_dt = dt

        end = input('Введите "stop" чтобы завершить обновление даты или др. чтобы продолжить: ')

    print('Новое значение даты истечения: ', new_dt)
    return new_dt


def update_note(note):
    value = ''
    check_field = False
    print('Доступны для обновления следующие поля с их содержимым:')

    for e in note.keys():
        if e == 'id':  # id как PK не меняется, название поля лучше скрыть
            print('заметка №', ': ', note[e], '\n********************')
        else:
            print(e, ': ', note[e])

    while not check_field:
        field = input('Введите имя поля или "stop" для выхода: ')
        if field == 'stop':
            break
        for e in note.keys():
            if e == field and e != 'id':
                check_field = True
                break
        if not check_field:
            print('Такого поля нет')

    if not check_field:
        return note, print('Update canceled')

    if field == 'issue_date':
        value = upd_issue_date(note['issue_date'])
    else:
        value = input('Введите новое значение для поля ' + field + ': ')

    note[field] = value
    return note


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
    if len(set_for_remove) > 0:
        for s in set_for_remove:
            notes.pop(s)
    return print('Удалено ', len(set_for_remove), ' позиций'), notes


def print_dict(n):
    print('=====================================================')
    print('Заметка №: ', n['id'])
    print('Пользователь: ', n['user'])
    print('Заголовок: ', n['title'])
    print('Описание: ', n['content'])
    print('Статус: ', n['status'])
    print('Дата создания: ', n['created_date'])
    print('Дата истечения: ', n['issue_date'])
    print('=====================================================')


def search_notes(notes, keyword=None, status=None):
    if len(notes) == 0:
        return print('Нет сохраненных заметок')

    if keyword is None and status is None:
        for n in notes:
            print_dict(n)
    elif status is None:
        for n in notes:
            if keyword in n['title']:
                print_dict(n)
    elif keyword is None:
        for n in notes:
            if status == n['status']:
                print_dict(n)
    else:
        for n in notes:
            if keyword in n['title'] and status == n['status']:
                print_dict(n)


now = datetime.datetime.now()
note1 = {'id': '1', 'user': 'user1', 'title': 'grade1', 'content': 'step 3', 'status': 'none',
         'created_date': now, 'issue_date': datetime.datetime.strptime('10.01.25', '%d.%m.%y')}

note2 = {'id': '2', 'user': 'user2', 'title': 'scope of var', 'content': 'step 4', 'status': 'inproc',
         'created_date': now, 'issue_date': datetime.datetime.strptime('22.01.25', '%d.%m.%y')}

note3 = {'id': '3', 'user': 'user3', 'title': 'search notes', 'content': 'step 5', 'status': 'close',
         'created_date': now, 'issue_date': datetime.datetime.strptime('12.01.25', '%d.%m.%y')}
notes = [note1, note2, note3]
id_note = 1
cmd = ''

while cmd != '6':
    cmd = input('Менеджер заметок\nВыберите:\n1 - для добавления новой заметки\n2 - для просмотра списка заметок' +
                '\n3 - для редактирования заметки\n4 - для удаления заметки\n5 - для поиска заметки\n6 - для выхода\n')
    if cmd == '1':
        notes.append(create_note(id_note))
        id_note += 1

    elif cmd == '2':
        display_notes(notes)
        print(notes)

    elif cmd == '3':
        id_range = len(notes)
        if id_range == 0:
            print('Нет сохраненных заметок')
            continue
        else:
            print('Доступны №№ заметок:\n')
            for n in notes:
                print(n['id'])
            id_ = input('Введите № заметки для редактирования: ')
            flag_updated = False
            for n in notes:
                if n['id'] == id_:
                    n = update_note(n)
                    flag_updated = True
            if not flag_updated:
                print('Такого номера нет, возврат в основное меню')


    elif cmd == '4':
        del_type = input('Выберите:\n1 - для удаления по имени пользователя\n2 - для удаления по заголовку\n3 - для ' +
                         'возврата в основное меню: ')
        if del_type == '1':
            del_str = input('Задайте имя пользователя: ')
            delete_note(del_type, del_str, notes)
        elif del_type == '2':
            del_str = input('Задайте заголовок: ')
            notes = delete_note(del_type, del_str, notes)
        else:
            continue

    elif cmd == '5':
        title = input('Введите заголовок заметки частично или полностью (Enter чтобы не искать по заголовку):')
        status = input('Введите статус заметки (Enter чтобы не искать по статусу):')
        if title == '':
            title = None
        if status == '':
            status = None
        print('Найдено:')
        search_notes(notes, title, status)

    elif cmd == '6':
        print('Работа приложения завершена')

    else:
        print('Такого пункта меню пока нет')
