from gerenciadorVendas import GerenciadorVendas
from interface import Interface
from banco.bancodedados import BancoDeDados
from modelos.vendedor import Vendedor

def main() -> None:
    print("Bem-vindo ao Sistema de Gerenciamento de Vendas!")

    # Credenciais de administrador
    codigo_admin: str = "admin"
    senha_admin: str = "admin123"

    # Criando vendedores diretamente
    vendedor1: Vendedor = Vendedor("101", "senha101")

    # Instância do GerenciadorVendas
    gerenciador: GerenciadorVendas = GerenciadorVendas(codigo_admin, senha_admin, [vendedor1])

    # Instância da interface
    interface: Interface = Interface()

    # Configuração inicial do banco de dados
    BancoDeDados.adicionarCliente(nome="Gustavo", cpf="12345678910", telefone="(12) 12345-1234")

    produtos: list[dict[str, int | str | float]] = [
        {"id": 1, "nome": "Edredom King Size", "preco": 199.99, "quantidade": 50},
        {"id": 2, "nome": "Cobertor Casal", "preco": 129.90, "quantidade": 30},
        {"id": 3, "nome": "Boneca de Pano", "preco": 49.90, "quantidade": 100},
        {"id": 4, "nome": "Edredom Solteiro", "preco": 159.90, "quantidade": 40},
        {"id": 5, "nome": "Cobertor Infantil", "preco": 89.90, "quantidade": 60}
    ]

    for produto in produtos:
        BancoDeDados.adicionarProduto(produto['id'], produto['nome'], produto['preco'], produto['quantidade'])

    BancoDeDados.removerProduto(id=1)

    while True:
        if interface.menuAbrirCaixa(gerenciador, codigo_admin, senha_admin):
            break
        else:
            print("Login inválido. Tente novamente.")

    # Menu principal
    while True:
        print("\n--- Menu Principal ---")
        print("1. Cadastrar Cliente")
        print("2. Cadastrar Produto")
        print("3. Editar Produto")
        print("4. Consultar Estoque")
        print("5. Fazer Compra")
        print("6. Fechar Caixa e Sair")
        
        opcao: str = input("Escolha uma opção: ")  # Tipagem de `opcao` adicionada

        if opcao == "1":
            interface.menuCadastrarCliente(gerenciador)
        elif opcao == "2":
            interface.menuCadastrarProduto(gerenciador)
        elif opcao == "3":
            interface.menuEditarProduto(gerenciador)
        elif opcao == "4":
            interface.menuConsultarEstoque(gerenciador)
        elif opcao == "5":
            interface.menuFazerCompra(gerenciador)
        elif opcao == "6":
            interface.menuFecharCaixa()
            print("Encerrando o sistema. Até mais!")
            break
        else:
            print("Opção inválida. Escolha novamente.")

if __name__ == "__main__":
    main()
