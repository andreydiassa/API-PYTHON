from fastapi import FastAPI
from pydantic import BaseModel, Field
from typing import List

# Criação da API
app = FastAPI()

# Banco de dados fake (memoria)
produtos = []

# Modelo do produto
class Produto(BaseModel):
    nome: str
    preco: float 

# GET - Listar produtos
@app.get("/produtos")
def listar_produtos():

    if not produtos:
        return {"mensagem": "Nenhum produto cadastrado"}

    return produtos

# POST - Cadastrar produtos
@app.post("/produtos")
def cadastrar_produto(produtos_recebidos: List[Produto]):

    for produto in produtos_recebidos:
        produtos.append(produto)

    return {
        "mensagem": "Produtos cadastrados com sucesso",
        "total": len(produtos_recebidos)
    }

# PUT - Atualizar produto
@app.put("/produtos/{id}")
def atualizar_produto(id: int, produto: Produto):

    if id >= len(produtos):
        return {"erro": "Produto não encontrado"}

    produtos[id] = produto

    return {
        "mensagem": "Produto atualizado com sucesso"
    }

# DELETE - Remover produto
@app.delete("/produtos/{id}")
def deletar_produto(id: int):

    if id >= len(produtos):
        return {"erro": "Produto não encontrado"}

    produtos.pop(id)

    return {
        "mensagem": "Produto removido com sucesso"
    }