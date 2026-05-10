from app.database.storage import get_connection

def gerar_feedback(media):
    if media < 2:
        return "uma rapariga é bom tutututuututtu"
    elif media < 3:
        return " Olha o caba lá, nível de concentração igual ao do squad do Smzinho"
    elif media < 4:
        return "Já estamos sentindo o cheiro do sucesso ou é algo queimando? "
    elif media <= 5:
        return "Você está no caminho certo! Já podemos jogar um Darksouls, matar Names king borraaaa? "
    else:
        return "I'm so happy 'cause today i found my friend, he's in my head"
    
def gerar_diagnostico():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM registros')
    registros = cursor.fetchall()
    conn.close()
    if not registros:
        return{
            "total_registros": 0,
            "media_foco": 0,
            "tempo_total_minutos": 0,
            "mensagem_feedback": "Nenhum registro encontrado. Vai começar a estudar ou vai ficar no insta?!?!?",
            "distribuicao_foco": {}
        }
    
    total = len(registros)
    soma_foco = sum(registro["nivel_foco"] for registro in registros)
    tempo_total = sum(r["tempo_minutos"] for r in registros)
    media = soma_foco / total
    distribuicao = {}

    for i in range(1, 6):
        distribuicao[str(i)] = len(
            [r for r in registros if r["nivel_foco"] == i]
        )

    return {
        "total_registros": total,
        "media_foco": round(media, 2),
        "tempo_total_minutos": tempo_total,
        "mensagem_feedback": gerar_feedback(media),
        "distribuicao_foco": distribuicao
    }