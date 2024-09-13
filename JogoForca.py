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
    print("\nPressione 'ENTER'para continuar.")
    getch() # Captura a tecla de confirmação pessioanda pelo usuário
    os.system('cls') # cls, pois a máquina de desenvolvimento é windows


# Função para exibir quantidade de letras da palavra
def dica_atualizar():
    # Define a variável 'dica_mensagem' como global para que ela possa ser alterada dentro da função. Como em python não tem ponteiro nativo, fizemos dessa forma para que fosse possível manipular o valor das variáveis
    global dica_mensagem
    
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
    # Senão
    else:
        print(f"\n\nA letra '{menu_opcao}' não está na palavra, tente novamente!")
        # Incrementa a tentativa falha do usuário
        tentativas_falhas += 1

# Função para processar a escolha do usuário
def processa_escolha_usuario(menu_opcao):
    # Define as seguintes variáveis como globais para que elas possam ser alteradas dentro da função. Como em python não tem ponteiro nativo, fizemos dessa forma para que fosse possível manipular o valor das variáveis
    global dica_mensagem, dica_ativa, tentativas
    
    # Se o usuário escolher a opção igual a 1, a dica é exibida
    if menu_opcao == "1":
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
        verificacao_palpite()
        limpar_terminal()
    
    # Senão, o terminal é limpo e volta para o loop perguntar novamente
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

    # Chama a função 'processa_escolha_usuario()' para verificar a escolha do usuário.
    # Após a verificação, o jogo continua ou não dependendo do retorno dessa função. Ela quem define se o loop será encerrado ou não
    return processa_escolha_usuario(menu_opcao)



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