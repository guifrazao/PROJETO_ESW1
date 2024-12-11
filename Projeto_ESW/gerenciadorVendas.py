from typing import List, Optional, Dict
from banco.bancodedados import BancoDeDados
from modelos.cliente import Cliente
from modelos.pedido import Pedido

class GerenciadorVendas:
    def __init__(self, codigo_admin: str, senha_admin: str, vendedores: List[object]) -> None:
        """
        Inicializa o Gerenciador de Vendas com um administrador e uma lista de vendedores.
        """
        self.__codigo_admin: str = codigo_admin
        self.__senha_admin: str = senha_admin
        self.__vendedores: List[object] = vendedores  # Lista de objetos vendedores
        self.__login: bool = False  # Indica se o vendedor está logado ou não

    def abrirCaixa(self, codigo: int, senha: str) -> bool:
        """
        Realiza o login e abre o caixa se as credenciais forem válidas.
        """
        # Verifica se é o administrador
        if codigo == self.__codigo_admin and senha == self.__senha_admin:
            self.__login = True
            return True

        # Verifica se o vendedor existe na lista e se a senha está correta
        for vendedor in self.__vendedores:
            vendedor_codigo: int = vendedor.obter_codigo()
            vendedor_senha: str = vendedor.obter_senha()
            if vendedor_codigo == codigo and vendedor_senha == senha:
                self.__login = True
                return True

        return False

    def cadastrarProduto(self, id: int, nome: str, preco: float, quantidade: int) -> None:
        """
        Cadastra um novo produto no banco de dados.
        """
        sucesso: bool = BancoDeDados.adicionarProduto(id, nome, preco, quantidade)
        if sucesso:
            print(f"")
        else:
            print("Erro ao cadastrar produto.")

    def buscarProduto(self, produto_id: int) -> Optional[object]:
        """
        Busca um produto pelo ID.
        """
        produto: Optional[object] = BancoDeDados.buscarProduto(produto_id)
        return produto

    def editarProduto(self, id: int, nome: Optional[str] = None, preco: Optional[float] = None, quantidade: Optional[int] = None) -> bool:
        """
        Edita um produto no banco de dados.
        """
        sucesso: bool = BancoDeDados.editarProduto(id, nome, preco, quantidade)
        return sucesso

    def cadastrarCliente(self, nome: str, cpf: str, telefone: str) -> None:
        """
        Cadastra um novo cliente.
        """
        dados_validos: bool = Cliente.verificarDados(nome, cpf, telefone)
        if dados_validos:
            BancoDeDados.adicionarCliente(nome, cpf, telefone)

    def fazerCompra(self, cpf_cliente: str, produtos_ids: List[int]) -> None:
        """
        Realiza uma compra associada a um cliente.
        """
        cliente: Optional[Dict[str, str]] = BancoDeDados.buscarCliente(cpf_cliente)
        if not cliente:
            print(f"Erro: Cliente com CPF {cpf_cliente} não encontrado.")
            return

        pedido: Pedido = Pedido(cpf_cliente)
        for produto_id in produtos_ids:
            produto: Optional[object] = BancoDeDados.buscarProduto(produto_id)
            if produto:
                pedido.adicionarAoPedido(produto)
            else:
                print(f"Erro: Produto com ID {produto_id} não encontrado.")

        total: float = pedido.obter_total()
        produtos_lista: List[Dict[str, object]] = pedido.__dict__["_Pedido__lista_produtos"]
        BancoDeDados.adicionarPedido(cliente["nome"], cpf_cliente, produtos_lista, total)

    def consultarProdutos(self) -> List[object]:
        """
        Retorna todos os produtos cadastrados.
        """
        produtos: List[object] = list(BancoDeDados.consultarProdutos().values())
        return produtos

    def buscarCliente(self, cpf: str) -> Optional[Dict[str, str]]:
        """
        Busca um cliente pelo CPF.
        """
        cliente: Optional[Dict[str, str]] = BancoDeDados.buscarCliente(cpf)
        return cliente
