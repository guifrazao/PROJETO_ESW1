class Produto:
    def __init__(self, id: int, nome: str, preco: float, quantidade: int) -> None:
        """Inicializa os atributos da classe Produto."""
        self.__id: int = id
        self.__nome: str = nome
        self.__preco: float = preco
        self.__quantidade: int = quantidade

    # Métodos para obter os dados do produto
    def obter_id(self) -> int:
        """
        Retorna o ID do produto.
        :return: ID do produto.
        """
        return self.__id

    def obter_nome(self) -> str:
        """
        Retorna o nome do produto.
        :return: Nome do produto.
        """
        return self.__nome

    def obter_preco(self) -> float:
        """
        Retorna o preço do produto.
        :return: Preço do produto.
        """
        return self.__preco

    def obter_quantidade(self) -> int:
        """
        Retorna a quantidade do produto.
        :return: Quantidade do produto.
        """
        return self.__quantidade

    # Métodos para definir os dados do produto
    def definir_nome(self, nome: str) -> None:
        """
        Define um novo nome para o produto.
        :param nome: Novo nome do produto.
        """
        self.__nome = nome

    def definir_preco(self, preco: float) -> None:
        """
        Define um novo preço para o produto.
        :param preco: Novo preço do produto.
        """
        self.__preco = preco

    def definir_quantidade(self, quantidade: int) -> None:
        """
        Define uma nova quantidade para o produto.
        :param quantidade: Nova quantidade do produto.
        """
        self.__quantidade = quantidade

    # Método para verificar os dados do produto
    @staticmethod
    def verificarDados(nome: str, preco: float, quantidade: int) -> bool:
        """
        Verifica se os dados fornecidos são válidos:
        - Nome não pode ser vazio
        - Preço deve ser maior que zero
        - Quantidade deve ser maior ou igual a zero
        :param nome: Nome do produto.
        :param preco: Preço do produto.
        :param quantidade: Quantidade do produto.
        :return: True se os dados são válidos, False caso contrário.
        """
        nome_valido: bool = bool(nome.strip())
        preco_valido: bool = preco > 0
        quantidade_valida: bool = quantidade >= 0

        if not nome_valido:  # Verifica se o nome não é vazio
            print("Erro: O nome do produto não pode estar vazio.")
            return False
        if not preco_valido:  # Verifica se o preço é válido
            print("Erro: O preço do produto deve ser maior que zero.")
            return False
        if not quantidade_valida:  # Verifica se a quantidade é válida
            print("Erro: A quantidade do produto não pode ser negativa.")
            return False

        return True
