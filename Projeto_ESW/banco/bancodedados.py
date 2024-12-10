from typing import List, Dict, Union
from models.produto import Produto
from models.vendedor import Vendedor

class BancoDeDados:
    def __init__(self) -> None:
        """Inicializa o banco de dados com estruturas para armazenar produtos, clientes e pedidos."""
        self.__produtos: Dict[int, Produto] = {}  # Armazena produtos por ID
        self.__clientes: Dict[str, Dict[str, Union[str, List[Dict]]]] = {}  # Clientes por CPF
        self.__pedidos: List[Dict[str, Union[str, List[Produto], float]]] = []
        self.__vendedores: List[Vendedor] = []# Lista de pedidos

    def adicionarProduto(self, id: int, nome: str, preco: float, quantidade: int) -> bool:
        """
        Adiciona um novo produto ao banco de dados.
        Retorna True se a operação for bem-sucedida, caso contrário, False.
        """
        if id in self.__produtos:
            print(f"Erro: Já existe um produto com o ID {id}.")
            return False
        
        if not Produto.verificarDados(nome, preco, quantidade):
            return False

        self.__produtos[id] = Produto(id, nome, preco, quantidade)
        print(f"Produto {nome} adicionado com sucesso!")
        return True

    def removerProduto(self, id: int) -> bool:
        """Remove um produto pelo ID. Retorna True se bem-sucedido, False caso contrário."""
        if id not in self.__produtos:
            print(f"Erro: Produto com ID {id} não encontrado.")
            return False
        
        del self.__produtos[id]
        print(f"Produto com ID {id} removido com sucesso.")
        return True

    def buscarProduto(self, id: int) -> Union[Produto, None]:
        """Busca um produto pelo ID. Retorna o Produto se encontrado, ou None caso contrário."""
        return self.__produtos.get(id)

    def editarProduto(self, id: int, nome: str = "", preco: float = None, quantidade: int = None) -> bool:
        """
        Edita as informações de um produto pelo ID.
        Permite alterar nome, preço e/ou quantidade.
        Retorna True se bem-sucedido, False caso contrário.
        """
        produto = self.__produtos.get(id)
        if not produto:
            print(f"Erro: Produto com ID {id} não encontrado.")
            return False
        
    def consultarProdutos(self) -> Dict[int, Produto]:
        """Retorna todos os produtos cadastrados no banco de dados."""
        return self.__produtos

        if nome:
            produto.set_nome(nome)
        if preco is not None:
            produto.set_preco(preco)
        if quantidade is not None:
            produto.set_quantidade(quantidade)

        print(f"Produto com ID {id} atualizado com sucesso.")
        return True

    def adicionarCliente(self, nome: str, cpf: str, telefone: str) -> bool:
        """
        Adiciona um cliente ao banco de dados.
        Retorna True se bem-sucedido, False caso contrário.
        """
        if cpf in self.__clientes:
            print(f"Erro: Cliente com CPF {cpf} já existe.")
            return False
        
        self.__clientes[cpf] = {"nome": nome, "telefone": telefone, "pedidos": []}
        print(f"Cliente {nome} adicionado com sucesso.")
        return True

    def buscarCliente(self, cpf: str) -> Union[Dict[str, Union[str, List]], None]:
        """Busca um cliente pelo CPF. Retorna o cliente se encontrado, ou None caso contrário."""
        return self.__clientes.get(cpf)

    def adicionarPedido(self, nome_cliente: str, cpf: str, lista_produtos: List[Produto], total: float) -> bool:
        """
        Adiciona um pedido ao banco de dados associado a um cliente.
        Retorna True se bem-sucedido, False caso contrário.
        """
        cliente = self.__clientes.get(cpf)
        if not cliente:
            print(f"Erro: Cliente com CPF {cpf} não encontrado.")
            return False
        
        pedido = {"nome_cliente": nome_cliente, "produtos": lista_produtos, "total": total}
        cliente["pedidos"].append(pedido)
        self.__pedidos.append(pedido)
        print(f"Pedido para o cliente {nome_cliente} adicionado com sucesso.")
        return True

    def buscarPedidosCliente(self, cpf: str) -> Union[List[Dict[str, Union[str, List, float]]], None]:
        """Retorna os pedidos associados a um cliente pelo CPF."""
        cliente = self.__clientes.get(cpf)
        if not cliente:
            print(f"Erro: Cliente com CPF {cpf} não encontrado.")
            return None
        
        return cliente["pedidos"]
    
    def adicionarVendedor(self, codigo: int, senha: str) -> None:
        """
        Adiciona um vendedor ao banco de dados.
        :param codigo: Código identificador do vendedor.
        :param senha: Senha do vendedor.
        """
        from models.vendedor import Vendedor
        vendedor = Vendedor(codigo, senha)
        self.__vendedores.append(vendedor)

    def autenticarVendedor(self, codigo: int, senha: str) -> bool:
        """
        Autentica o vendedor pelo código e senha.
        :param codigo: Código do vendedor.
        :param senha: Senha do vendedor.
        :return: True se a autenticação for bem-sucedida, False caso contrário.
        """
        for vendedor in self.__vendedores:
            if vendedor.get_codigo() == codigo and vendedor.get_senha() == senha:
                return True
        return False
