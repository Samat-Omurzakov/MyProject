import sqlite3
import re


def create_connection(db_name):
    conn = None
    try:
        conn = sqlite3.connect(db_name)
        return conn
    except sqlite3.Error as e:
        print(e)

def create_table(conn, sql):
    try:
        cursor = conn.cursor()
        cursor.execute(sql)
    except sqlite3.Error as e:
        print(e)

def create_product(conn, product: tuple):
    try:
        sql = '''insert into products (product_title, price, quantity)
        values (?, ?, ?)
        '''
        cursor = conn.cursor()
        cursor.execute(sql, product)
        conn.commit()
    except sqlite3.Error as e:
        print(e)

def update_quantity(conn, product: tuple):
    try:
        sql = '''update products set quantity = ? where id = ?
        '''
        cursor = conn.cursor()
        cursor.execute(sql, product)
        conn.commit()
    except sqlite3.Error as e:
        print(e)

def update_price(conn, product: tuple):
    try:
        sql = '''update products set price = ? where id = ?
        '''
        cursor = conn.cursor()
        cursor.execute(sql, product)
        conn.commit()
    except sqlite3.Error as e:
        print(e)

def delete_product(conn, id):
    try:
        sql = '''delete from products where id = ?
        '''
        cursor = conn.cursor()
        cursor.execute(sql, (id,))
        conn.commit()
    except sqlite3.Error as e:
        print(e)

def select_all_products(conn):
    try:
        sql = '''select * from products
        '''
        cursor = conn.cursor()
        cursor.execute(sql)
        rows = cursor.fetchall()

        for row in rows:
            print(row)
    except sqlite3.Error as e:
        print(e)

def select_by_price_and_quantity(conn, limit):
    try:
        sql = '''select * from products where price < ? and quantity > ?
        '''
        cursor = conn.cursor()
        cursor.execute(sql, limit)
        rows = cursor.fetchall()

        for row in rows:
            print(row)
    except sqlite3.Error as e:
        print(e)

def search_by_word(conn, word):
    try:
        sql = '''select * from products where product_title like ?
        '''
        cursor = conn.cursor()
        cursor.execute(sql, ('%'+word+'%',))
        rows = cursor.fetchall()

        for row in rows:
            print(row)
    except sqlite3.Error as e:
        print(e)


database = r'hw.db'

sql_create_products_table = '''
create table products (
id integer primary key autoincrement,
product_title varchar(200) not null,
price  double(10, 2) not null default 0.0,
quantity integer(5) not null default 0
)
'''

connection = create_connection(database)
create_table(connection, sql_create_products_table)
create_product(connection, ('Сэндвич с курицей', 80.5, 10))
create_product(connection, ('Сэндвич Хот-дог', 75.89, 5))
create_product(connection, ('Вода негазированная 0.5', 30.25, 8))
create_product(connection, ('Вода газированная 0.5', 30.15, 4))
create_product(connection, ('Вода со вкусом лимона 0.5', 35.67, 12))
create_product(connection, ('Вода со вкусом лимона 1л.', 49.99, 9))
create_product(connection, ('Вафли с шоколадом', 120.34, 15))
create_product(connection, ('Вафли со сгущенкой', 115.58, 7))
create_product(connection, ('Печенье овсяные', 138.12, 15))
create_product(connection, ('Чипсы со вкусом сыра', 125.19, 11))
create_product(connection, ('Чипсы со вкусом краба', 123.79, 8))
create_product(connection, ('Жвачка с мятой', 34.45, 17))
create_product(connection, ('Жвачка с арбузом', 35.23, 10))
create_product(connection, ('Молоко 2,5%', 96.5, 6))
create_product(connection, ('Молоко 3,2%', 97.1, 12))
update_quantity(connection, (13, 7))
update_price(connection, (33.33, 12))
delete_product(connection, 2)
select_all_products(connection)
select_by_price_and_quantity(connection, (100, 5))
search_by_word(connection, 'Вода')

connection.close()
