from datetime import datetime
from app.database.storage import registros

def criar_registro(dados):
    novo_registro = {
        "id": len(registros) + 1,
        "nivel_foco": dados.nivel_foco,
        "tempo_minutos": dados.tempo_minutos,
        "data_hora": datetime.now(),
        "comentarios": dados.comentarios,
        "categoria": dados.categoria,
        "tags": dados.tags,
        "criado_em": datetime.now()
    }

    registros.append(novo_registro)
    return novo_registro