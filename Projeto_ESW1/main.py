from models.estoque import Estoque
from controllers.produto_controller import ProdutoController
from controllers.caixa_controller import CaixaController
from models.produto import Produto
from tabulate import tabulate  # Importando tabulate para exibir a tabela

def main():
    # Inicialização dos sistemas
    estoque: Estoque = Estoque()
    caixa_controller: CaixaController = CaixaController()
    produto_controller: ProdutoController = ProdutoController(estoque, caixa_controller)

    # Pré-cadastro de produtos
    produtos_iniciais: list[dict[str, float | int | str]] = [
        {"nome": "Arroz", "preco": 25.0, "quantidade": 100},
        {"nome": "Feijão", "preco": 10.0, "quantidade": 200},
        {"nome": "Macarrão", "preco": 5.0, "quantidade": 150},
        {"nome": "Óleo", "preco": 8.0, "quantidade": 50},
        {"nome": "Açúcar", "preco": 4.5, "quantidade": 80}
    ]

    print("Cadastrando produtos iniciais...\n")
    for produto in produtos_iniciais:
        produto_controller.cadastrar_produto(
            produto["nome"], produto["preco"], produto["quantidade"]
        )

    print("Produtos cadastrados com sucesso!\n")

    # Simulação do Menu
    while True:
        print("\n1. Cadastrar produto")
        print("2. Listar produtos")
        print("3. Fazer compra")
        print("4. Fechar caixa")
        print("5. Sair")
        opcao: str = input("Escolha uma opção: ")

        if opcao == '1':
            nome: str = input("Nome do produto: ")
            preco: float = float(input("Preço: "))
            quantidade: int = int(input("Quantidade: "))
            print(produto_controller.cadastrar_produto(nome, preco, quantidade))

        elif opcao == '2':
            print("\nLista de Produtos Disponíveis:")
            produtos = estoque.listar_produtos()
            produtos_tabela = [
                [i, p.get_nome(), f"R$ {p.get_preco():.2f}", p.get_quantidade(), 
                "Repor" if p.precisa_reposicao() else "OK"]
                for i, p in enumerate(produtos)
            ]
            print(tabulate(produtos_tabela, headers=["#", "Produto", "Preço", "Quantidade", "Status"], tablefmt="grid"))

        elif opcao == '3':
            print("\nLista de Produtos Disponíveis para Compra:")
            produtos = estoque.listar_produtos()
            produtos_tabela = [
                [i, p.get_nome(), f"R$ {p.get_preco():.2f}", p.get_quantidade()]
                for i, p in enumerate(produtos)
            ]
            print(tabulate(produtos_tabela, headers=["#", "Produto", "Preço", "Quantidade"], tablefmt="grid"))

            try:
                indice: int = int(input("\nDigite o número do produto que deseja comprar (ou -1 para finalizar a compra): "))
                if indice == -1:
                    continue

                quantidade: int = int(input(f"Quantas unidades de {produtos[indice].get_nome()} deseja comprar? "))
                if 0 <= indice < len(produtos):
                    produto: Produto = produtos[indice]
                    if produto.get_quantidade() >= quantidade:
                        total: float = quantidade * produto.get_preco()
                        produto.set_quantidade(produto.get_quantidade() - quantidade)
                        caixa_controller.registrar_venda(total)
                        print(f"Adicionado {quantidade} unidades de {produto.get_nome()} ao carrinho. Total parcial: R$ {total:.2f}")
                        print(f"Estoque atualizado: {produto.get_quantidade()} unidades restantes de {produto.get_nome()}.\n")
                        
                        metodo_pagamento: int = int(input("Informe o método de pagamento (1 - Dinheiro, 2 - Cartão): "))
                        if metodo_pagamento == 1:
                            dinheiro: float = float(input("Digite o valor entregue: "))
                            troco: float = dinheiro - total
                            print(f"Compra finalizada! Total da compra: R$ {total:.2f}, Troco: R$ {troco:.2f}")
                        else:
                            print(f"Compra finalizada! Total da compra: R$ {total:.2f} (Pagamento: Cartão)\n")
                    else:
                        print("Quantidade insuficiente no estoque!\n")
                else:
                    print("Produto inválido!\n")
            except (ValueError, IndexError):
                print("Entrada inválida. Tente novamente!\n")

        elif opcao == '4':
            total: float = caixa_controller.fechar_caixa()
            print(f"\nCaixa fechado! Total de vendas: R$ {total:.2f}\n")

        elif opcao == '5':
            print("\nEncerrando o programa. Até mais!\n")
            break

        else:
            print("\nOpção inválida! Tente novamente.\n")


if __name__ == "__main__":
    main()
