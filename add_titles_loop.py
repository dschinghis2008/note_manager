content = ''
set_titles = set()

while content != 'stop':
    content = input('Введите заголовок или "stop" для завершения ввода:')
    if content != 'stop':
        set_titles.add(content)
else:
    print('Ввод заголовков завершен. Дубли исключены. Введены следующие заголовки:')
for title in set_titles:
    print(title)
