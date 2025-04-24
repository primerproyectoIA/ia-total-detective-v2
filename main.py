from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import re

app = FastAPI()

# Permitir CORS para conectar con CodePen
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class InputData(BaseModel):
    content: str

@app.post("/analizar")
async def analizar(data: InputData):
    texto = data.content

    # Algoritmo Detective básico (v1)
    patrones_sospechosos = [
        r"\bdespierta\b",
        r"\bverdad que no quieren que sepas\b",
        r"\bcontrol mental\b",
        r"\bélite\b",
        r"\bdesinformación\b",
        r"https://t.me/",  # enlaces a Telegram
        r"\bplandemia\b",
        r"\bmatrix\b"
    ]

    coincidencias = []
    for patron in patrones_sospechosos:
        if re.search(patron, texto, re.IGNORECASE):
            coincidencias.append(patron)

    resultado = {
        "resultado": "Posible contenido manipulado o con narrativa sospechosa" if coincidencias else "Contenido sin patrones evidentes",
        "coincidencias": coincidencias
    }

    return resultado
