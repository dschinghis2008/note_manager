import datetime


def print_dict(n):
    print('=====================================================')
    print('Заметка №: ', n['id'])
    print('Пользователь: ', n['username'])
    print('Заголовок: ', n['title'])
    print('Описание: ', n['content'])
    print('Статус: ', n['status'])
    print('Дата создания: ', n['created_date'])
    print('Дата истечения: ', n['issue_date'])
    print('=====================================================')


def search_notes(notes, user=None, keyword=None, status=None):
    if not notes:
        return print('Нет сохраненных заметок')
    if user is not None or keyword is not None or status is not None:
        if user is None:
            user = '=='
        if keyword is None:
            keyword = '=='
        if status is None:
            status = '=='
        for n in notes:
            if user == n['username'] or keyword in n['title'] or status == n['status']:
                print_dict(n)
    else:
        for n in notes:
            print_dict(n)


def search_notes_old(notes, keyword=None, status=None):
    if not notes:
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


if __name__ == '__main__':
    now = datetime.datetime.now().date()

    notes = []
    print('Тестирование функции поиска заметок\n1 - пустой список')
    search_notes(notes)
    notes = [
        {'id': '1', 'username': 'user1', 'title': 'grade1', 'content': 'step 3', 'status': 'none',
         'created_date': now, 'issue_date': datetime.datetime.strptime('10.01.25', '%d.%m.%y')},
        {'id': '2', 'username': 'user2', 'title': 'scope of var', 'content': 'step 4', 'status': 'inproc',
         'created_date': now, 'issue_date': datetime.datetime.strptime('22.01.25', '%d.%m.%y')},
        {'id': '3', 'username': 'user3', 'title': 'search notes', 'content': 'step 5', 'status': 'close',
         'created_date': now, 'issue_date': datetime.datetime.strptime('12.01.25', '%d.%m.%y')}
    ]

    print('2 - список из 3-х заметок с пустыми строками заголовка и статуса')
    search_notes(notes)
    print('3 - список из 3-х заметок с пустой строкой статуса. Ожидается нахождение заметки №2')
    search_notes(notes, 'user2', 'var')
    print('4 - список из 3-х заметок с пустой строкой заголовка. Ожидается нахождение заметки №1')
    search_notes(notes, status='none')
    print('5 - список из 3-х заметок со всеми параметрами поиска. Ожидается нахождение заметки №3')
    search_notes(notes, 'user3', 'note', 'close')
    print('6 - список из 3-х заметок со всеми параметрами поиска из разных заметок. Ожидается нахождение всех заметок')
    search_notes(notes, 'user1', 'of', 'close')
