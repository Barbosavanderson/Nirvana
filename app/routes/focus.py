from fastapi import APIRouter
from fastapi import Query
from app.models.registro import RegistroFocoInput
from app.services.focus_service import criar_registro, listar_registros_service


router = APIRouter()

@router.post("/registrar-foco")
def registrar_foco(dados: RegistroFocoInput):
    return criar_registro(dados)

# Definir rota para listagem de registros com paginação
@router.get("/registros")
def listar_registros(
    pagina: int = Query(1, ge=1, description=" começa na primeira pág (a partir de 1)"),
    tamanho: int = Query(10, ge=1, le=50, description="número de registros listados por página (1-50)")
):
    return listar_registros_service(pagina, tamanho)
