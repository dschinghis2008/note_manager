from .load_notes_from_file_function import load_notes_from_file as load_notes
from .save_notes_to_file_function import save_notes_to_file as save_notes
from .append_notes_to_file import save_notes_to_file as append_notes
from .save_notes_json import save_notes_json as save_json
import datetime

def print_notes(notes):
    for n in notes:
        print('=====================================================')
        print('Заметка №: ', n['id'])
        print('Пользователь: ', n['username'])
        print('Заголовок: ', n['title'])
        print('Описание: ', n['content'])
        print('Статус: ', n['status'])
        print('Дата создания: ', n['created_date'])
        print('Дата истечения: ', n['issue_date'])
        print('=====================================================')

now = datetime.datetime.now().date()
notes = [
    {'id': '1', 'username': 'user1', 'title': 'grade1', 'content': 'step 3', 'status': 'none',
     'created_date': now,
     'issue_date': datetime.datetime.strptime('10.01.25', '%d.%m.%y').date()},
    {'id': '2', 'username': 'user2', 'title': 'grade1', 'content': 'step 4', 'status': 'inproc',
     'created_date': now,
     'issue_date': datetime.datetime.strptime('22.01.25', '%d.%m.%y').date()},
    {'id': '3', 'username': 'user3', 'title': 'grade', 'content': 'step 5', 'status': 'close',
     'created_date': now,
     'issue_date': datetime.datetime.strptime('12.01.25', '%d.%m.%y').date()}
]