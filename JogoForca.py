# ==================== Importações e definições gerais ====================
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
dica_ativa = False
# Variável para definir a string da dica para poder ser impressa
dica_mensagem = ""



# ==================== Controle - jogo da forca ====================

# Função para limpar o terminal
def limpar_terminal():
    print("\nPressione 'ENTER'para continuar.")
    getch() # Captura a tecla de confirmação pessioanda pelo usuário
    os.system('cls') # cls, pois a máquina de desenvolvimento é windows


# Função para exibir quantidade de letras da palavra
def dica_atualizar():
    # Define a variável 'dica_mensagem' como global para que ela possa ser alterada dentro da função. Como em python não tem ponteiro nativo, fizemos dessa forma para que fosse possível manipular o valor das variáveis
    global dica_mensagem
    
    # Reseta a variável para que ela possa ser atualizada corretamente
    dica_mensagem = ""
    # Para cada caracter dentro da variável 'alvo'
    for char in alvo:
        # Verifica se o caracter já foi inserido pelo usuário em 'letras_usadas'
        if char in letras_usadas:
            # Se o caracter existe em 'letras_usadas', adiciona o caracter na string 'dica_mensagem'
            dica_mensagem += char + ' '
        # Verifica se o caracter é uma letra com o método 'isalpha()' do python.
        elif char.isalpha():
            # Se for uma letra, então adiciona '_ ' na string 'dica_mensagem'
            dica_mensagem += "_ "
        # Senão
        else:
            # Acrescenta apenas uma string vazia em 'dica_mensagem'
            dica_mensagem += " "
    
    # 'dica_mensagem' é definida com a exibição de quantidade de letras a ela, acrescentada do 'desenho' no terminal
    dica_mensagem = f"A palavra tem {len(alvo)} letras.\n\n{dica_mensagem}"


# Função para validar a entrada (input, 'menu_opcao') do usuário
def validacao_input_usuario(menu_opcao):
    # Verifica em 'letras_usadas' se a letra já foi inserida antes
    if menu_opcao in letras_usadas:
        print("Insira uma letra não usada anteriormente.")
        return False
    # Verifica se o tamanho da string 'menu_opcao' é igual a 1, ou seja, um carater. E se 'menu_opcao' não é um número
    elif len(menu_opcao) == 1 and not menu_opcao.isdigit():
        # Retorna True para que possa contabilizar a tentativa
        return True
    # Senão
    else:
        # Verifica se a quantidade de caracteres na string 'menu_opcao' é diferente de 1
        if len(menu_opcao) != 1:
            print("Insira apenas uma letra.")
        # Senão, o usuário pressionou um número inválido
        else:
            print("Opção inválida")
        return False


# Função para verificar se a letra está na palavra do 'alvo'
def verificacao_palpite(menu_opcao):
    # Define a variável 'tentativas_falhas' como global para que ela possa ser alterada dentro da função. Como em python não tem ponteiro nativo, fizemos dessa forma para que fosse possível manipular o valor das variáveis
    global tentativas_falhas
    
    # Verifica se o caracter inserido faz parte da palavra
    if menu_opcao in alvo:
        print(f"\n\nA letra '{menu_opcao}' está na palavra!")
        # Atualiza a 'dica_mensagem' para exibir o caracter inserido
        dica_atualizar()
        # Verifica se o usuário ganhou o jogo. Se sim, encerra o programa
        if verificacao_vitoria():
            return
    # Senão
    else:
        print(f"\n\nA letra '{menu_opcao}' não está na palavra, tente novamente!")
        # Incrementa a tentativa falha do usuário
        tentativas_falhas += 1


# Função para exibir o resultado do jogo
def exibe_resultado(acertou):
    # Verifica se o usuário acertou a palavra
    desenho_forca(tentativas_falhas)
    if acertou:
        print("\n\nParabéns. Você ganhou!")
        print(f"Com {tentativas} tentativas.")
    # Senão
    else:
        print("\n\nPerdeu!")
        print("A palavra era:", alvo)


