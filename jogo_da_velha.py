
from funcao_quem_ganhou import quem_ganhou

tabuleiro = [[' ', ' ', ' '],
             [' ', ' ', ' '],
             [' ', ' ', ' ']]

# passo 1:
# funcao para exibir o menu inicial
def menuInicial():
    print('--------------------------------------')
    print('>>> BEM-VINDO AO JOGO DA VELHA! :D <<<')
    print('--------------------------------------\n')

# passo 2:
# funcao para imprimir o tabuleiro de forma legível ao usuário
def exibirTabuleiro():
    # organizar o tabuleiro para que exiba sem a ultima linha :')
    for i, linha in enumerate(tabuleiro):
        print('|'.join(linha) + ' ')
        if i < len(tabuleiro) - 1:
            print('-----')
    return

# salvar o tabuleiro como um arquivo tipo txt
def atualizar_tabuleiro():
    with open('tabuleiro.txt', 'w') as arquivo:
        for i, linha in enumerate(tabuleiro):
            arquivo.write('|'.join(linha) + '\n')
            if i < len(tabuleiro) - 1:
                arquivo.write('-----\n')
    return

def marca_posicao(jogador, linha, coluna):
    if tabuleiro[linha][coluna] == ' ':
        tabuleiro[linha][coluna] = jogador

        resultado = quem_ganhou()
        if resultado != 'o jogo ainda não acabou...':
            return False  # encerra o jogo?

        atualizar_tabuleiro()
        return True
    else:
        return False

# programa:
atualizar_tabuleiro()
menuInicial()
exibirTabuleiro()

jogadas = 0
jogo_continua = True  # Variável para controlar se o jogo deve continuar ou não
# passo 3
# pedir que o jogador X escreva em qual posição do tabuleiro o jogador quer marcar

jogador = 'X'
while jogadas < 9 and jogo_continua:  # o loop continua enquanto houver jogadas disponíveis e o jogo continuar
    print(f'\n> é a vez do jogador {jogador}!\n  em qual posição você deseja jogar?')

    posicao_valida = False
    while posicao_valida == False:
        entrada = input('> ').split(' ')
        linha, coluna = int(entrada[0]), int(entrada[1])

        if marca_posicao(jogador, linha, coluna) == True:
            posicao_valida = True
        else:
            print('')
            exibirTabuleiro()

            print('\n> posição ocupada!\n  escolha outra posição...')

    jogadas += 1

    print('')
    exibirTabuleiro()

    if jogador == 'X':
        jogador = 'O'
    else:
        jogador = 'X'

    resultado = quem_ganhou()
    if resultado != 'o jogo ainda não acabou...':
        print('\n --------------------------------\n')
        exibirTabuleiro()
        print(f'\n> {resultado}!')
        print(f'   mais sorte na próxima vez! XD')
        print(' --------------------------------')
        jogo_continua = False  # se houver um vencedor, o jogo deve ser encerrado

#quem_ganhou()
# exibirTabuleiro()

############ TESTE ####################
#print(f'\nresultado> {quem_ganhou()}')
