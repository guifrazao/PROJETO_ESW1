from gerenciadorVendas import GerenciadorVendas
from typing import List
from tabulate import tabulate


class Interface:
    def __init__(self, gerenciador: GerenciadorVendas) -> None:
        """
        Inicializa a interface de interação com o usuário.
        :param gerenciador: Instância do GerenciadorVendas.
        """
        self.__gerenciador = gerenciador

    def menuAbrirCaixa(self) -> None:
        """Menu para abrir o caixa (realizar login do vendedor)."""
        print("\n--- Abrir Caixa ---")
        codigo = int(input("Digite o código do vendedor: "))
        senha = input("Digite a senha do vendedor: ")

        if self.__gerenciador.abrirCaixa(codigo, senha):
            print("Caixa aberto com sucesso.")
        else:
            print("Erro ao abrir o caixa. Verifique os dados e tente novamente.")

    def menuCadastrarCliente(self) -> None:
        """Menu para cadastrar um novo cliente."""
        print("\n--- Cadastrar Cliente ---")
        nome = input("Digite o nome do cliente: ")
        cpf = input("Digite o CPF do cliente (somente números): ")
        telefone = input("Digite o telefone do cliente (formato: (XX) XXXXX-XXXX): ")

        self.__gerenciador.cadastrarCliente(nome, cpf, telefone)

    def menuFecharCaixa(self) -> None:
        """Menu para fechar o caixa."""
        print("\n--- Fechar Caixa ---")
        print("Caixa fechado. Até logo!")



    def menuFazerCompra(self) -> None:
        """Menu para realizar uma compra."""
        print("\n--- Fazer Compra ---")
        cpf_cliente = input("Digite o CPF do cliente: ")

        # Listar os produtos disponíveis
        produtos = self.__gerenciador.consultarProdutos()
        if not produtos:
            print("Nenhum produto disponível no estoque.")
            return

        headers = ["ID", "Nome", "Preço (R$)", "Quantidade"]
        tabela_produtos = [(produto.get_id(), produto.get_nome(), produto.get_preco(), produto.get_quantidade()) for produto in produtos]
        print("Lista de produtos disponíveis para compra:")
        print(tabulate(tabela_produtos, headers=headers, tablefmt="grid"))

        # Processo de compra
        carrinho = {}
        while True:
            try:
                produto_id = int(input("Digite o número do produto que deseja comprar (ou -1 para finalizar a compra): "))
                if produto_id == -1:
                    break

                produto = self.__gerenciador.buscarProduto(produto_id)
                if not produto:
                    print("Produto não encontrado. Tente novamente.")
                    continue

                quantidade = int(input(f"Quantas unidades de {produto.get_nome()} deseja comprar? "))
                if quantidade > produto.get_quantidade():
                    print(f"Quantidade indisponível! Estoque atual: {produto.get_quantidade()}.")
                    continue

                # Adicionar ao carrinho
                if produto_id in carrinho:
                    carrinho[produto_id]["quantidade"] += quantidade
                else:
                    carrinho[produto_id] = {"produto": produto, "quantidade": quantidade}

                produto.set_quantidade(produto.get_quantidade() - quantidade)
                print(f"Adicionado {quantidade} unidade(s) de {produto.get_nome()} ao carrinho.")
            except ValueError:
                print("Entrada inválida. Por favor, digite um número válido.")

        # Finalizar compra
        if not carrinho:
            print("Nenhum produto foi adicionado ao carrinho. Compra cancelada.")
            return

        # Resumo da compra
        total = 0
        print("\nResumo da compra:")
        resumo = []
        for item in carrinho.values():
            produto = item["produto"]
            quantidade = item["quantidade"]
            subtotal = produto.get_preco() * quantidade
            total += subtotal
            resumo.append([produto.get_nome(), quantidade, f"R$ {subtotal:.2f}"])

        headers_resumo = ["Produto", "Quantidade", "Subtotal"]
        print(tabulate(resumo, headers=headers_resumo, tablefmt="grid"))
        print(f"Total: R$ {total:.2f}")

        # Seleção de método de pagamento
        while True:
            metodo_pagamento = input("Informe o método de pagamento (1 - Dinheiro, 2 - Cartão): ")
            if metodo_pagamento == "1":
                # Pagamento em dinheiro
                while True:
                    try:
                        valor_entregue = float(input(f"Digite o valor entregue pelo cliente (R$): "))
                        if valor_entregue < total:
                            print(f"Valor insuficiente! O total é R$ {total:.2f}. Tente novamente.")
                        else:
                            troco = valor_entregue - total
                            print(f"Pagamento realizado com sucesso via Dinheiro!")
                            print(f"Troco: R$ {troco:.2f}")
                            break
                    except ValueError:
                        print("Entrada inválida. Por favor, digite um valor numérico válido.")
                break

            elif metodo_pagamento == "2":
                # Pagamento no cartão
                print("Pagamento realizado com sucesso via Cartão!")
                break
            else:
                print("Método inválido. Escolha 1 para Dinheiro ou 2 para Cartão.")

        # Concluir pedido no sistema
        produtos_ids = [item["produto"].get_id() for item in carrinho.values()]  # Correção feita aqui
        self.__gerenciador.fazerCompra(cpf_cliente, produtos_ids)




    def menuConsultarEstoque(self) -> None:
        """Exibe os produtos cadastrados no estoque em formato de tabela."""
        print("\n--- Consultar Estoque ---")

        produtos = self.__gerenciador.consultarProdutos()  # Obtem a lista de produtos
        if produtos:
            # Formata a tabela
            headers = ["ID", "Nome", "Preço (R$)", "Quantidade"]
            table = [(produto.get_id(), produto.get_nome(), produto.get_preco(), produto.get_quantidade()) for produto in produtos]

            # Exibe a tabela
            print(tabulate(table, headers=headers, tablefmt="grid"))
        else:
            print("Nenhum produto cadastrado no estoque.")

    def menuProdutos(self) -> None:
        """Menu para listar os pedidos de um cliente."""
        print("\n--- Consultar Pedidos do Cliente ---")
        cpf_cliente = input("Digite o CPF do cliente: ")
        self.__gerenciador.consultarPedidos(cpf_cliente)
        
    def menuCadastrarProduto(self) -> None:
        """Exibe o menu para cadastrar um produto."""
        try:
            id = int(input("Digite o ID do produto: "))
            nome = input("Digite o nome do produto: ")
            preco = float(input("Digite o preço do produto: "))
            quantidade = int(input("Digite a quantidade do produto: "))
            
            # Chama o método do GerenciadorVendas para cadastrar o produto
            self.__gerenciador.cadastrarProduto(id, nome, preco, quantidade)
        except ValueError:
            print("Erro: Entrada inválida. Por favor, insira os dados corretamente.")
