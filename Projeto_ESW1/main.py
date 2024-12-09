from models.estoque import Estoque
from controllers.produto_controller import ProdutoController
from controllers.caixa_controller import CaixaController
from controllers.cliente_controller import ClienteController
from utils.autenticar import login_usuario
from tabulate import tabulate

def inicializar_estoque(estoque):
    """Adiciona produtos pré-cadastrados."""
    produtos = [
        ("Edredom", 150.00, 20),
        ("Boneca de pano", 50.00, 30),
        ("Toalha de banho", 30.00, 50),
        ("Lençol de casal", 80.00, 25),
        ("Travesseiro", 40.00, 40)
    ]
    for nome, preco, quantidade in produtos:
        estoque.adicionar_produto(Produto(nome, preco, quantidade))

def main():
    estoque = Estoque()
    caixa_controller = CaixaController()
    produto_controller = ProdutoController(estoque)
    cliente_controller = ClienteController()

    # Adicionar produtos pré-cadastrados
    inicializar_estoque(estoque)

    # Login
    usuario = login_usuario()
    if not usuario:
        return

    while True:
        print("\n===== Menu Principal =====")
        print("1. Cadastrar cliente")
        print("2. Cadastrar produto")
        print("3. Checar estoque")
        print("4. Fazer compra")
        print("5. Fechar caixa")
        print("0. Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            nome = input("Nome: ")
            contato = input("Contato: ")
            endereco = input("Endereço: ")
            print(cliente_controller.cadastrar_cliente(nome, contato, endereco))

        elif opcao == "2":
            nome = input("Nome do produto: ")
            preco = float(input("Preço: "))
            quantidade = int(input("Quantidade: "))
            print(produto_controller.cadastrar_produto(nome, preco, quantidade))

        elif opcao == "3":
            produtos = estoque.listar_produtos()
            tabela = [[p.get_nome(), f"R$ {p.get_preco():.2f}", p.get_quantidade()] for p in produtos]
            print(tabulate(tabela, headers=["Produto", "Preço", "Quantidade"], tablefmt="grid"))

        elif opcao == "4":
            produtos = estoque.listar_produtos()
            tabela = [[i, p.get_nome(), f"R$ {p.get_preco():.2f}", p.get_quantidade()] for i, p in enumerate(produtos)]
            print(tabulate(tabela, headers=["#", "Produto", "Preço", "Quantidade"], tablefmt="grid"))

            indice = int(input("Digite o número do produto (ou -1 para cancelar): "))
            if 0 <= indice < len(produtos):
                quantidade = int(input("Quantas unidades deseja comprar? "))
                produto = produtos[indice]
                if produto.get_quantidade() >= quantidade:
                    total = quantidade * produto.get_preco()
                    produto.set_quantidade(produto.get_quantidade() - quantidade)
                    caixa_controller.registrar_venda(total)
                    print(f"Adicionado {quantidade} unidades de {produto.get_nome()} ao carrinho. Total: R$ {total:.2f}")
                    
                    # Perguntar pelo método de pagamento
                    metodo_pagamento = input("Informe o método de pagamento (1 - Dinheiro, 2 - Cartão): ")
                    
                    if metodo_pagamento == "1":  # Pagamento em Dinheiro
                        dinheiro = float(input(f"Digite o valor entregue: R$ "))
                        if dinheiro >= total:
                            troco = dinheiro - total
                            print(f"Compra finalizada! Total: R$ {total:.2f}, Troco: R$ {troco:.2f}")
                        else:
                            print("Valor insuficiente!")
                    
                    elif metodo_pagamento == "2":  # Pagamento com Cartão
                        print(f"Compra finalizada! Total: R$ {total:.2f} (Pagamento: Cartão)")

                    else:
                        print("Método de pagamento inválido.")
                else:
                    print("Estoque insuficiente!")
            else:
                print("Produto inválido.")

        elif opcao == "5":
            total = caixa_controller.fechar_caixa()
            print(f"Caixa fechado. Total de vendas: R$ {total:.2f}")

        elif opcao == "0":
            print("Encerrando o programa. Até logo!")
            break

        else:
            print("Opção inválida!")

if __name__ == "__main__":
    from models.produto import Produto
    main()
