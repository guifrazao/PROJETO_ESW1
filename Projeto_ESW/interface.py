from gerenciadorVendas import GerenciadorVendas
from tabulate import tabulate
import msvcrt  # Importa a biblioteca msvcrt para Windows
import sys
from typing import Optional, List, Dict

class Interface:
    @staticmethod
    def menuAbrirCaixa(gerenciador: "GerenciadorVendas", codigo_admin: str, senha_admin: str) -> bool:
        """Menu para abrir o caixa (realizar login do vendedor)."""
        print("\n--- Abrir Caixa ---")
        
        # Tipagem do input
        codigo: str = input("Digite o código do vendedor: ")
        senha: str = Interface._input_senha()

        # Verifica se é administrador
        if codigo == codigo_admin and senha == senha_admin:
            print("Acesso de administrador concedido.")
            return True  # Retorna True para login bem-sucedido

        # Verifica login do vendedor usando o Gerenciador
        if gerenciador.abrirCaixa(codigo, senha):
            print("Login bem-sucedido como vendedor.")
            return True  # Retorna True para login bem-sucedido
        else:
            print("Erro ao abrir o caixa. Verifique o código e a senha e tente novamente.")
            return False  # Retorna False para login falho

    @staticmethod
    def _input_senha() -> str:
        """Função para capturar a senha e mostrar * no lugar de cada caractere (apenas no Windows)."""
        senha: str = ""  # Tipagem da variável senha
        print("Digite a senha do vendedor: ", end='', flush=True)
        while True:
            tecla: bytes = msvcrt.getch()
            if tecla == b'\r':  # Caractere de Enter
                print()  # Move para a próxima linha
                break
            elif tecla == b'\x08':  # Caractere de backspace
                if len(senha) > 0:
                    senha = senha[:-1]
                    sys.stdout.write('\b \b')  # Apaga o último caractere na tela
                    sys.stdout.flush()
            else:
                senha += tecla.decode('utf-8')
                sys.stdout.write('*')
                sys.stdout.flush()
        return senha

    @staticmethod
    def menuCadastrarCliente(gerenciador: "GerenciadorVendas") -> None:
        """Menu para cadastrar um novo cliente."""
        print("\n--- Cadastrar Cliente ---")
        
        # Tipagem das entradas
        nome: str = input("Digite o nome do cliente: ")
        cpf: str = input("Digite o CPF do cliente (somente números): ")
        telefone: str = input("Digite o telefone do cliente (formato: (XX) XXXXX-XXXX): ")

        gerenciador.cadastrarCliente(nome, cpf, telefone)

    @staticmethod
    def menuCadastrarProduto(gerenciador: "GerenciadorVendas") -> None:
        """Exibe o menu para cadastrar um produto."""
        try:
            # Tipagem das entradas
            id: int = int(input("Digite o ID do produto: "))
            nome: str = input("Digite o nome do produto: ")
            preco: float = float(input("Digite o preço do produto: "))
            quantidade: int = int(input("Digite a quantidade do produto: "))

            # Chama o método do GerenciadorVendas para cadastrar o produto
            gerenciador.cadastrarProduto(id, nome, preco, quantidade)
        except ValueError:
            print("Erro: Entrada inválida. Por favor, insira os dados corretamente.")

    @staticmethod
    def menuEditarProduto(gerenciador: "GerenciadorVendas") -> None:
        """Menu para editar um produto existente."""
        print("\n--- Editar Produto ---")
        try:
            # Tipagem da entrada do ID
            id_produto: int = int(input("Digite o ID do produto que deseja editar: "))
            produto: Optional["Produto"] = gerenciador.buscarProduto(id_produto)

            if produto is None:
                print("Produto não encontrado.")
                return

            # Tipagem das entradas opcionais
            nome: str = input(f"Nome atual: {produto.obter_nome()}. Novo nome (deixe em branco para manter): ")
            preco_input: str = input(f"Preço atual: R$ {produto.obter_preco():.2f}. Novo preço (deixe em branco para manter): ")
            quantidade_input: str = input(f"Quantidade atual: {produto.obter_quantidade()}. Nova quantidade (deixe em branco para manter): ")

            # Converte os campos de preço e quantidade para float/int se não estiverem vazios
            preco: Optional[float] = float(preco_input) if preco_input else None
            quantidade: Optional[int] = int(quantidade_input) if quantidade_input else None

            if gerenciador.editarProduto(id_produto, nome if nome else None, preco, quantidade):
                print("Produto editado com sucesso.")
            else:
                print("Erro ao editar o produto.")
        except ValueError:
            print("Erro: ID, preço ou quantidade inválidos.")


    @staticmethod
    def menuFazerCompra(gerenciador: GerenciadorVendas) -> None:
        """Menu para realizar uma compra."""
        print("\n--- Fazer Compra ---")
        
        while True:
            cpf_cliente: str = input("Digite o CPF do cliente: ")
            cliente: Optional[dict] = gerenciador.buscarCliente(cpf_cliente)
            if not cliente:
                print("Cliente não encontrado.")
                opcao: str = input("Deseja tentar novamente (1) ou cadastrar um novo cliente (2)? ").strip()
                if opcao == "1":
                    continue
                elif opcao == "2":
                    Interface.menuCadastrarCliente(gerenciador)
                    continue
                else:
                    print("Opção inválida. Tente novamente.")
                    continue

            # Listar os produtos disponíveis
            produtos: List[object] = gerenciador.consultarProdutos()
            if not produtos:
                print("Nenhum produto disponível no estoque.")
                return

            headers: List[str] = ["ID", "Nome", "Preço (R$)", "Quantidade"]
            tabela_produtos: List[List] = [
                [produto.obter_id(), produto.obter_nome(), produto.obter_preco(), produto.obter_quantidade()]
                for produto in produtos
            ]
            print("Lista de produtos disponíveis para compra:")
            print(tabulate(tabela_produtos, headers=headers, tablefmt="fancy_grid"))

            # Processo de compra
            carrinho: Dict[int, Dict[str, object | int]] = {}
            while True:
                try:
                    produto_id: int = int(input("Digite o número do produto que deseja comprar (ou -1 para finalizar a compra): "))
                    if produto_id == -1:
                        break

                    produto: Optional[object] = gerenciador.buscarProduto(produto_id)
                    if not produto:
                        print("Produto não encontrado. Tente novamente.")
                        continue

                    quantidade: int = int(input(f"Quantas unidades de {produto.obter_nome()} deseja comprar? "))
                    if quantidade > produto.obter_quantidade():
                        print(f"Quantidade indisponível! Estoque atual: {produto.obter_quantidade()}.")
                        continue

                    if produto_id in carrinho:
                        carrinho[produto_id]["quantidade"] += quantidade
                    else:
                        carrinho[produto_id] = {"produto": produto, "quantidade": quantidade}

                    produto.definir_quantidade(produto.obter_quantidade() - quantidade)
                    print(f"Adicionado {quantidade} unidade(s) de {produto.obter_nome()} ao carrinho.")
                except ValueError:
                    print("Entrada inválida. Por favor, digite um número válido.")

            # Finalizar compra
            if not carrinho:
                print("Nenhum produto foi adicionado ao carrinho. Compra cancelada.")
                return

            total: float = 0.0
            resumo: List[List] = []
            for item in carrinho.values():
                produto: object = item["produto"]
                quantidade: int = item["quantidade"]
                subtotal: float = produto.obter_preco() * quantidade
                total += subtotal
                resumo.append([produto.obter_nome(), quantidade, f"R$ {subtotal:.2f}"])

            headers_resumo: List[str] = ["Produto", "Quantidade", "Subtotal"]
            print(tabulate(resumo, headers=headers_resumo, tablefmt="fancy_grid"))
            print(f"Total: R$ {total:.2f}")

            # Seleção de método de pagamento
            while True:
                metodo_pagamento: str = input("Informe o método de pagamento (1 - Dinheiro, 2 - Cartão): ")
                if metodo_pagamento == "1":
                    # Pagamento em dinheiro
                    while True:
                        try:
                            valor_entregue: float = float(input(f"Digite o valor entregue pelo cliente (R$): "))
                            if valor_entregue < total:
                                print(f"Valor insuficiente! O total é R$ {total:.2f}. Tente novamente.")
                            else:
                                troco: float = valor_entregue - total
                                print("Pagamento realizado com sucesso via Dinheiro!")
                                print(f"Troco: R$ {troco:.2f}")
                                break
                        except ValueError:
                            print("Entrada inválida. Por favor, digite um valor numérico válido.")
                    break

                elif metodo_pagamento == "2":
                    print("Pagamento realizado com sucesso via Cartão!")
                    break
                else:
                    print("Método inválido. Escolha 1 para Dinheiro ou 2 para Cartão.")

            # Concluir pedido no sistema
            produtos_ids: List[int] = [item["produto"].obter_id() for item in carrinho.values()]
            gerenciador.fazerCompra(cpf_cliente, produtos_ids)
        
            print("Compra concluída com sucesso!")
            return

    @staticmethod
    def menuConsultarEstoque(gerenciador: GerenciadorVendas) -> None:
        """Exibe os produtos cadastrados no estoque em formato de tabela com opção de busca por ID."""
        print("\n--- Consultar Estoque ---")

        produtos: List[object] = gerenciador.consultarProdutos()
        if produtos:
            headers: List[str] = ["ID", "Nome", "Preço (R$)", "Quantidade"]
            table: List[List] = [
                [produto.obter_id(), produto.obter_nome(), produto.obter_preco(), produto.obter_quantidade()]
                for produto in produtos
            ]
            print("Produtos no estoque:")
            print(tabulate(table, headers=headers, tablefmt="fancy_grid"))

            busca_id: str = input("\nDeseja buscar um produto por ID? (s/n): ").strip().lower()
            if busca_id == 's':
                try:
                    id_produto: int = int(input("Digite o ID do produto para busca: "))
                    produto: Optional[object] = next((p for p in produtos if p.obter_id() == id_produto), None)

                    if produto:
                        print("\nProduto encontrado:")
                        print(tabulate(
                            [[produto.obter_id(), produto.obter_nome(), produto.obter_preco(), produto.obter_quantidade()]],
                            headers=headers, tablefmt="fancy_grid"
                        ))
                    else:
                        print(f"Produto com ID {id_produto} não encontrado.")
                except ValueError:
                    print("ID inválido. Por favor, digite um número válido.")
        else:
            print("Nenhum produto cadastrado no estoque.")

    @staticmethod
    def menuFecharCaixa() -> None:
        """Menu para fechar o caixa."""
        print("\n--- Fechar Caixa ---")
        print("Caixa fechado. Até logo!")
