
# Faça um programa que leia um arquivo no formato
# padrão exibido pela professora. O arquivo é um tabuleiro
# de jogo da velha e seu programa deve informar quem ganhou
# o jogo ou se houve empate.

# Exemplo do Arquivo:
# X| |X
# -----
# X|O|O
# -----
# X|O|X

# O arquivo sempre terá 5 linhas; as linhas 2 e 4 sempre
# serão tracejados; Só podem ter os caracteres X, O, | ou espaço
# vazio em cada posição do arquivo.

with open ('jogo_da_velha.txt', 'w') as arquivo:
    arquivo.write('X| |X\n')
    arquivo.write('-----\n')
    arquivo.write('X|O|O\n')
    arquivo.write('-----\n')
    arquivo.write('X|O|X')

# variáveis globais
tabuleiro = [] # vazio
resultado = '' # string vazia

with open ('jogo_da_velha.txt', 'r') as arquivo:
    linhas_arquivo = arquivo.readlines() # tirando as quebras de linhas e separando a partir das '|'s
    tabuleiro = [linhas_arquivo[0].strip('\n').split('|'),
                 linhas_arquivo[2].strip('\n').split('|'),
                 linhas_arquivo[4].strip('\n').split('|')]

    # primeiro verificar se o jogo ainda deve continuar, detectando espaços vazios
    for linha in tabuleiro:
        for jogada in linha:
            if jogada == ' ':
                resultado = 'o jogo ainda não acabou'

    # verificar as linhas
    for linha in tabuleiro:
        if linha[0] == linha[1] == linha[2] and linha[0] != ' ':
            resultado = linha[0]

    # verificar colunas
    for coluna in [0, 1, 2]:
        if tabuleiro[0][coluna] == tabuleiro[1][coluna] == tabuleiro[2][coluna] and tabuleiro[0][coluna] != ' ':
            resultado = tabuleiro[0][coluna]

    # verificar cada posicao nas linhas do tabuleiro
    if tabuleiro[0][0] == tabuleiro[0][1] == tabuleiro[0][2] and tabuleiro[0][0] != ' ':
        resultado = tabuleiro[0][0]
    elif tabuleiro[1][0] == tabuleiro[1][1] == tabuleiro[1][2] and tabuleiro[1][0] != ' ':
        resultado = tabuleiro[1][0]
    elif tabuleiro[2][0] == tabuleiro[2][1] == tabuleiro[2][2] and tabuleiro[2][0] != ' ':
        resultado = tabuleiro[2][0]

    # colunas
    if tabuleiro[0][0] == tabuleiro[1][0] == tabuleiro[2][0] and tabuleiro[0][0] != ' ':
        resultado = tabuleiro[0][0]
    elif tabuleiro[1][0] == tabuleiro[1][1] == tabuleiro[2][1] and tabuleiro[1][0]!= ' ':
        resultado = tabuleiro[1][0]
    elif tabuleiro[2][0] == tabuleiro[2][1] == tabuleiro[2][2] and tabuleiro[2][0] != ' ':
        resultado = tabuleiro[2][0]

    # diagonais
    # 00 == 11 == 22
    # 20 == 11 == 02
    if tabuleiro[0][0] == tabuleiro[1][1] == tabuleiro[2][2] and tabuleiro[0][0] != ' ':
        resultado = tabuleiro[0][0]
    elif tabuleiro[2][0] == tabuleiro[1][1] == tabuleiro[0][2] and tabuleiro[2][0] != ' ':
        resultado = tabuleiro[2][0]

    # ou:
    # quem marcou na diagonal (meio) ganha
    #if tabuleiro[0][0] == tabuleiro[1][1] == tabuleiro[2][2] or tabuleiro[2][0] == tabuleiro[1][1] == tabuleiro[0][2] and tabuleiro[0][0] != ' ':
        #resultado = tabuleiro[2][0]

    # empate:
    if resultado == '':
        resultado = '> EMPATE'

    print('resultado>', resultado)

    # empate:
    if resultado == '':
        resultado = '> EMPATE'

    print('resultado>', resultado)
