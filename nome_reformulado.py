# (09.04.2024)
# faca um programa que receba o nome do usuario e a posicao
# em que ele deseja adicionar uma letra, se a ltra que estiver
# na posicao indica for 'S', substitua for 'R', se a letra for
# 'M', substitua for 'N'.
# senao for nenhuma dessas, remova a letra do nome
# imprima na tela, a palavra reformulada.

nome = input('nome> ')
posicao = int(input('posição> '))
letra = nome[posicao]

if letra == 's' or letra == 'S':
    nome = nome[:posicao] + 'R' + nome[posicao+1:]
    print('\nnome reformulado> ', nome.capitalize())

elif letra == 'm' or letra == 'M':
    nome = nome[:posicao] + 'N' + nome[posicao+1:]
    print('\nnome reformulado> ', nome.capitalize())

else:
    nome = nome[:posicao] + nome[posicao + 1:]

    print('\nnome reformulado> ', nome.capitalize())
