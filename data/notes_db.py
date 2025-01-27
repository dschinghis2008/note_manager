import sqlite3

from data import notes, print_notes


def update_note(id, upd_dict, path_db):
    try:
        con = sqlite3.connect(path_db)
        cur = con.cursor()
        cur.execute('update notes set title=?, content=?, status=?, issue_date=? where id=?;',
                    (upd_dict['title'], upd_dict['content'], upd_dict['status'], upd_dict['issue_date'], id))
        con.commit()
    finally:
        con.close()


def delete_note(id, path_db):
    try:
        con = sqlite3.connect(path_db)
        cur = con.cursor()
        cur.execute('delete from notes where id=?;', (id,))
        con.commit()
    finally:
        con.close()


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


print('--==>> SAVE TO DB')
for n in notes:
    try:
        save_to_db(n)
    except sqlite3.IntegrityError as e:
        print(e)
        continue

print('--==>> LOAD FROM DB')
print_notes(load_from_db())

notes[0]['title'] = 'тест апдейта'
notes[0]['content'] = 'тест апдейта'
notes[0]['status'] = 'тест апдейта'
notes[0]['issue_date'] = '28.02.2025'
update_note(1, notes[0], 'db_note.db')
print('--==>> UPDATE DB')
print_notes(load_from_db())

print('--==>> DELETE FROM DB')
delete_note(3, 'db_note.db')
print_notes(load_from_db())
