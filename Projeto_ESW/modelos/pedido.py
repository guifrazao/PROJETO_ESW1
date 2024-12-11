from modelos.produto import Produto  # Importa a classe Produto

class Pedido:
    def __init__(self, cpf_cliente: str) -> None:
        """
        Inicializa os atributos da classe Pedido.
        :param cpf_cliente: CPF do cliente que realizou o pedido.
        """
        self.__cpf_cliente: str = cpf_cliente
        self.__lista_produtos: list[Produto] = []  # Lista de produtos agregados ao pedido
        self.__total: float = 0.0  # Total do pedido inicializado como 0.0

    # Método para adicionar um produto ao pedido
    def adicionarAoPedido(self, produto: Produto) -> None:
        """
        Adiciona um produto à lista de produtos no pedido e atualiza o total.
        :param produto: Objeto Produto a ser adicionado.
        """
        preco_produto: float = produto.obter_preco()
        self.__lista_produtos.append(produto)
        self.__total += preco_produto
        print(f"Produto '{produto.obter_nome()}' adicionado ao pedido.")

    # Método para obter a quantidade de produtos no pedido
    def obterQuantidadeProdutos(self) -> int:
        """
        Retorna a quantidade total de produtos no pedido.
        :return: Quantidade total de produtos.
        """
        quantidade: int = len(self.__lista_produtos)
        return quantidade

    # Método para obter o código (ID) de um produto específico
    def obterCodigoProduto(self, indice: int) -> int:
        """
        Retorna o código (ID) do produto na lista, dado seu índice.
        :param indice: Índice do produto na lista.
        :return: ID do produto ou -1 se o índice for inválido.
        """
        if 0 <= indice < len(self.__lista_produtos):
            id_produto: int = self.__lista_produtos[indice].obter_id()
            return id_produto
        else:
            print("Erro: Índice fora da faixa válida.")
            return -1  # Retorna -1 em caso de índice inválido

    # Método para calcular o total do pedido
    def obter_total(self) -> float:
        """
        Retorna o total do pedido.
        :return: Total do pedido em reais.
        """
        return self.__total

    # Método __str__ para representar o pedido
    def __str__(self) -> str:
        """
        Representação em string do pedido, listando o CPF do cliente, os produtos e o total.
        :return: String formatada com os detalhes do pedido.
        """
        produtos_str: str = "\n".join(
            [f"- {produto.obter_nome()} (R$ {produto.obter_preco():.2f})" for produto in self.__lista_produtos]
        )
        return f"CPF do Cliente: {self.__cpf_cliente}\nProdutos:\n{produtos_str}\nTotal: R$ {self.__total:.2f}"
