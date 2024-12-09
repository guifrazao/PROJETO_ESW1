class CaixaController:
    def __init__(self):
        self.__saldo = 0.0

    def registrar_venda(self, valor: float) -> None:
        self.__saldo += valor

    def fechar_caixa(self) -> float:
        total = self.__saldo
        self.__saldo = 0
        return total
