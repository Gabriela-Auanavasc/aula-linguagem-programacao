
def quem_ganhou():
    # variáveis globais
    tabuleiro = []  # vazio
    resultado = ''  # string vazia

    with open('tabuleiro.txt', 'r') as arquivo:
        linhas_arquivo = arquivo.readlines()  # tirando as quebras de linhas e separando a partir das '|'s
        tabuleiro = [linhas_arquivo[0].strip('\n').split('|'),
                     linhas_arquivo[2].strip('\n').split('|'),
                     linhas_arquivo[4].strip('\n').split('|')]

        # primeiro verificar se o jogo ainda deve continuar, detectando espaços vazios
        for linha in tabuleiro:
            for jogada in linha:
                if jogada == ' ':
                    resultado = 'o jogo ainda não acabou...'

        # verificar as linhas
        for linha in tabuleiro:
            if linha[0] == linha[1] == linha[2] and linha[0] != ' ':
                resultado = f'o jogador {linha[0]} ganhou'

        # verificar colunas
        for coluna in [0, 1, 2]:
            if tabuleiro[0][coluna] == tabuleiro[1][coluna] == tabuleiro[2][coluna] and tabuleiro[0][coluna] != ' ':
                resultado = f'o jogador {tabuleiro[0][coluna]} ganhou'

        # verificar cada posicao nas linhas do tabuleiro
        if tabuleiro[0][0] == tabuleiro[0][1] == tabuleiro[0][2] and tabuleiro[0][0] != ' ':
            resultado = f'o jogador {tabuleiro[0][0]} ganhou'
        elif tabuleiro[1][0] == tabuleiro[1][1] == tabuleiro[1][2] and tabuleiro[1][0] != ' ':
            resultado = f'o jogador {tabuleiro[1][0]} ganhou'
        elif tabuleiro[2][0] == tabuleiro[2][1] == tabuleiro[2][2] and tabuleiro[2][0] != ' ':
            resultado = f'o jogador {tabuleiro[2][0]} ganhou'

        # colunas
        if tabuleiro[0][0] == tabuleiro[1][0] == tabuleiro[2][0] and tabuleiro[0][0] != ' ':
            resultado = f'o jogador {tabuleiro[0][0]} ganhou'
        elif tabuleiro[1][0] == tabuleiro[1][1] == tabuleiro[2][1] and tabuleiro[1][0] != ' ':
            resultado = f'o jogador {tabuleiro[1][0]} ganhou'
        elif tabuleiro[2][0] == tabuleiro[2][1] == tabuleiro[2][2] and tabuleiro[2][0] != ' ':
            resultado = f'o jogador {tabuleiro[2][0]} ganhou'

        # diagonais
        # 00 == 11 == 22
        # 20 == 11 == 02
        if tabuleiro[0][0] == tabuleiro[1][1] == tabuleiro[2][2] and tabuleiro[0][0] != ' ':
            resultado = f'o jogador {tabuleiro[0][0]} ganhou'
        elif tabuleiro[2][0] == tabuleiro[1][1] == tabuleiro[0][2] and tabuleiro[2][0] != ' ':
            resultado = f'o jogador {tabuleiro[2][0]} ganhou'

        # empate:
        if resultado == '':
            resultado = 'deu empate'

    return resultado
