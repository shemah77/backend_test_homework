import sqlite3

con = sqlite3.connect('db_video.sqlite')
cur = con.cursor()

# Напишите SQL запрос в строке.
cur.execute('''
    SELECT name FROM sqlite_master 
    WHERE type='table';
''')

table = cur.fetchall()[0][0] # Получите имя таблицы через атрибут курсора.
print (table)
# table1 = table[0]


# table = table1[0]
# Напишите SQL запрос в строке.
results = cur.execute(f'''
      SELECT title, description 
FROM {table};
''')


for result in results:
    print(result)

con.close()