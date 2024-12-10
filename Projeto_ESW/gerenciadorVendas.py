from typing import List, Optional
from banco.bancodedados import BancoDeDados
from models.vendedor import Vendedor
from models.cliente import Cliente
from models.pedido import Pedido

class GerenciadorVendas:
    def __init__(self, banco: BancoDeDados) -> None:
        """Inicializa o Gerenciador de Vendas com uma instância do BancoDeDados."""
        self.__banco = banco  # Estabelece a dependência com BancoDeDados
        self.__login = False  # Indica se o vendedor está logado ou não

    def abrirCaixa(self, codigo: int, senha: str) -> bool:
        """
        Realiza o login do vendedor e abre o caixa se as credenciais forem válidas.
        :param codigo: Código do vendedor.
        :param senha: Senha do vendedor.
        :return: True se o login for bem-sucedido, False caso contrário.
        """
        if self.__banco.autenticarVendedor(codigo, senha):  # Chama o método do BancoDeDados
            self.__login = True
            print("Caixa aberto com sucesso!")
            return True
        else:
            print("Erro: Código ou senha inválidos.")
            return False

    def cadastrarProduto(self, id: int, nome: str, preco: float, quantidade: int) -> None:
        """
        Cadastra um novo produto no banco de dados.
        :param id: ID do produto.
        :param nome: Nome do produto.
        :param preco: Preço do produto.
        :param quantidade: Quantidade inicial do produto.
        """
        if self.__banco.adicionarProduto(id, nome, preco, quantidade):
            print(f"Produto {nome} cadastrado com sucesso.")
            

    def buscarProduto(self, produto_id: int):
        """
        Busca um produto pelo ID.
        :param produto_id: ID do produto a ser buscado.
        :return: O produto se encontrado, ou None caso contrário.
        """
        # Utilizando o método consultarProdutos do BancoDeDados para obter todos os produtos
        produtos = self.__banco.consultarProdutos()
        produto = produtos.get(produto_id)  # Busca o produto pelo ID no dicionário
        return produto


    def cadastrarCliente(self, nome: str, cpf: str, telefone: str) -> None:
        """
        Cadastra um novo cliente no banco de dados.
        :param nome: Nome do cliente.
        :param cpf: CPF do cliente.
        :param telefone: Telefone do cliente.
        """
        if Cliente.verificarDados(nome, cpf, telefone):
            self.__banco.adicionarCliente(nome, cpf, telefone)

    def fazerCompra(self, cpf_cliente: str, produtos_ids: List[int]) -> None:
        """
        Realiza uma compra, criando um pedido associado a um cliente.
        :param cpf_cliente: CPF do cliente que está realizando a compra.
        :param produtos_ids: Lista de IDs de produtos a serem comprados.
        """
        cliente = self.__banco.buscarCliente(cpf_cliente)
        if not cliente:
            print(f"Erro: Cliente com CPF {cpf_cliente} não encontrado.")
            return

        pedido = Pedido(cpf_cliente)
        for produto_id in produtos_ids:
            produto = self.__banco.buscarProduto(produto_id)
            if produto:
                pedido.adicionarAoPedido(produto)
            else:
                print(f"Erro: Produto com ID {produto_id} não encontrado.")
        
        total = pedido.get_total()
        self.__banco.adicionarPedido(cliente["nome"], cpf_cliente, pedido.__dict__["_Pedido__lista_produtos"], total)
        print(f"Compra realizada com sucesso! Total: R$ {total:.2f}")

    def consultarProdutos(self) -> list:
        """Retorna todos os produtos cadastrados no banco de dados."""
        return list(self.__banco.consultarProdutos().values())


    def __login(self, codigo: int, senha: str) -> bool:
        """
        Realiza o login do vendedor.
        :param codigo: Código do vendedor.
        :param senha: Senha do vendedor.
        :return: True se o login for bem-sucedido, False caso contrário.
        """
        if Vendedor.verificarDados(codigo, senha):
            self.__vendedor_logado = Vendedor(codigo, senha)
            print(f"Login realizado com sucesso para o vendedor com código {codigo}.")
            return True
        print("Erro: Login inválido.")
        return False
