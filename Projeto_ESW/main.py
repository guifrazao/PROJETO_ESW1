from banco.bancodedados import BancoDeDados
from gerenciadorVendas import GerenciadorVendas
from interface import Interface


def main() -> None:
    print("Bem-vindo ao Sistema de Gerenciamento de Vendas!")

    # Instancia o BancoDeDados e o GerenciadorVendas
    banco = BancoDeDados()

    # Cadastra vendedores (podemos adicionar mais vendedores se necessário)
    banco.adicionarVendedor(codigo=123, senha="senha123")
    banco.adicionarVendedor(codigo=456, senha="senha456")

    gerenciador = GerenciadorVendas(banco)
    interface = Interface(gerenciador)
    
    banco.adicionarCliente(nome="Gustavo",cpf="12345678910", telefone="(12) 12345-1234")

    # Adiciona produtos no estoque para testar
    banco.adicionarProduto(id=1, nome="Edredom King Size", preco=199.99, quantidade=50)
    banco.adicionarProduto(id=2, nome="Cobertor Casal", preco=129.90, quantidade=30)
    banco.adicionarProduto(id=3, nome="Boneca de Pano", preco=49.90, quantidade=100)
    banco.adicionarProduto(id=4, nome="Edredom Solteiro", preco=159.90, quantidade=40)
    banco.adicionarProduto(id=5, nome="Cobertor Infantil", preco=89.90, quantidade=60)

    # Exigir login antes de acessar o menu principal
    while True:
        print("\n--- Login do Vendedor ---")
        codigo = int(input("Digite o código do vendedor: "))
        senha = input("Digite a senha do vendedor: ")

        if gerenciador.abrirCaixa(codigo, senha):
            print("Login bem-sucedido! Caixa aberto.")
            break
        else:
            print("Erro: Código ou senha inválidos. Tente novamente.")

    # Menu principal após o login
    while True:
        print("\n--- Menu Principal ---")
        print("1. Cadastrar Cliente")
        print("2. Cadastrar Produto")
        print("3. Checar Estoque") 
        print("4. Fazer Compra")
        print("5. Fechar Caixa e Sair")
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            interface.menuCadastrarCliente()
        elif opcao == "2":
            interface.menuCadastrarProduto()
        elif opcao == "3":
            interface.menuConsultarEstoque()
        elif opcao == "4":
            interface.menuFazerCompra()
        elif opcao == "5":
            interface.menuFecharCaixa()
            print("Encerrando o sistema. Até mais!")
            break
        else:
            print("Opção inválida. Por favor, escolha novamente.")

if __name__ == "__main__":
    main()

