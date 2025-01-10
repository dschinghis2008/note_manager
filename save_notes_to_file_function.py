import datetime


def save_notes_to_file(notes, file):
    for n in notes:
        file.writelines(f"Заметка №: {n['id']}\n")
        file.writelines(f"Пользователь:  {n['username']}\n")
        file.writelines(f"Заголовок: {n['title']}\n")
        file.writelines(f"Описание:  {n['content']}\n")
        file.writelines(f"Статус:  {n['username']}\n")
        file.writelines(f"Дата создания: {n['created_date']}\n")
        file.writelines(f"Дата истечения:  {n['issue_date']}\n==========\n")



now = datetime.datetime.now()
note1 = {'id': '1', 'username': 'user1', 'title': 'grade1', 'content': 'step 3', 'status': 'none',
         'created_date': now, 'issue_date': datetime.datetime.strptime('10.01.25', '%d.%m.%y')}

note2 = {'id': '2', 'username': 'user2', 'title': 'grade1', 'content': 'step 4', 'status': 'inproc',
         'created_date': now, 'issue_date': datetime.datetime.strptime('22.01.25', '%d.%m.%y')}

note3 = {'id': '3', 'username': 'user3', 'title': 'grade', 'content': 'step 5', 'status': 'close',
         'created_date': now, 'issue_date': datetime.datetime.strptime('12.01.25', '%d.%m.%y')}

notes = [note1, note2, note3]
file = open('notes.txt', 'w', encoding='utf-8')
try:
    save_notes_to_file(notes, file)
finally:
    file.close()
