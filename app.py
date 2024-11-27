# ==================== Importações e definições gerais ====================
# Importações
from msvcrt import getch  # Importação do Getch para a captura da tecla de confirmação do usuário
import os  # Importação do os para que o terminal possa ser limpo
import requests # Importação para poder obter as palavras
import random  # Importação para poder sortear as palavras
from unidecode import unidecode  # Importação para remover acentuação das letras e palavras

# ==================== Controle - jogo da forca ====================

# Função para limpar o terminal
def limpar_terminal():
    print("\nPressione 'ENTER' para continuar.")
    getch()  # Captura a tecla de confirmação pressionada pelo usuário
    os.system('cls')  # cls, pois a máquina de desenvolvimento é windows


# Obtém uma palavra aleatória para o jogo usando a API.
def nova_palavra():
    try:
        # Faz a requisição diretamente ao endpoint
        resposta = requests.get("https://faccamp.pythonanywhere.com/hangman-api/getdata")

        # Converte a resposta JSON em um dicionário Python
        dado = resposta.json()

        if dado:
            return dado
        else:
            print("Erro: o campo 'palavra' não foi encontrado na resposta da API.")
            return None

    except requests.exceptions.RequestException as e:
        print("Erro na conexão com a API: ", e)
        return None


# Função para exibir quantidade de letras da palavra
def dica_atualizar():
    global dica_mensagem, alvo  # Variáveis globais para manipulação dentro da função
    dica_mensagem = ""
    for char in alvo:
        if char in letras_usadas:
            dica_mensagem += char + ' '
        elif char.isalpha():
            dica_mensagem += "_ "
        else:
            dica_mensagem += " "
    dica_mensagem = f"A palavra tem {len(alvo)} letras.\n\n{dica_mensagem}"


# Função para validar a entrada (input, 'menu_opcao') do usuário
def validacao_input_usuario(menu_opcao):
    # Verifica se a letra foi usada antes
    if menu_opcao in letras_usadas:
        print("Insira uma letra não usada anteriormente.")
        return False
    # Verifica se o input é uma letra única
    elif len(menu_opcao) == 1 and menu_opcao.isalpha():
        return True
    else:
        if len(menu_opcao) != 1:
            print("Insira apenas uma letra.")
        else:
            print("Opção inválida")
        return False


# Função para verificar se a letra está na palavra do 'alvo'
def verificacao_palpite(menu_opcao):
    global tentativas_falhas
    if menu_opcao in alvo:  # Verifica se a letra está na palavra
        print(f"\n\nA letra '{menu_opcao}' está na palavra!")
        dica_atualizar()  # Atualiza a dica com as letras corretas
        if verificacao_vitoria():  # Verifica se o jogador ganhou
            return
    else:
        print(f"\n\nA letra '{menu_opcao}' não está na palavra, tente novamente!")
        tentativas_falhas += 1


# Função para exibir o resultado do jogo
def exibe_resultado(acertou):
    if acertou:
        print("\n\nParabéns. Você ganhou!")
        print(f"Com {tentativas} tentativas.")
    else:
        print("\n\nPerdeu!")
        print("A palavra era:", alvo)


# Função para verificar se o usuário ganhou o jogo
def verificacao_vitoria():
    global acertou
    todas_letras_validadas = all(
        letra.isalpha() and letra in letras_usadas for letra in alvo)
    if todas_letras_validadas:
        limpar_terminal()
        acertou = True
        exibe_resultado(acertou)
        return True
    else:
        return False


# Função para processar a escolha do usuário
def processa_escolha_usuario(menu_opcao, acertou):
    global dica_mensagem, dica_ativa, tentativas, segunda_dica_ativa
    if tentativas_falhas >= 5:
        verificacao_palpite(menu_opcao)
        limpar_terminal()
        exibe_resultado(False)
        return False
    elif menu_opcao == "1":
        dica_atualizar()
        print(f"\n\n{dica_mensagem}")
        dica_ativa = True
        limpar_terminal()
    elif menu_opcao == "2":
        print("\nVocê desistiu do jogo.")
        return False
    elif menu_opcao == "3":
        segunda_dica_ativa = True
        limpar_terminal()
    elif validacao_input_usuario(menu_opcao):
        letras_usadas.append(menu_opcao)
        tentativas += 1
        verificacao_palpite(menu_opcao)
        if verificacao_vitoria():
            return False
        limpar_terminal()
    else:
        limpar_terminal()
    return not acertou


