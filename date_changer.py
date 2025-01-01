import datetime

temp_created_date = datetime.datetime.strptime('22.12', '%d.%m')
temp_issue_date = datetime.datetime.strptime('31.12', '%d.%m')
print('Краткая дата создания: ', temp_created_date.strftime('%d.%m'))
print('Краткая дата истечения: ', temp_issue_date.strftime('%d.%m'))
