import re

class Cliente:
    def __init__(self, nome: str, cpf: str, telefone: str) -> None:
        """Inicializa os atributos da classe Cliente."""
        self.__nome: str = nome
        self.__cpf: str = cpf
        self.__telefone: str = telefone

    # Métodos de acesso (Getters)
    def obter_nome(self) -> str:
        return self.__nome

    def obter_cpf(self) -> str:
        return self.__cpf

    def obter_telefone(self) -> str:
        return self.__telefone

    # Métodos de modificação (Setters)
    def alterar_nome(self, nome: str) -> None:
        self.__nome = nome

    def alterar_cpf(self, cpf: str) -> None:
        self.__cpf = cpf

    def alterar_telefone(self, telefone: str) -> None:
        self.__telefone = telefone

    # Método estático para verificar os dados do cliente
    @staticmethod
    def verificarDados(nome: str, cpf: str, telefone: str) -> bool:
        """
        Verifica se os dados fornecidos são válidos:
        - Nome não pode ser vazio.
        - CPF deve ter 11 dígitos numéricos.
        - Telefone deve seguir o padrão (XX) XXXXX-XXXX ou (XX) XXXX-XXXX.
        """
        nome_valido: bool = bool(nome.strip())  # Verifica se o nome não é vazio
        cpf_valido: bool = bool(re.fullmatch(r'\d{11}', cpf))  # CPF com 11 dígitos numéricos
        telefone_valido: bool = bool(re.fullmatch(r'\(\d{2}\) \d{4,5}-\d{4}', telefone))  # Telefone formatado
        
        # Validações com mensagens de erro
        if not nome_valido:
            print("Erro: O nome do cliente não pode estar vazio.")
            return False

        if not cpf_valido:
            print("Erro: O CPF deve conter exatamente 11 dígitos numéricos.")
            return False

        if not telefone_valido:
            print("Erro: O telefone deve estar no formato (XX) XXXXX-XXXX ou (XX) XXXX-XXXX.")
            return False

        return True
