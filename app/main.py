from fastapi import FastAPI
from app.api.routes import router

app = FastAPI(
    title="API Raízes do Nordeste",
    version="1.0.0",
    description="Sistema de pedidos com FastAPI + MySQL"
)

app.include_router(router, prefix="/api")