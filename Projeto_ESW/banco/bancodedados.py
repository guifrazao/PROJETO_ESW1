from typing import List, Dict, Union, Optional
from modelos.produto import Produto


class BancoDeDados:
    __produtos: Dict[int, Produto] = {}  # Armazena produtos por ID
    __clientes: Dict[str, Dict[str, Union[str, List[Dict[str, Union[str, List, float]]]]]] = {}  # Clientes por CPF
    __pedidos: List[Dict[str, Union[str, List[Produto], float]]] = []  # Lista global de pedidos

    @staticmethod
    def adicionarProduto(id: int, nome: str, preco: float, quantidade: int) -> bool:
        """
        Adiciona um novo produto ao banco de dados.
        :param id: ID único do produto.
        :param nome: Nome do produto.
        :param preco: Preço do produto.
        :param quantidade: Quantidade em estoque.
        :return: True se bem-sucedido, False caso contrário.
        """
        if id in BancoDeDados.__produtos:
            print(f"Erro: Já existe um produto com o ID {id}.")
            return False

        if not Produto.verificarDados(nome, preco, quantidade):
            return False

        BancoDeDados.__produtos[id] = Produto(id, nome, preco, quantidade)
        print(f"Produto {nome} adicionado com sucesso!")
        return True

    @staticmethod
    def removerProduto(id: int) -> bool:
        """
        Remove um produto pelo ID.
        :param id: ID do produto a ser removido.
        :return: True se bem-sucedido, False caso contrário.
        """
        if id not in BancoDeDados.__produtos:
            print(f"Erro: Produto com ID {id} não encontrado.")
            return False

        del BancoDeDados.__produtos[id]
        print(f"Produto com ID {id} removido com sucesso.")
        return True

    @staticmethod
    def buscarProduto(id: int) -> Optional[Produto]:
        """
        Busca um produto pelo ID.
        :param id: ID do produto a ser buscado.
        :return: Produto se encontrado, None caso contrário.
        """
        return BancoDeDados.__produtos.get(id)

    @staticmethod
    def editarProduto(id: int, nome: str = "", preco: Optional[float] = None, quantidade: Optional[int] = None) -> bool:
        """
        Edita as informações de um produto pelo ID.
        :param id: ID do produto.
        :param nome: Novo nome do produto (opcional).
        :param preco: Novo preço do produto (opcional).
        :param quantidade: Nova quantidade em estoque (opcional).
        :return: True se bem-sucedido, False caso contrário.
        """
        produto: Optional[Produto] = BancoDeDados.__produtos.get(id)
        if not produto:
            print(f"Erro: Produto com ID {id} não encontrado.")
            return False

        # Atualiza os atributos do produto se forem fornecidos
        if nome:
            produto.definir_nome(nome)
        if preco is not None:
            produto.definir_preco(preco)
        if quantidade is not None:
            produto.definir_quantidade(quantidade)

        print(f"Produto com ID {id} editado com sucesso.")
        return True

    @staticmethod
    def consultarProdutos() -> Dict[int, Produto]:
        """
        Retorna todos os produtos cadastrados no banco de dados.
        :return: Dicionário de produtos (ID -> Produto).
        """
        return BancoDeDados.__produtos

    @staticmethod
    def adicionarCliente(nome: str, cpf: str, telefone: str) -> bool:
        """
        Adiciona um cliente ao banco de dados.
        :param nome: Nome do cliente.
        :param cpf: CPF do cliente.
        :param telefone: Telefone do cliente.
        :return: True se bem-sucedido, False caso contrário.
        """
        if cpf in BancoDeDados.__clientes:
            print(f"Erro: Cliente com CPF {cpf} já existe.")
            return False

        BancoDeDados.__clientes[cpf] = {"nome": nome, "telefone": telefone, "pedidos": []}
        print(f"Cliente {nome} adicionado com sucesso.")
        return True

    @staticmethod
    def buscarCliente(cpf: str) -> Optional[Dict[str, Union[str, List[Dict[str, Union[str, List, float]]]]]]:
        """
        Busca um cliente pelo CPF.
        :param cpf: CPF do cliente.
        :return: Dicionário com dados do cliente ou None caso não exista.
        """
        return BancoDeDados.__clientes.get(cpf)

    @staticmethod
    def adicionarPedido(nome_cliente: str, cpf: str, lista_produtos: List[Produto], total: float) -> bool:
        """
        Adiciona um pedido ao banco de dados associado a um cliente.
        :param nome_cliente: Nome do cliente.
        :param cpf: CPF do cliente.
        :param lista_produtos: Lista de produtos no pedido.
        :param total: Valor total do pedido.
        :return: True se bem-sucedido, False caso contrário.
        """
        cliente: Optional[Dict[str, Union[str, List[Dict[str, Union[str, List, float]]]]]] = BancoDeDados.__clientes.get(cpf)
        if not cliente:
            print(f"Erro: Cliente com CPF {cpf} não encontrado.")
            return False

        pedido: Dict[str, Union[str, List[Produto], float]] = {
            "nome_cliente": nome_cliente,
            "produtos": lista_produtos,
            "total": total,
        }
        cliente["pedidos"].append(pedido)
        BancoDeDados.__pedidos.append(pedido)
        print(f"Pedido para o cliente {nome_cliente} adicionado com sucesso.")
        return True

    @staticmethod
    def buscarPedidosCliente(cpf: str) -> Optional[List[Dict[str, Union[str, List[Produto], float]]]]:
        """
        Retorna os pedidos associados a um cliente pelo CPF.
        :param cpf: CPF do cliente.
        :return: Lista de pedidos ou None caso o cliente não exista.
        """
        cliente: Optional[Dict[str, Union[str, List[Dict[str, Union[str, List, float]]]]]] = BancoDeDados.__clientes.get(cpf)
        if not cliente:
            print(f"Erro: Cliente com CPF {cpf} não encontrado.")
            return None

        return cliente["pedidos"]
