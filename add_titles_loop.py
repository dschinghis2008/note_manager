content = ''
set_titles = {content}

while content != 'stop':
    content = input('Введите заголовок или "stop" для завершения ввода: ')
    set_titles.add(content)
else:
    print('Ввод заголовков завершен. Дубли исключены. Введены следующие заголовки:')
set_titles.remove('stop')
set_titles.remove('')
for title in set_titles:
    print(title)
