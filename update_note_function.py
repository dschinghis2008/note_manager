import datetime

def upd_issue_date(dt):
    end = '1'
    new_dt = ''
    while end != 'end':
        try:
            new_dt = input('Введите дату истечения заметки в формате "dd.mm.yy": ')
            new_dt = datetime.datetime.strptime(new_dt, '%d.%m.%y')
        except ValueError:
            print('Неверный формат даты. Будет оставлено старое значение: ', dt)
            new_dt = dt

        end=input('Введите "end" чтобы завершить обновление или др. чтобы продолжить: ')

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

if __name__ == '__main__':
    note = {'username': 'user', 'title': 'grade1', 'content': 'step 3', 'status': 'none',
            'issue_date': datetime.datetime.strptime('10.01.25', '%d.%m.%y')}
    print('Исходная заметка:\n', note)
    print('После обновления:\n', update_note(note))
