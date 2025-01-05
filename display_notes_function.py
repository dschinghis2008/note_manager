import datetime


def display_notes(notes):
    if len(notes) == 0:
        return print('У вас нет сохраненных заметок')
    else:
        for n in notes:
            print('=====================================================')
            print('Заметка №: ', n['id'])
            print('Пользователь: ', n['user'])
            print('Заголовок: ', n['title'])
            print('Описание: ', n['content'])
            print('Статус: ', n['status'])
            print('Дата создания: ', n['created_date'])
            print('Дата истечения: ', n['issue_date'])
            print('=====================================================')


now = datetime.datetime.now()
note1 = {'id': '1', 'user': 'user1', 'title': 'grade1', 'content': 'step 3', 'status': 'none',
         'created_date': now, 'issue_date': datetime.datetime.strptime('10.01.25', '%d.%m.%y')}

note2 = {'id': '2', 'user': 'user2', 'title': 'grade1', 'content': 'step 4', 'status': 'inproc',
         'created_date': now, 'issue_date': datetime.datetime.strptime('11.01.25', '%d.%m.%y')}

note3 = {'id': '3', 'user': 'user3', 'title': 'grade', 'content': 'step 5', 'status': 'close',
         'created_date': now, 'issue_date': datetime.datetime.strptime('12.01.25', '%d.%m.%y')}

notes = []
display_notes(notes)
notes = [note1, note2, note3]
display_notes(notes)
