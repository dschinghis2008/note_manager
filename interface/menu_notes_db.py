from data import notes, print_notes
from data.notes_db import save_to_db, load_from_db, search_notes_by_keyword, update_note, delete_note, \
    filter_notes_by_status

# print('--==>> SAVE TO DB')
# for n in notes:
#      save_to_db(n, 'data\\db_note.db')

print('--==>> DELETE FROM DB')
#delete_note(3, '..\\data\\db_note.db')


# print('--==>> LOAD FROM DB')
#print_notes(load_from_db('..\\data\\db_note.db'))

# notes[0]['title'] = 'тест апдейта'
# notes[0]['content'] = 'тест апдейта'
# notes[0]['status'] = 'тест апдейта'
# notes[0]['issue_date'] = '28.02.2025'
# update_note(10, notes[0], '..\\data\\db_note.db')
# print('--==>> UPDATE DB')
# print_notes(load_from_db('..\\data\\db_note.db'))

#print_notes(search_notes_by_keyword('4', '..\\data\\db_note.db'))
print_notes(filter_notes_by_status('none', '../data/db_note.db'))
