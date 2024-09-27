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


# Função para processar a categoria escolhida pelo usuário
def processa_categoria_escolhida(categoria):
    
    # Dicionário com as categorias mapeadas
    categorias = {
        1: "Países",
        2: "Verbos",
        3: "Animais",
        4: "Frutas"
    }
    
    # Se a entrada do usuário for um número válido
    if categoria in [0, 1, 2, 3, 4]:
        # Verifica se não é a opção de voltar ao menu
        if not categoria == 0:
            # Obtem a categoria no dicionário de acordo com o valor
            nome_categoria = categorias.get(categoria)
            limpar_terminal() 
            # Função para iniciar o jogo, passando a categoria como parametro
            jogo_forca(nome_categoria)
        else:
            print("Voltando para o menu")
            limpar_terminal()
            # Encerra o loop, voltando assim para o menup principal
            return False
    else:
        print("\n\nInsira uma opção válida.")
        limpar_terminal()
        # Mantem o loop ativo
        return True


def obtem_categoria():
    print("========== CATEGORIAS ==========")
    print("\nVoltar ao menu = 0;")
    print("\nPaíses = 1;")
    print("Verbos = 2;")
    print("Animais = 3;")
    print("Frutas = 4.")

    # Try adicionado para capturar erros na conversão da entrada do usuário para um inteiro
    try:
        # Define categoria com o input do usuário
        categoria = int(input("\nEscolha uma opção: "))
    except:
        print("\n\nInsira uma opção válida.")
        limpar_terminal()
        # Mantem o loop ativo
        return True
    
    return processa_categoria_escolhida(categoria)


# Função para processar a escolha do usuário
def processa_escolha_usuario(menu_opcao):
    
    # Se a entrada do usuário for um número válido
    if menu_opcao in [1, 2]:
        # Se o usuário escolher a opção igual a 1, o jogo inicia
        if menu_opcao == 1:
            limpar_terminal()            
            # Inicia o jogo da forca
            # A função obter categoria, traz as opções disponíveis dentro da categoria selecionada na função
            menu_categoria_loop= True
            while menu_categoria_loop:
                # Define loop com o valor retornado da função 'obtem_categoria()'
                menu_categoria_loop = obtem_categoria()
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
    
    # Try adicionado para capturar erros na conversão da entrada do usuário para um inteiro
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