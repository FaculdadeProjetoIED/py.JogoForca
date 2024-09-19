# Projeto Python - Jogo da Forca

Este projeto foi desenvolvido para a disciplina "Projeto Interdisciplinar de Estruturas de Dados" na faculdade. O time é composto por três alunos:

- @vitoroliveirasilva
- @RyanJacob431
- @ThomazGC

## Objetivo
O objetivo deste projeto é criar um jogo da forca utilizando implementações que envolvam estruturas de dados. Através deste projeto, buscamos aplicar os conhecimentos adquiridos em aula, desenvolvendo uma aplicação prática e interativa.

## Índice

1. [Jogo da Forca em Python](#jogo-da-forca-em-python)
2. [Funcionalidades](#funcionalidades)
3. [Como funciona](#como-funciona)
4. [Requisitos](#requisitos)
5. [Como rodar o jogo](#como-rodar-o-jogo)
6. [Licença](#licença)

# Jogo da Forca em Python

Este projeto é um jogo da forca implementado em Python, onde o jogador tenta adivinhar uma palavra secreta letra por letra. O jogo inclui um sistema de dicas, controle de tentativas erradas e feedback para o usuário após cada palpite.

## Funcionalidades

- Limpeza do terminal para uma interface mais organizada (compatível com Windows).
- Sistema de dicas que exibe a quantidade de letras da palavra.
- Validação das entradas do usuário para garantir que apenas letras válidas sejam inseridas.
- Contador de tentativas erradas com limite de 6 erros.
- Exibição de uma mensagem de vitória ou derrota ao final do jogo.

## Como funciona

O jogo escolhe uma palavra secreta e o jogador deve adivinhar as letras. Para cada letra correta, a palavra é atualizada e mostrada ao jogador. O jogador tem até 6 tentativas erradas antes de perder o jogo. A qualquer momento, o jogador pode solicitar uma dica ou desistir.

### Opções no jogo

- Pressionar **1**: Exibe uma dica, mostrando a quantidade de letras e as letras já adivinhadas.
- Pressionar **2**: Desiste do jogo.
- Pressionar uma letra (A-Z): Faz uma tentativa de adivinhar uma letra.

## Requisitos

- Python 3 ou superior instalado no sistema.

## Como rodar o jogo

1. Clone o repositório ou baixe o arquivo do projeto.
2. No terminal, navegue até o diretório do projeto.
3. Execute o arquivo principal:

```bash
python JogosForca.py run
```

Ou acesse e execute o código no <a href="https://colab.research.google.com/drive/1F6J3zDOhrzuiIsPOyaB9o0SMNHfuz4kp?usp=sharing" target="_blank">Google Colab</a>

## Licença

Este projeto está licenciado sob a Licença MIT - veja o arquivo [LICENSE](LICENSE) para detalhes.