import sqlite3

from data import notes


def save_to_db(note):
    try:
        con = sqlite3.connect('db_note.db')
        cur = con.cursor()
        cur.execute("""insert into notes values(?,?,?,?,?,?,?);""",
                    (note['id'], note['username'], note['title'], note['content'], note['status'],
                     note['created_date'], note['issue_date']))
        con.commit()
    finally:
        con.close()


def load_from_db():
    try:
        con = sqlite3.connect('db_note.db')
        cur = con.cursor()
        cur.execute('select * from notes')
        rows = cur.fetchall()
        notes = []
        for row in rows:
            notes.append(
                {'id': str(row[0]),
                 'username': row[1],
                 'title': row[2],
                 'content': row[3],
                 'status': row[4],
                 'created_date': row[5],
                 'issue_date': row[6]
                 }
            )
        return notes
    finally:
        con.close()


for n in notes:
    try:
        save_to_db(n)
    except sqlite3.IntegrityError as e:
        print(e)
        continue

for n in load_from_db():
    print('=====================================================')
    print('Заметка №: ', n['id'])
    print('Пользователь: ', n['username'])
    print('Заголовок: ', n['title'])
    print('Описание: ', n['content'])
    print('Статус: ', n['status'])
    print('Дата создания: ', n['created_date'])
    print('Дата истечения: ', n['issue_date'])
    print('=====================================================')
