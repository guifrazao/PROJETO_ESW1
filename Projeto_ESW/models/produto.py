class Produto:
    def __init__(self, id: int, nome: str, preco: float, quantidade: int) -> None:
        """Inicializa os atributos da classe Produto."""
        self.__id = id
        self.__nome = nome
        self.__preco = preco
        self.__quantidade = quantidade

    # Getters
    def get_id(self) -> int:
        return self.__id

    def get_nome(self) -> str:
        return self.__nome

    def get_preco(self) -> float:
        return self.__preco

    def get_quantidade(self) -> int:
        return self.__quantidade

    # Setters
    def set_nome(self, nome: str) -> None:
        self.__nome = nome

    def set_preco(self, preco: float) -> None:
        self.__preco = preco

    def set_quantidade(self, quantidade: int) -> None:
        self.__quantidade = quantidade

    # Método para verificar os dados do produto
    @staticmethod
    def verificarDados(nome: str, preco: float, quantidade: int) -> bool:
        """
        Verifica se os dados fornecidos são válidos:
        - Nome não pode ser vazio
        - Preço deve ser maior que zero
        - Quantidade deve ser maior ou igual a zero
        """
        if not nome.strip():  # Verifica se o nome não é vazio
            print("Erro: O nome do produto não pode estar vazio.")
            return False
        if preco <= 0:  # Verifica se o preço é válido
            print("Erro: O preço do produto deve ser maior que zero.")
            return False
        if quantidade < 0:  # Verifica se a quantidade é válida
            print("Erro: A quantidade do produto não pode ser negativa.")
            return False
        return True