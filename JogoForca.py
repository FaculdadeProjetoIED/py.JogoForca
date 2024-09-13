# Importações
from msvcrt import getch # Importação do Getch para a captura da tecla de confirmação do usuário
import os # Importação do os para que o terminal possa ser limpo

# Definições
alvo = "hangman"
letras_usadas = []
tentativas = 0
# Variável para definir a quantidade de erros do usuário
tentativas_falhas = 0
acertou = False
# Variável para definir se a dica será exibida ou não
dica_ativa = True
# Variável para definir a string da dica para poder ser impressa
dica_mensagem = ""



# Função para limpar o terminal
def limpar_terminal():
    print("Pressione 'ENTER'para continuar.")
    getch() # Captura a tecla de confirmação pessioanda pelo usuário
    os.system('cls') # cls, pois a máquina de desenvolvimento é windows

def validacao_escolha_usuario(menu_opcao):
    if menu_opcao == "1":
        print("\nDica")
        limpar_terminal()
    elif menu_opcao == "2":
        print("\nVocê desistiu do jogo.")
        return False
    else:
        limpar_terminal()

# Função para exibir o menu e obter a escolha do usuário
def menu_opcoes():
    print("========== MENU DE OPÇÕES ==========")
    print("Para receber uma dica, pressione 1;")
    print("Para desistir do jogo, pressione 2;")
    print("Para continuar jogando, pressione qualquer tecla de A a Z.")
    print(f"\nTentativas: {tentativas}\nErros: {tentativas_falhas}/6") # Exibe a quantidade de tentativas e de erros
    
    # Define menu_opcao com o input do usuário em lowercase
    menu_opcao = input("\nEscolha uma opção: ").lower()

    # Chama a função 'validacao_escolha_usuario()' para verificar a escolha do usuário.
    # Após a verificação, o jogo continua ou não dependendo do retorno dessa função. Ela quem define se o loop será encerrado ou não
    return validacao_escolha_usuario(menu_opcao)



# Função principal do jogo da forca
def main():
    # Define a variável menu_loop como True para poder iniciar o loop de interação com o usuário
    menu_loop = True
    # Loop para chamar o menu após cada tentativa
    while menu_loop:
        # Define loop com o valor retornado da função 'menu_opcoes()'
        menu_loop = menu_opcoes()

# Verifica se o programa é executado diretamente
if __name__ == "__main__":
    # Chama a função principal
    main()