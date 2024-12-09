from models.estoque import Estoque
from models.produto import Produto

class ProdutoController:
    def __init__(self, estoque: Estoque):
        self.__estoque = estoque

    def cadastrar_produto(self, nome: str, preco: float, quantidade: int) -> str:
        produto = Produto(nome, preco, quantidade)
        self.__estoque.adicionar_produto(produto)
        return f"Produto '{nome}' cadastrado com sucesso!"
