from datetime import datetime
from app.database.storage import get_connection


def criar_registro(dados):
    conn = get_connection()
    cursor = conn.cursor()
    criado_em = datetime.now().isoformat()
    tags_str = ",".join(dados.tags) if dados.tags else ""
    cursor.execute('''
        INSERT INTO registros (
                    nivel_foco,
                    tempo_minutos,
                    comentario, 
                    categoria, 
                    tags, 
                    criado_em
        )
        VALUES (?, ?, ?, ?, ?, ?)
    ''', (dados.nivel_foco, 
          dados.tempo_minutos,
          dados.comentarios or "", 
          dados.categoria, 
          tags_str, criado_em
          ))
    conn.commit()
    registro_id = cursor.lastrowid
    conn.close()
    
    return {
        "id": registro_id,
        "nivel_foco": dados.nivel_foco,
        "tempo_minutos": dados.tempo_minutos,        
        "comentarios": dados.comentarios,
        "categoria": dados.categoria,
        "tags": dados.tags,
        "criado_em": criado_em
    }
