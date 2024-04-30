import psycopg2

conn = psycopg2.connect(dbname='n42',
                        user='postgres' ,
                        host='localhost' ,
                        password='1201',
                        port='5432')
cur = conn.cursor()
def create_table_func():
    create_table = '''CREATE TABLE IF NOT EXISTS products
(
        id SERIAL PRIMARY KEY,
        product_name varchar(20) NOT NULL,
        price float not null,
        color varchar(20) NOT NULL
);
'''
    cur.execute(create_table)
    conn.commit()
create_table_func()

def insert_data():
    insert_into = """ INSERT INTO products (product_name,price,color)
    VALUES
        ('iphone 15',1200,'white'),
        ('Samsung Galaxy S23',1000,'black'),
        ('Honor',500,'blue')
"""
    cur.execute(insert_into)
    conn.commit()
insert_data()


def delete_data():

    delete_query = """
    DELETE FROM products
    where id = 3
"""
    cur.execute(delete_query)
    conn.commit()
delete_data()

def update_data(price,color):
    data = (price,color)
    update_query = """UPDATE products
    SET price = price + 100 and color = %s
    where id = 1
"""
    cur.execute(update_query)
    conn.commit()
update_data('iphone 15','white')

def select_all_data():
    select_all_query = """SELECT * FROM products
"""
    cur.execute(select_all_query)
    conn.commit()
select_all_data()

def select_one_data():
    select_one = """SELECT * FROM products
    where price = 1100
"""
    cur.execute(select_one)
    conn.commit()
select_one_data()

cur.close()
conn.close()




