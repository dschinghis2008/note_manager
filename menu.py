import datetime

from create_note_function import create_note
from delete_note import delete_note
from display_notes_function import display_notes
from search_notes_function import search_notes
from update_note_function import update_note


def menu():
    now = datetime.datetime.now()
    note1 = {'id': '1', 'username': 'user1', 'title': 'grade1', 'content': 'step 3', 'status': 'none',
             'created_date': now, 'issue_date': datetime.datetime.strptime('10.01.25', '%d.%m.%y')}

    note2 = {'id': '2', 'username': 'user2', 'title': 'scope of var', 'content': 'step 4', 'status': 'inproc',
             'created_date': now, 'issue_date': datetime.datetime.strptime('22.01.25', '%d.%m.%y')}

    note3 = {'id': '3', 'username': 'user3', 'title': 'search notes', 'content': 'step 5', 'status': 'close',
             'created_date': now, 'issue_date': datetime.datetime.strptime('12.01.25', '%d.%m.%y')}
    notes = [note1, note2, note3]
    id_note = 1
    cmd = ''

    while cmd != '6':
        cmd = input('Менеджер заметок\nВыберите:\n1 - для добавления новой заметки\n2 - для просмотра списка заметок' +
                    '\n3 - для редактирования заметки\n4 - для удаления заметки\n5 - для поиска заметки\n6 - для выхода\n')
        if cmd == '1':
            notes.append(create_note(id_note))
            id_note += 1

        elif cmd == '2':
            display_notes(notes)

        elif cmd == '3':
            id_range = len(notes)
            if id_range == 0:
                print('Нет сохраненных заметок')
                continue
            else:
                print('Доступны №№ заметок:\n')
                for n in notes:
                    print(n['id'])
                id_ = input('Введите № заметки для редактирования: ')
                flag_updated = False
                for n in notes:
                    if n['id'] == id_:
                        n = update_note(n)
                        flag_updated = True
                if not flag_updated:
                    print('Такого номера нет, возврат в основное меню')


        elif cmd == '4':
            del_type = input('Выберите:\n1 - для удаления по имени пользователя\n2 - для удаления по заголовку\n3 - для ' +
                             'возврата в основное меню: ')
            if del_type == '1':
                del_str = input('Задайте имя пользователя: ')
                delete_note(del_type, del_str, notes)
            elif del_type == '2':
                del_str = input('Задайте заголовок: ')
                notes = delete_note(del_type, del_str, notes)
            else:
                continue

        elif cmd == '5':
            title = input('Введите заголовок заметки частично или полностью (Enter чтобы не искать по заголовку):')
            status = input('Введите статус заметки (Enter чтобы не искать по статусу):')
            if title == '':
                title = None
            if status == '':
                status = None
            print('Найдено:')
            search_notes(notes, title, status)

        elif cmd == '6':
            print('Работа приложения завершена')

        else:
            print('Такого пункта меню пока нет')

if __name__ == '__main__':
    menu()