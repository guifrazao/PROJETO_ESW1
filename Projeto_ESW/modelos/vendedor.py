class Vendedor:
    def __init__(self, codigo: int, senha: str) -> None:
        """
        Inicializa os atributos da classe Vendedor.
        :param codigo: Código numérico identificador do vendedor.
        :param senha: Senha do vendedor.
        """
        self.__codigo: str = codigo
        self.__senha: str = senha

    # Métodos para obter os dados do vendedor
    def obter_codigo(self) -> str:
        """
        Retorna o código do vendedor.
        :return: Código identificador do vendedor.
        """
        return self.__codigo

    def obter_senha(self) -> str:
        """
        Retorna a senha do vendedor.
        :return: Senha do vendedor.
        """
        return self.__senha

    # Métodos para definir os dados do vendedor
    def definir_codigo(self, codigo: str) -> None:
        """
        Define um novo código para o vendedor.
        :param codigo: Novo código do vendedor.
        """
        self.__codigo = codigo

    def definir_senha(self, senha: str) -> None:
        """
        Define uma nova senha para o vendedor.
        :param senha: Nova senha do vendedor.
        """
        self.__senha = senha

    # Método estático para verificar os dados do vendedor
    @staticmethod
    def verificarDados(codigo: str, senha: str) -> bool:
        """
        Verifica se os dados fornecidos são válidos:
        - Código deve ser um número positivo.
        - A senha não pode estar vazia.
        :param codigo: Código identificador do vendedor.
        :param senha: Senha do vendedor.
        :return: True se os dados forem válidos, False caso contrário.
        """
        codigo_valido: bool = codigo > 0
        senha_valida: bool = bool(senha.strip())

        if not codigo_valido:  # Validação do código
            print("Erro: O código do vendedor deve ser um número positivo.")
            return False
        if not senha_valida:  # Validação da senha
            print("Erro: A senha não pode estar vazia.")
            return False
        return True

    # Método __str__ para representar o vendedor como string
    def __str__(self) -> str:
        """
        Retorna uma representação formatada do vendedor.
        :return: Representação do vendedor com código e senha mascarada.
        """
        return f"Código: {self.__codigo}, Senha: {'*' * len(self.__senha)}"
