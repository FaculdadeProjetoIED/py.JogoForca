# ==================== Importações e definições gerais ====================
# Importações
from msvcrt import getch # Importação do Getch para a captura da tecla de confirmação do usuário
import os # Importação do os para que o terminal possa ser limpo
from JogoDaForca.JogoForca import jogo_forca # Importação do jogo da forca para ser inicializado

# Função para limpar o terminal
def limpar_terminal():
    print("\nPressione 'ENTER'para continuar.")
    getch() # Captura a tecla de confirmação pessioanda pelo usuário
    os.system('cls') # cls, pois a máquina de desenvolvimento é windows

# Função para processar a escolha do usuário
def processa_escolha_usuario(menu_opcao):
    
    # Se a entrada do usuário foi um número inteiro de apenas 1 caractere
    if menu_opcao in [1, 2]:
        # Se o usuário escolher a opção igual a 1, o jogo inicia
        if menu_opcao == 1:
            limpar_terminal()
            # Inicia o jogo da forca
            jogo_forca()
            # Mantem o loop ativo
            return True
        # Se o usuário escolher a opção igual a 2, o jogo é encerrado
        elif menu_opcao == 2:
            limpar_terminal()
            print("\nVocê escolheu sair do jogo.")
            # Encerra o loop
            return False
        # Senão, avisa ao usuário que ele deve escolher uma opção válida
        else:
            print("\n\nInsira uma opção válida.")
            limpar_terminal()
            # Mantem o loop ativo
            return True
    # Senão, avisa ao usuário que ele deve escolher uma opção válida
    else:
        print("\n\nInsira uma opção válida.")
        limpar_terminal()
        # Mantem o loop ativo
        return True


# Função para exibir o menu e obter a escolha do usuário
def menu():
    print("\n\n           JOGO DA FORCA - UNIFACCAMP           ")
    print("================================================")
    print("                      MENU                      \n")
    print("\nPara jogar, pressione 1;")
    print("Para sair do jogo, pressione 2.\n")
    
    try:
        # Define menu_opcao com o input do usuário
        menu_opcao = int(input("\nEscolha uma opção: "))
    except:
        print("\n\nInsira uma opção válida.")
        limpar_terminal()
        # Mantem o loop ativo
        return True
    
    return processa_escolha_usuario(menu_opcao)


# Função principal do jogo da forca
def main():
    os.system('cls') # cls, pois a máquina de desenvolvimento é windows
    # Define a variável menu_loop como True para poder iniciar o loop de interação com o usuário
    menu_loop = True
    # Loop para chamar o menu após cada opção
    while menu_loop:
        # Define loop com o valor retornado da função 'menu()'
        menu_loop = menu()


# Executa a função main
if(__name__ == "__main__"):
    main()