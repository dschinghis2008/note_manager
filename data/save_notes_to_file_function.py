import datetime


def save_notes_to_file(notes, file):
    for n in notes:
        file.write(f"Заметка №: {n['id']}\n")
        file.write(f"Пользователь: {n['username']}\n")
        file.write(f"Заголовок: {n['title']}\n")
        file.write(f"Описание: {n['content']}\n")
        file.write(f"Статус: {n['status']}\n")
        file.write(f"Дата создания: {n['created_date']}\n")
        file.write(f"Дата истечения: {n['issue_date']}\n==========\n")


if __name__ == '__main__':
    now = datetime.date.today()

    notes = [
        {'id': '1', 'username': 'user1', 'title': 'работа с файлами', 'content': 'step 3', 'status': 'none',
         'created_date': now, 'issue_date': datetime.datetime.strptime('10.01.25', '%d.%m.%y').date()},
        {'id': '2', 'username': 'user2', 'title': 'grade1', 'content': 'step 4', 'status': 'inproc',
         'created_date': now, 'issue_date': datetime.datetime.strptime('22.01.25', '%d.%m.%y').date()},
        {'id': '3', 'username': 'user3', 'title': 'grade', 'content': 'step 5', 'status': 'close',
         'created_date': now, 'issue_date': datetime.datetime.strptime('12.01.25', '%d.%m.%y').date()}
    ]

    try:
        with open('notes.txt', 'w', encoding='utf-8') as file:  # write mode
            save_notes_to_file(notes, file)
    except Exception as e:
        print(f'Error: {e}')
