import sqlite3

conn = sqlite3.connect("escola.db")
cursor = conn.cursor()

cursor.execute("""
    SELECT * FROM disciplinas
""")

disciplinas = cursor.fetchall()

for disciplina in disciplinas:
    print(disciplina)

conn.close()