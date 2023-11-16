import pandas as pd


def get_room(conn, floor):
    if floor < 10:
        floor_temp = "0" + str(floor)
    else:
        floor_temp = str(floor)

    return pd.read_sql('''
        SELECT 
            room_name AS Номер,
            type_room_name AS Тип_номера,
            price AS Цена
        FROM 
            room 
            NATURAL JOIN type_room
        WHERE 
            substr(Room_name, 3, 2) = ?
        ORDER BY 
            price ASC, 
            room_name ASC
            ''', conn, params=(floor_temp,))