# Função para verificar se o usuário ganhou o jogo
def verificacao_vitoria():
    # Define a variável 'acertou' como global para que ela possa ser alterada dentro da função. Como em python não tem ponteiro nativo, fizemos dessa forma para que fosse possível manipular o valor das variáveis
    global acertou
    

    todas_letras_validadas = True
    # Para cada letra em 'alvo'
    for letra in alvo:
        # Verifica se a letra é váida (ignora espaços e pontuações) e se a letra não existe nas letras já inseridas
        if letra.isalpha() and letra not in letras_usadas:
            todas_letras_validadas = False # Se a condição for verdadeira, a validação é definida como False
            break # Para o for
    
    # Se todas as letras foram acertadas
    if todas_letras_validadas:
        # Limpa o terminal e define a variável de acerto como True
        limpar_terminal()
        acertou = True
        # Exibe pro usuário a vitória
        exibe_resultado(acertou)
        return True  # Retorna True, pois o usuário ganhou o jogo
    else:
        return False  # O jogo ainda não foi vencido


# Função para processar a escolha do usuário
def processa_escolha_usuario(menu_opcao, acertou):
    # Define as seguintes variáveis como globais para que elas possam ser alteradas dentro da função. Como em python não tem ponteiro nativo, fizemos dessa forma para que fosse possível manipular o valor das variáveis
    global dica_mensagem, dica_ativa, tentativas
    
    # Verifica se o usuário atigiu o limite de 6 tentativas falhas
    if tentativas_falhas >= 5:
        verificacao_palpite(menu_opcao)
        limpar_terminal()
        exibe_resultado(False)
        return False
    
    # Se o usuário escolher a opção igual a 1, a dica é exibida
    elif menu_opcao == "1":
        # Atualiza a 'dica_mensagem'
        dica_atualizar()
        # Imprime a 'dica_mensagem'
        print(f"\n\n{dica_mensagem}")
        # Define a 'dica_ativa' como True para que a dica possa ser exibida durante todo o jogo
        dica_ativa = True
        limpar_terminal()
        
    # Se o usuário escolher a opção igual a 2, o programa é encerrado por desistencia
    elif menu_opcao == "2":
        print("\nVocê desistiu do jogo.")
        return False
    
    # Se o usuário escolher uma opção que seja diferente de 1 e 2, o programa chama a função 'validacao_input_usuario()' e valida se o input é um caracter válido
    elif validacao_input_usuario(menu_opcao):
        # Adiciona o caracter em 'letras_usadas' com o método de lista 'append'
        letras_usadas.append(menu_opcao)
        # Incrementa a tentativa
        tentativas += 1
        # Chama a função 'verificacao_palpite()' para verificar se o caracter está na palavra mesmo ou não
        verificacao_palpite(menu_opcao)
        # Verifica se o usuário ganhou
        if verificacao_vitoria():
            return False
        limpar_terminal()
    
    # Senão, o terminal é limpo e volta para o loop perguntar novamente
    else:
        limpar_terminal()

    # Retorna not da varíavel 'acertou' para poder encerrar o loop se o usuário ganhar o jogo
    return not acertou


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
def menu_opcoes():
    print("========== MENU DE OPÇÕES ==========")
    print("Para receber uma dica, pressione 1;")
    print("Para desistir do jogo, pressione 2;")
    print("Para continuar jogando, pressione qualquer tecla de A a Z.")
    if letras_usadas:
        # Exibe as letras já usadas e a quantidade de erros
        print(f"\nLetras já utilizadas: {', '.join(letras_usadas)}\nErros: {tentativas_falhas}/6")
        
    desenho_forca(tentativas_falhas)
    
    # Se 'dica_ativa' estiver ativa após o usuário pressionar 1, a dica será exibida até o fim do jogo
    if dica_ativa:
        print(f"\n{dica_mensagem}")
    
    # Define menu_opcao com o input do usuário em lowercase
    menu_opcao = input("\nEscolha uma opção: ").lower()

    # Chama a função 'processa_escolha_usuario()' para verificar a escolha do usuário.
    # Após a verificação, o jogo continua ou não dependendo do retorno dessa função. Ela quem define se o loop será encerrado ou não
    return processa_escolha_usuario(menu_opcao, acertou)



# ==================== Incialização do jogo da forca ====================

# Função principal do jogo da forca
def main():
    # Define a variável menu_loop como True para poder iniciar o loop de interação com o usuário
    menu_loop = True
    # Loop para chamar o menu após cada tentativa
    while menu_loop:
        # Define loop com o valor retornado da função 'menu_opcoes()'
        menu_loop = menu_opcoes()

# Executa a função main
main()