# Função principal do jogo da forca
def jogo_forca():
    global alvo, tentativas, tentativas_falhas, letras_usadas, dica_mensagem, dica_ativa, segunda_dica_ativa, acertou, categoria_api
    
    # Obtém a palavra da API
    json_api = nova_palavra()

    # Obtém a palavra do JSON retornado
    palavra_api = json_api.get("palavra")
    # Obtém a categoria do JSON retornado
    categoria_api = json_api.get("categoria")
    # Obtém a complexidade do JSON retornado
    complexidade_api = json_api.get("complexidade")
    
    if palavra_api is None:
        print("Não foi possível obter uma palavra para o jogo.")
        return
    
    alvo = unidecode(palavra_api.lower())  # Remove acentos e converte para minúsculas
    tentativas, tentativas_falhas, letras_usadas = 0, 0, []
    dica_ativa, segunda_dica_ativa, acertou = False, False, False
    dica_atualizar()
    
    jogando = True
    while jogando:
        jogando = menu_jogando()


# Função para exibir o desenho da forca baseado nas tentativas falhas
def desenho_forca(tentativas_falhas):
    print("  _______     ")
    print(" |/      |    ")

    if (tentativas_falhas == 1):
        print(" |      (_)   ")
        print(" |            ")
        print(" |            ")
        print(" |            ")
    elif (tentativas_falhas == 2):
        print(" |      (_)   ")
        print(" |      \|    ")
        print(" |            ")
        print(" |            ")
    elif (tentativas_falhas == 3):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |            ")
        print(" |            ")
    elif (tentativas_falhas == 4):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |            ")
    elif (tentativas_falhas == 5):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      /     ")
    elif (tentativas_falhas == 6):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      / \   ")
    else:
        print(" |")
        print(" |")
        print(" |")
        print(" |")

    print(" |            ")
    print("_|___         ")


# Função para exibir o menu e obter a escolha do usuário
def menu_jogando():
    print("========== MENU DE OPÇÕES ==========")
    if not dica_ativa:
        print("Para receber uma dica de duas, pressione 1;")
    print("Para desistir do jogo, pressione 2;")
    if dica_ativa and not segunda_dica_ativa:
        print("Para receber a segunda e ultima dica, pressione 3;")
    print(alvo)
    print("Para continuar jogando, pressione qualquer tecla de A a Z.")
    if letras_usadas:
        # Exibe as letras já usadas e a quantidade de erros
        print(f"\nLetras já utilizadas: {', '.join(letras_usadas)}\nErros: {tentativas_falhas}/6")
        
    desenho_forca(tentativas_falhas)
    
    # Se 'dica_ativa' estiver ativa após o usuário pressionar 1, a dica será exibida até o fim do jogo
    if dica_ativa:
        print(f"\n{dica_mensagem}")

    # Se 'segunda_dica_ativa' estiver ativa após o usuário pressionar 3, a dica será exibida até o fim do jogo
    if segunda_dica_ativa:
        print(f"\nA categoria da palavra é: {categoria_api.capitalize()}")

    # Define menu_opcao com o input do usuário em lowercase
    menu_opcao = unidecode(input("Escolha uma opção: ")).lower()
    
    # Chama a função 'processa_escolha_usuario()' para verificar a escolha do usuário.
    # Após a verificação, o jogo continua ou não dependendo do retorno dessa função. Ela quem define se o loop será encerrado ou não
    return processa_escolha_usuario(menu_opcao, acertou)


# Função para processar a escolha do usuário no menu principal
def processa_escolha_usuario_menu(menu_opcao):
    if menu_opcao in [1, 2]:
        if menu_opcao == 1:
            limpar_terminal()
            menu_principal_loop = True
            while menu_principal_loop:
                menu_principal_loop = jogo_forca()
            return True
        elif menu_opcao == 2:
            limpar_terminal()
            print("\nVocê escolheu sair do jogo.")
            return False
    else:
        print("\n\nInsira uma opção válida.")
        limpar_terminal()
        return True


# Função para exibir o menu principal
def menu():
    print("\n\n           JOGO DA FORCA - UNIFACCAMP           ")
    print("================================================")
    print("                      MENU                      \n")
    print("\nPara jogar, pressione 1;")
    print("Para sair do jogo, pressione 2.\n")
    try:
        menu_opcao = int(input("\nEscolha uma opção: "))
    except:
        print("\n\nInsira uma opção válida.")
        limpar_terminal()
        return True
    return processa_escolha_usuario_menu(menu_opcao)


# Função principal
def main():
    os.system('cls')  # cls, pois a máquina de desenvolvimento é windows
    menu_loop = True
    while menu_loop:
        menu_loop = menu()


# Executa a função main
if __name__ == "__main__":
    main()
