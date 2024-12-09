class Produto:
    def __init__(self, nome: str, preco: float, quantidade: int, quantidade_minima: int = 10):
        self.__nome = nome
        self.__preco = preco
        self.__quantidade = quantidade
        self.__quantidade_minima = quantidade_minima

    def get_nome(self) -> str:
        return self.__nome

    def get_preco(self) -> float:
        return self.__preco

    def get_quantidade(self) -> int:
        return self.__quantidade

    def set_quantidade(self, quantidade: int) -> None:
        self.__quantidade = quantidade

    def precisa_reposicao(self) -> bool:
        return self.__quantidade < self.__quantidade_minima
