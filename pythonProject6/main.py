import sqlite3
import pandas as pd
from jinja2 import Template
from room_model import get_room # , get_book_reader

# создаем базу данных и устанавливаем соединение с ней
con = sqlite3.connect("booking.sqlite")
# открываем файл с дампом базой данных
f_template = open('room_templ.html', 'r', encoding='utf-8-sig')
# читаем данные из файла
html = f_template.read()
# закрываем файл с дампом
f_template.close()
template = Template(html)
floor = 9
df_room = get_room(con, floor)
result_html = template.render(
    floor = floor,
    rooms = df_room,
    len = len
)
f = open('room.html', 'w', encoding ='utf-8-sig')
# выводим сгенерированную страницу в файл
f.write(result_html)
# pd.set_option('display.max_colwidth', None)

# print(get_room(con, 10))

con.close()