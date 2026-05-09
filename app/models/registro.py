from pydantic import BaseModel, Field
from typing import Optional
from datetime import datetime
from enum import Enum

class CategoriaEnum(str, Enum):
    coding = "coding"
    reuniao = "reuniao"
    estudo = "estudo"
    outro = "outro"

class RegistroFocoInput(BaseModel):
    nivel_foco: int = Field(..., ge=1, le=10, description="Nível de foco de 1 a 10")
    tempo_minutos: int = Field(..., gt=0, description="Tempo invéstido em minutos")
    comentarios: Optional[str] = Field(None, description="Comentários adicionais sobre o registro")
    
    categoria: Optional[CategoriaEnum] = Field(None, description="Categoria do registro")
    tags: Optional[list[str]] = []
    

class RegistroFocoOutput(RegistroFocoInput):
    id: int = Field(..., description="ID do registro")
    criado_em: datetime 

class DiagnosticoOutput(BaseModel):
     total_registros: int
     media_foco: float
     tempo_total_minutos: int
     mensagem_feedback: str
     distribuicao_foco: dict