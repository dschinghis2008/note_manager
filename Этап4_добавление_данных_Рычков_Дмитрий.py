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


now = datetime.date.today()

try:
    with open('notes.txt', 'a', encoding='utf-8') as file:
        notes = [
            {'id': '100', 'username': 'user100', 'title': 'append mode', 'content': 'append test', 'status': 'none',
             'created_date': now,
             'issue_date': datetime.datetime.strptime('20.01.25', '%d.%m.%y').date()}
        ]
        save_notes_to_file(notes, file)
except FileExistsError:
    print(f'{file} не найден, будет создан пустой файл')
    save_notes_to_file(notes, file)
finally:
    if not file.closed:
        file.close()
