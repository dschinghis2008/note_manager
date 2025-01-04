import datetime


def update_note(note):
    value = ''
    check_field = False
    print('Доступны для обновления следующие поля с их содержимым:')

    for e in note.keys():
        print(e, ': ', note[e])

    while not check_field:
        field = input('Введите имя поля или "stop" для выхода: ')
        if field == 'stop':
            break
        for e in note.keys():
            if e == field:
                check_field = True
                break
        if not check_field:
            print('Такого поля нет')

    if not check_field:
        return print('Update canceled')

    if field == 'issue_date':
        try:
            value = input('Введите дату истечения заметки в формате "dd.mm.yy": ')
            value = datetime.datetime.strptime(value, '%d.%m.%y')
        except ValueError:
            print('Неверный формат даты. Будет присвоено текущее значение')
            value = datetime.datetime.now()
    else:
        value = input('Введите новое значение для поля: ' + field + ': ')

    note[field] = value
    return note


note = {'username': 'user', 'title': 'grade1', 'content': 'step 3', 'status': 'none',
        'issue_date': datetime.datetime.strptime('10.01.25', '%d.%m.%y')}
print('Исходная заметка:\n', note)
print('После обновления:\n', update_note(note))
