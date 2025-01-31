import sqlite3

from data import print_notes


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


def save_to_db(note, db_path):
    try:
        con = sqlite3.connect(db_path)
        cur = con.cursor()
        cur.execute("""insert into notes values(?,?,?,?,?,?,?);""",
                    (note['id'], note['username'], note['title'], note['content'], note['status'],
                     note['created_date'], note['issue_date']))
        con.commit()
    except Exception as e:
        print(e)
    finally:
        con.close()


def load_from_db(db_path):
    try:
        con = sqlite3.connect(db_path)
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
    except Exception as e:
        print(e)
    finally:
        con.close()

def search_notes_by_keyword(keyword, db_path):
    con = sqlite3.connect(db_path)
    cur = con.cursor()
    cur.execute('select * from notes where title like ? or content like ?',
                (f'%{keyword}%', f'%{keyword}%'))
    rows = cur.fetchall()
    con.close()
    return [
        {'id': row[0], 'username': row[1], 'title': row[2], 'content': row[3], 'status': row[4], 'created_date': row[5],
         'issue_date': row[6]} for row in rows]

def filter_notes_by_status(status, db_path):
    try:
        con = sqlite3.connect(db_path)
        cur = con.cursor()
        cur.execute('select * from notes where status = ?',(status,))
        rows = cur.fetchall()
        return [
        {'id': row[0], 'username': row[1], 'title': row[2], 'content': row[3], 'status': row[4], 'created_date': row[5],
         'issue_date': row[6]} for row in rows]
    finally:
        con.close()

if __name__ == '__main__':
    delete_note(1,'db_note.db')


