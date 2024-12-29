status = ''
select_status = ''
while select_status not in ('1', '2', '3', '4'):
    print('Для изменения статуса заметки задайте значение от 1 до 4:')
    select_status = input('1 - в процессе\n2 - выполнен\n3 - отложен\n4 - другое значение: ')
else:
    if select_status == '1':
        status = 'в процессе'
    elif select_status == '2':
        status = 'выполнен'
    elif select_status == '3':
        status = 'отложен'
    else:
        status = input('Введите новое значение статуса заметки: ')
print('Статус заметки изменен на: ', status)
