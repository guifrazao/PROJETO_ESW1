class Vendedor:
    def __init__(self, codigo: int, senha: str) -> None:
        """
        Inicializa os atributos da classe Vendedor.
        :param codigo: Código numérico identificador do vendedor.
        :param senha: Senha do vendedor.
        """
        self.__codigo = codigo
        self.__senha = senha

    # Getters
    def get_codigo(self) -> int:
        return self.__codigo

    def get_senha(self) -> str:
        return self.__senha

    # Setters
    def set_codigo(self, codigo: int) -> None:
        self.__codigo = codigo

    def set_senha(self, senha: str) -> None:
        self.__senha = senha

    # Método estático para verificar os dados do vendedor
    @staticmethod
    def verificarDados(codigo: int, senha: str) -> bool:
        """
        Verifica se os dados fornecidos são válidos:
        - Código deve ser um número positivo.
        - A senha não pode estar vazia.
        :param codigo: Código identificador do vendedor.
        :param senha: Senha do vendedor.
        :return: True se os dados forem válidos, False caso contrário.
        """
        if codigo <= 0:  # Validação do código
            print("Erro: O código do vendedor deve ser um número positivo.")
            return False
        if not senha.strip():  # Validação da senha
            print("Erro: A senha não pode estar vazia.")
            return False
        return True

    # Método __str__ para representar o vendedor como string
    def __str__(self) -> str:
        return f"Código: {self.__codigo}, Senha: {'*' * len(self.__senha)}"
