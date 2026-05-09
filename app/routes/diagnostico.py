from fastapi import APIRouter
from app.services.diagnostico_service import gerar_diagnostico

router = APIRouter()

@router.get("/diagnostico-produtividade")
def diagnostico():
    return gerar_diagnostico()