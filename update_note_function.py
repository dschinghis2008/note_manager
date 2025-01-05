import datetime

def upd_issue_date(dt):
    end = '1'
    new_dt = ''
    while end != '2':
        try:
            new_dt = input('Введите дату истечения заметки в формате "dd.mm.yy": ')
            new_dt = datetime.datetime.strptime(new_dt, '%d.%m.%y')
        except ValueError:
            print('Неверный формат даты. Будет оставлено старое значение: ', dt)
            new_dt = dt

        end=input('Введите 1 чтобы продолжить обновление даты истечения\nВведите 2 чтобы завершить обновление: ')

    print('Новое значение даты истечения: ', new_dt)
    return new_dt

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
        return note, print('Update canceled')

    if field == 'issue_date':
        value = upd_issue_date(note['issue_date'])
    else:
        value = input('Введите новое значение для поля: ' + field + ': ')

    note[field] = value
    return note


note = {'username': 'user', 'title': 'grade1', 'content': 'step 3', 'status': 'none',
        'issue_date': datetime.datetime.strptime('10.01.25', '%d.%m.%y')}
print('Исходная заметка:\n', note)
print('После обновления:\n', update_note(note))
