from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

chamados = []

class Chamado(BaseModel):
    usuario: str
    problema: str
    status: str = "Aberto"


@app.get("/")
def inicio():
    return {"mensagem": "API de Chamados funcionando!"}


@app.get("/chamados")
def listar_chamados():
    return chamados


@app.post("/chamados")
def criar_chamado(chamado: Chamado):
    novo_chamado = chamado.model_dump()
    novo_chamado["id"] = len(chamados) + 1

    chamados.append(novo_chamado)

    return novo_chamado