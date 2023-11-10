import sqlite3

# 1. Izveido datu bāzi un pieslēdzies tai
conn = sqlite3.connect('piemers.db')
cursor = conn.cursor()

# 2. Izveido tabulu
cursor.execute('''
    CREATE TABLE IF NOT EXISTS lietotaji (
        id INTEGER PRIMARY KEY,
        vards TEXT NOT NULL,
        uzvards TEXT NOT NULL,
        epasts TEXT NOT NULL UNIQUE
    )
''')

# 3. Izveido otru tabulu ar relāciju
cursor.execute('''
    CREATE TABLE IF NOT EXISTS pasutijumi (
        id INTEGER PRIMARY KEY,
        lietotaja_id INTEGER,
        produkta_nosaukums TEXT NOT NULL,
        daudzums INTEGER NOT NULL,
        FOREIGN KEY (lietotaja_id) REFERENCES lietotaji(id)
    )
''')

# 4. Ievieto datus lietotaju tabulā
#cursor.execute("INSERT INTO lietotaji (vards, uzvards, epasts) VALUES (?, ?, ?)", ('Janis', 'Berzins', 'janis.berzins@example.com'))
#cursor.execute("INSERT INTO lietotaji (vards, uzvards, epasts) VALUES (?, ?, ?)", ('Anna', 'Liepa', 'anna.liepa@example.com'))

# 5. Ievieto datus pasūtījumu tabulā
cursor.execute("INSERT INTO pasutijumi (lietotaja_id, produkta_nosaukums, daudzums) VALUES (?, ?, ?)", (1, 'Dators', 2))
cursor.execute("INSERT INTO pasutijumi (lietotaja_id, produkta_nosaukums, daudzums) VALUES (?, ?, ?)", (2, 'Televizors', 1))

# 6. Saglabā izmaiņas un aizver savienojumu
conn.commit()
conn.close()
