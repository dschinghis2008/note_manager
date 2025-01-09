import datetime


def sort_by_dt_issue(list_notes):  # сортировка перестановкой
    index = 0
    flag_sort = False
    index_min = 0

    note = {}

    while index < len(list_notes):
        min_dt = datetime.datetime.strptime('01.01.2100', '%d.%m.%Y')
        for i in range(index, len(list_notes)):
            if list_notes[i]['issue_date'] < min_dt:
                min_dt = list_notes[i]['issue_date']
                index_min = i
                flag_sort = True
                note = list_notes[i]

        if flag_sort:
            list_notes[index_min] = list_notes[index]
            list_notes[index] = note
        # print(index, notes, min)
        index += 1
        flag_sort = False

    return list_notes


def display_notes(notes):
    if len(notes) == 0:
        return print('У вас нет сохраненных заметок')
    else:
        sort = input('Введите "y" если необходимо отсортировать по дате дедлайна: ')
        if sort == 'y':
            notes = sort_by_dt_issue(notes)
        for n in notes:
            print('=====================================================')
            print('Заметка №: ', n['id'])
            print('Пользователь: ', n['user'])
            print('Заголовок: ', n['title'])
            print('Описание: ', n['content'])
            print('Статус: ', n['status'])
            print('Дата создания: ', n['created_date'])
            print('Дата истечения: ', n['issue_date'])
            print('=====================================================')


if __name__ == '__main__':
    now = datetime.datetime.now()
    note1 = {'id': '1', 'user': 'user1', 'title': 'grade1', 'content': 'step 3', 'status': 'none',
             'created_date': now, 'issue_date': datetime.datetime.strptime('10.01.25', '%d.%m.%y')}

    note2 = {'id': '2', 'user': 'user2', 'title': 'grade1', 'content': 'step 4', 'status': 'inproc',
             'created_date': now, 'issue_date': datetime.datetime.strptime('22.01.25', '%d.%m.%y')}

    note3 = {'id': '3', 'user': 'user3', 'title': 'grade', 'content': 'step 5', 'status': 'close',
             'created_date': now, 'issue_date': datetime.datetime.strptime('12.01.25', '%d.%m.%y')}

    notes = []
    display_notes(notes)  # проверка на сообщение о пустом списке
    notes = [note1, note2, note3]
    display_notes(notes)
