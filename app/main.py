from fastapi import FastAPI

from app.routes.focus import router as focus_router
from app.routes.diagnostico import router as diagnostico_router

app = FastAPI(
    title="Nirvana API",
    description="API para registro de níveis de foco e diagnóstico de produtividade",
)

app.include_router(focus_router)
app.include_router(diagnostico_router)