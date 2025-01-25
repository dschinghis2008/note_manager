from data import notes

def save_to_db(note):
    import sqlite3
    con = sqlite3.connect('db_note.db')
    cur=con.cursor()
    cur.execute("""insert into notes values(?,?,?,?,?,?,?);""",
                (note['id'],note['username'], note['title'], note['content'], note['status'],
                 note['created_date'], note['issue_date']))
    con.commit()
    con.close()


