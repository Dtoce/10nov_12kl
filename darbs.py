import sqlite3

# 1. Izveido datu bāze un jāpieslēdzas tai
conn=sqlite3.connect('piemers.db')
cursor=conn.cursor()

# 2. Izveidot tabulu
cursor.execute('''
               CREATE TABLE IF NOT EXISTS lietotaji(
                   id INTEGER PRIMARY KEY,
                   vards TEXT NOT NULL,
                   uzvards TEXT NOT NULL,
                   epasts TEXT NOT NULL UNIQUE
               )
               ''')













conn.commit()
conn.close()
