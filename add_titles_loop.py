content = ''
set_titles = {content}

while content != 'stop':
    content = input('Введите заголовок или "stop" для завершения ввода:')
    if content != 'stop':
        set_titles.add(content)
else:
    print('Ввод заголовков завершен. Дубли исключены. Введены следующие заголовки:')
set_titles.remove('')
for title in set_titles:
    print(title)
