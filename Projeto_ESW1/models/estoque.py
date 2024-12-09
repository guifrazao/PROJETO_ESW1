from models.produto import Produto

class Estoque:
    def __init__(self):
        self.__produtos: list[Produto] = []

    def adicionar_produto(self, produto: Produto) -> None:
        self.__produtos.append(produto)

    def buscar_produto(self, nome: str) -> Produto | None:
        for produto in self.__produtos:
            if produto.get_nome() == nome:
                return produto
        return None

    def listar_produtos(self) -> list[Produto]:
        return self.__produtos
