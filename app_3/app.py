import uvicorn
from fastapi import FastAPI

app = FastAPI()


vendas = {
        1: {"item": "Vaca", "preco_unitario": 4, "quantidade": 5},
        2: {"item": "Moleza", "preco_unitario": 10, "quantidade": 15},
        3: {"item": "Vaca", "preco_unitario": 7, "quantidade": 19},
        4: {"item": "Vaca", "preco_unitario": 9, "quantidade": 26}
        }

@app.get("/")
def home():
    return {"Vendas": len(vendas)}


@app.get("/vendas/{id_venda}")
def pegar_venda(id_venda: int):
    if id_venda in vendas:
        return vendas[id_venda]
    else:
        return {"Erro": "ID venda inexistente"}


if __name__ == "__main__":
    uvicorn.run(app, port=8000)
