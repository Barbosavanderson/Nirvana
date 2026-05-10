import sqlite3

DATABASE_NAME = "nirvana.db"
def get_connection():
    conn = sqlite3.connect(DATABASE_NAME)
    conn.row_factory = sqlite3.Row
    return conn

def criar_tabela():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS registros (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nivel_foco INTEGER NOT NULL,
            tempo_minutos INTEGER NOT NULL,
            comentario TEXT NOT NULL,
            categoria TEXT,
            tags TEXT,
            criado_em TEXT NOT NULL
        )
    ''')
    conn.commit()
    conn.close()