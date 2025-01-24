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
