import sqlite3

DATABASE_NAME = "nirvana.db"
def get_connection():
    conn = sqlite3.connect(DATABASE_NAME)
    conn.row_factory = sqlite3.Row
    return conn

# VERSÃO 1: Refatoração Padrão (Context Manager)
# def criar_tabela():
#     with get_connection() as conn:
#         conn.execute('''
#             CREATE TABLE IF NOT EXISTS registros (
#                 id INTEGER PRIMARY KEY AUTOINCREMENT,
#                 nivel_foco INTEGER NOT NULL,
#                 tempo_minutos INTEGER NOT NULL,
#                 comentario TEXT NOT NULL,
#                 categoria TEXT,
#                 tags TEXT,
#                 criado_em TEXT NOT NULL
#             )
#         ''')

# VERSÃO 2: Clean Code (Responsabilidade Única)
# def _obter_schema_registros():
#     return '''
#         CREATE TABLE IF NOT EXISTS registros (
#             id INTEGER PRIMARY KEY AUTOINCREMENT,
#             nivel_foco INTEGER NOT NULL,
#             tempo_minutos INTEGER NOT NULL,
#             comentario TEXT NOT NULL,
#             categoria TEXT,
#             tags TEXT,
#             criado_em TEXT NOT NULL
#         )
#     '''
#
# def criar_tabela():
#     with get_connection() as conn:
#         conn.execute(_obter_schema_registros())

# VERSÃO 3: Concisa (Menos de 20 linhas, sem alteração de nome)
def criar_tabela():
    query = "CREATE TABLE IF NOT EXISTS registros (id INTEGER PRIMARY KEY AUTOINCREMENT, nivel_foco INTEGER NOT NULL, tempo_minutos INTEGER NOT NULL, comentario TEXT NOT NULL, categoria TEXT, tags TEXT, criado_em TEXT NOT NULL)"
    with get_connection() as conn: conn.execute(query)

def paginacao_registros(pagina: int = 1, tamanho: int = 10):
    offset = (pagina - 1) * tamanho

    with get_connection() as conn:
        cursor = conn.cursor()

        cursor.execute("SELECT COUNT(*) AS total FROM registros")
        total = cursor.fetchone()["total"]

        cursor.execute(
            """
            SELECT * FROM registros
            ORDER BY criado_em DESC
            LIMIT ? OFFSET ?
            """,
            (tamanho, offset)
        )

        registros = cursor.fetchall()

    return {
        "pagina": pagina,
        "tamanho": tamanho,
        "total": total,
        "registros": [dict(registro) for registro in registros]
    }

paginacao_registro = paginacao_registros
paginacao_registros_service = paginacao_registros
