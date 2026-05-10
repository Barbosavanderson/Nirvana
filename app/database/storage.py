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

def paginacao_registros(pagina: int = 1, tamanho: int = 10):
    conn = get_connection()
    cursor = conn.cursor()
    offset = (pagina - 1) * tamanho
    cursor.execute("SELECT COUNT(*) as total FROM registros")
    total = cursor.fetchone()['total']
    cursor.execute(
    """
    SELECT * FROM registros
    ORDER BY criado_em DESC
    LIMIT ? OFFSET ?
    """,
    (tamanho, offset)
    )

    registros = cursor.fetchall()
    conn.close()

    return [dict(registro) for registro in registros]

paginacao_registro = paginacao_registros
paginacao_registros_service = paginacao_registros
