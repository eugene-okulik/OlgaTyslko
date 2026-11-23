import os
from datetime import datetime, timedelta

base_path = os.path.dirname(os.path.abspath(__file__))
homework_path = os.path.dirname(os.path.dirname(base_path))
file_path = os.path.join(homework_path, 'eugene_okulik', 'hw_13', 'data.txt')

try:
    with open(file_path, encoding='utf-8') as data_file:
        for line in data_file:
            left_part = line.split(' - ', maxsplit=1)[0]
            num_str, date_str = left_part.split('. ', maxsplit=1)
            line_num = int(num_str)
            date_obj = datetime.fromisoformat(date_str)
            if line_num == 1:
                next_week = date_obj + timedelta(weeks=1)
                print(f'Дата из файла: {date_obj}, дата через неделю: {next_week}')
            elif line_num == 2:
                print(f'День недели: {date_obj.strftime("%A")}')
            elif line_num == 3:
                diff_date = datetime.now() - date_obj
                print(f'Эта дата была {diff_date.days} дней назад')
except FileNotFoundError:
    print(f'Файл не найден по пути: {file_path}')
except ValueError as err:
    print(f'Ошибка формата данных в файле: {err}')
