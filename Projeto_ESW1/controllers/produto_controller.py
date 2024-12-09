from models.estoque import Estoque
from models.produto import Produto
from controllers.caixa_controller import CaixaController

class ProdutoController:
    def __init__(self, estoque: Estoque, caixa_controller):
        self.__estoque = estoque
        self.__caixa_controller = caixa_controller

    def cadastrar_produto(self, nome: str, preco: float, quantidade: int) -> str:
        produto_existente = self.__estoque.buscar_produto(nome)
        if produto_existente:
            return f"Produto '{nome}' já existe!"
        
        produto = Produto(nome, preco, quantidade)
        self.__estoque.adicionar_produto(produto)
        return f"Produto '{nome}' cadastrado com sucesso!"

    def listar_produtos(self) -> None:
        produtos = self.__estoque.listar_produtos()
        for i, produto in enumerate(produtos):
            status = "Repor" if produto.precisa_reposicao() else "OK"
            print(f"{i}. {produto.get_nome()} - R$ {produto.get_preco()} - Qtd: {produto.get_quantidade()} ({status})")

    def comprar_produto(self) -> None:
        self.listar_produtos()
        indice = int(input("Digite o número do produto que deseja comprar (ou -1 para finalizar): "))
        if indice == -1:
            return
        
        quantidade = int(input("Quantas unidades deseja comprar? "))
        produtos = self.__estoque.listar_produtos()

        if 0 <= indice < len(produtos):
            produto = produtos[indice]
            if produto.get_quantidade() >= quantidade:
                produto.set_quantidade(produto.get_quantidade() - quantidade)
                total = quantidade * produto.get_preco()
                self.__caixa_controller.registrar_venda(total)
                print(f"Compra realizada! Total: R$ {total:.2f}")
            else:
                print("Quantidade insuficiente no estoque!")
        else:
            print("Produto inválido!")
