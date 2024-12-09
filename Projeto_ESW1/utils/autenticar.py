import bcrypt
import msvcrt  # Usado para capturar a entrada no Windows
import sys

# Senhas hash pré-cadastradas
USUARIOS = {
    "admin": bcrypt.hashpw("admin123".encode(), bcrypt.gensalt()),
    "caixa": bcrypt.hashpw("caixa123".encode(), bcrypt.gensalt())
}

def entrada_senha():
    """Função para exibir a senha como '***' enquanto digita"""
    senha = ""
    sys.stdout.write("Senha: ")  # Exibe "Senha:" antes de digitar
    sys.stdout.flush()

    while True:
        tecla = msvcrt.getch()  # Lê um caractere da entrada
        if tecla == b'\r' or tecla == b'\n':  # Se pressionar Enter, termina
            break
        if tecla == b'\x08':  # Se pressionar Backspace
            senha = senha[:-1]
            sys.stdout.write("\b \b")  # Remove o último asterisco
        else:
            senha += tecla.decode("utf-8")
            sys.stdout.write("*")  # Exibe o asterisco
        sys.stdout.flush()
    print()  # Pula a linha após digitar a senha
    return senha

# Função de Login Seguro
def login_usuario() -> str:
    print("\n===== Tela de Login =====")
    for _ in range(3):
        usuario = input("Usuário: ").lower()
        senha = entrada_senha()  # Chama a função para digitar a senha
        if usuario in USUARIOS and bcrypt.checkpw(senha.encode(), USUARIOS[usuario]):
            print("\nLogin bem-sucedido!")
            return usuario
        print("Usuário ou senha incorretos.")
    print("Tentativas excedidas.")
    return ""
