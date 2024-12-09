from models.cliente import Cliente

class ClienteController:
    def __init__(self):
        self.__clientes = []

    def cadastrar_cliente(self, nome: str, cpf: str, contato: str, endereco: str) -> str:
        for cliente in self.__clientes:
            if cliente.get_cpf() == cpf:
                return f"Cliente com CPF '{cpf}' já cadastrado!"
        
        cliente = Cliente(nome, cpf, contato, endereco)
        self.__clientes.append(cliente)
        return f"Cliente '{nome}' cadastrado com sucesso!"
