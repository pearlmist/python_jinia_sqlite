import pandas as pd


def get_reader(conn):
 return pd.read_sql("SELECT * FROM reader", conn)


def get_book_reader(conn, reader_id):
 return pd.read_sql("SELECT * FROM book_reader WHERE reader_id = ?", conn, params=(reader_id,))

