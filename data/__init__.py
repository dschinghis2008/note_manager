from .load_notes_from_file_function import load_notes_from_file as load
from .save_notes_to_file_function import save_notes_to_file as save
import datetime

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