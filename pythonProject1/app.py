import psycopg2
import os
conn = psycopg2.connect(
    host="127.0.0.1",
    port=5432,
    dbname="users",
    user="postgres",
    password="vaheeda@123",

)





cur=conn.cursor()
cur.execute('DROP TABLE IF EXISTS books;')
cur.execute('CREATE TABLE books (id serial PRIMARY KEY,'
                                 'title varchar (150) NOT NULL,'
                                 'author varchar (50) NOT NULL,'
                                 'pages_num integer NOT NULL,'
                                 'review text,'
                                 'date_added date DEFAULT CURRENT_TIMESTAMP);'
                                 )

# Insert data into the table

cur.execute('INSERT INTO books (title, author, pages_num, review)'
            'VALUES (%s, %s, %s, %s)',
            ('Anna Karenina',
             'Leo Tolstoy',
             864,
             'Another great classic!')
            )

conn.commit()
with conn.cursor() as cursor:
    cursor.execute('SELECT * FROM books')
    print(cursor.fetchall())
    print("connected")
cur.close()
conn.close()