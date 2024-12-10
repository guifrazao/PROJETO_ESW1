import re

class Cliente:
    def __init__(self, nome: str, cpf: str, telefone: str) -> None:
        """Inicializa os atributos da classe Cliente."""
        self.__nome = nome
        self.__cpf = cpf
        self.__telefone = telefone

    # Getters
    def get_nome(self) -> str:
        return self.__nome

    def get_cpf(self) -> str:
        return self.__cpf

    def get_telefone(self) -> str:
        return self.__telefone

    # Setters
    def set_nome(self, nome: str) -> None:
        self.__nome = nome

    def set_cpf(self, cpf: str) -> None:
        self.__cpf = cpf

    def set_telefone(self, telefone: str) -> None:
        self.__telefone = telefone

    # Método estático para verificar os dados do cliente
    @staticmethod
    def verificarDados(nome: str, cpf: str, telefone: str) -> bool:
        """
        Verifica se os dados fornecidos são válidos:
        - Nome não pode ser vazio.
        - CPF deve ter 11 dígitos numéricos.
        - Telefone deve seguir o padrão (XX) XXXXX-XXXX.
        """
        if not nome.strip():  # Verifica se o nome não é vazio
            print("Erro: O nome do cliente não pode estar vazio.")
            return False

        # Validação do CPF: deve conter exatamente 11 dígitos numéricos
        if not re.fullmatch(r'\d{11}', cpf):
            print("Erro: O CPF deve conter exatamente 11 dígitos numéricos.")
            return False

        # Validação do telefone: formato (XX) XXXXX-XXXX ou (XX) XXXX-XXXX
        if not re.fullmatch(r'\(\d{2}\) \d{4,5}-\d{4}', telefone):
            print("Erro: O telefone deve estar no formato (XX) XXXXX-XXXX.")
            return False

        return True