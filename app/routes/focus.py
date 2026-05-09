from fastapi import APIRouter
from app.models.registro import RegistroFocoInput
from app.services.focus_service import criar_registro

router = APIRouter()

@router.post("/registrar-foco")
def registrar_foco(dados: RegistroFocoInput):
    return criar_registro(dados)