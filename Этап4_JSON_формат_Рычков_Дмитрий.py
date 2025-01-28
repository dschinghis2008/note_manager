import datetime, json


def save_notes_json(notes, filename):
    with open(filename, 'w', encoding='utf-8') as file:
        json.dump(notes, file, indent=4, ensure_ascii=False)


now = datetime.datetime.now().date()
dt_create_str = str(now)  # для сериализации
dt_issue_str = str(now + datetime.timedelta(days=7))

notes = [
    {'id': '1', 'username': 'user1', 'title': 'работа с файлами', 'content': 'step 3', 'status': 'none',
     'created_date': dt_create_str, 'issue_date': dt_issue_str},
    {'id': '2', 'username': 'user2', 'title': 'grade1', 'content': 'step 4', 'status': 'inproc',
     'created_date': dt_create_str, 'issue_date': dt_issue_str},
    {'id': '3', 'username': 'user3', 'title': 'grade', 'content': 'step 5', 'status': 'close',
     'created_date': dt_create_str, 'issue_date': dt_issue_str}
]
try:  # save to json
    save_notes_json(notes, 'notes.json')
except Exception as e:
    print(e)

try:  # load from json
    with open('notes.json', encoding='utf-8') as file:
        list_from_json = json.loads(file.read())
        for j in list_from_json:
            j['created_date'] = datetime.datetime.strptime(j['created_date'], '%Y-%m-%d').date()
            j['issue_date'] = datetime.datetime.strptime(j['issue_date'], '%Y-%m-%d').date()
            print(f'№: {j['id']}\nuser: {j['username']}\ntitle: {j['title']}\ncontent: {j['content']}\n' +
                  f'status: {j['status']}\ncreate: {j['created_date']}\nissue: {j['issue_date']}\n======')
except FileNotFoundError:
    print('Файл не найден в текущей директории, будет создан новый')
    file = open('notes.json', 'w')
    file.close()
except UnicodeDecodeError:
    print('Файл поврежден или не является текстовым')
except PermissionError:
    print('Отсутствуют права доступа к файлу')
