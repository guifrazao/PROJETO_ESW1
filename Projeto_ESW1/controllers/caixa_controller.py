class CaixaController:
    def __init__(self):
        self.__total_vendas = 0.0

    def registrar_venda(self, valor: float) -> None:
        self.__total_vendas += valor

    def fechar_caixa(self) -> float:
        total = self.__total_vendas
        self.__total_vendas = 0.0
        return total
