class Cliente:
    def __init__(self, nome: str, cpf: str, contato: str, endereco: str):
        self.__nome = nome
        self.__cpf = cpf
        self.__contato = contato
        self.__endereco = endereco

    def get_nome(self) -> str:
        return self.__nome

    def get_cpf(self) -> str:
        return self.__cpf

    def get_contato(self) -> str:
        return self.__contato
