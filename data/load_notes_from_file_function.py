import datetime


def load_notes_from_file(file):
    source_list = file.readlines()
    notes = []
    # инициируем поля
    id = ''
    username = ''
    title = ''
    content = ''
    status = ''
    created_date = ''
    issue_date = ''

    for s in source_list:
        if 'Заметка №: ' in s:
            id = s.replace('Заметка №: ', '').rstrip('\n')
        if 'Пользователь: ' in s:
            username = s.replace('Пользователь: ', '').rstrip('\n')
        if 'Заголовок: ' in s:
            title = s.replace('Заголовок: ', '').rstrip('\n')
        if 'Описание: ' in s:
            content = s.replace('Описание: ', '').rstrip('\n')
        if 'Статус: ' in s:
            status = s.replace('Статус: ', '').rstrip('\n')
        if 'Дата создания: ' in s:
            created_date = s.replace('Дата создания: ', '').rstrip('\n')
            created_date = datetime.datetime.strptime(created_date, '%Y-%m-%d').date()
        if 'Дата истечения: ' in s:
            issue_date = s.replace('Дата истечения: ', '').rstrip('\n')
            issue_date = datetime.datetime.strptime(issue_date, '%Y-%m-%d').date()
        if s == '==========\n':
            note = {'id': id, 'username': username, 'title': title, 'content': content, 'status': status,
                    'created_date': created_date, 'issue_date': issue_date}
            notes.append(note)
    return notes


if __name__ == '__main__':

    file = None
    try:
        file = open('notes.txt', encoding='utf-8')
        notes = load_notes_from_file(file)
        print(notes)
    except FileNotFoundError:
        print('Файл не найден в текущей директории, будет создан новый')
        file = open('notes.txt', 'w')
        file.close()
    except UnicodeDecodeError:
        print('Файл поврежден или не является текстовым')
    except PermissionError:
        print('Отсутствуют права доступа к файлу')
