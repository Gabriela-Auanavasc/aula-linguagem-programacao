
# escreva um programa que escreva em um
# arquivo informações no formato abaixo:

# NOME COMPLETO
# DATA_DE_HOJE      MANAUS-AM
# IDADE     BAIRRO

# depois de escrever o cabeçalho, seu programa deve ler
# o nome de uma disciplina seguida da nota, manter o cabeçalho
# escrever no arquivo até que ele digite 'sair'

# NOME_DA_DISCIPLINA, 36

from datetime import datetime

def criar_cabecalho(arquivo):
    nome, sobrenome = input('digite seu nome e sobrenome> ').split(' ')
    nome = nome.capitalize()
    sobrenome = sobrenome.capitalize()
    texto = nome + ' ' + sobrenome
    arquivo.write(texto)

    data_hoje = datetime.now().strftime('\n%d/%m/%Y')
    texto = data_hoje + '\t'
    arquivo.write(texto)

    cidade = input('digite sua cidade> ')
    texto = (cidade + '\t\n').capitalize()
    arquivo.write(texto)

    idade = input('digite sua idade> ')
    texto = idade + '\t'
    arquivo.write(texto)

    bairro = input('digite seu bairro> ')
    texto = (bairro + '\n').capitalize()
    arquivo.write(texto)

def disciplina_nota(arquivo):
    disciplina = input('\ndigite o nome da disciplina> ')
    nota = input('digite sua nota> ')

    while disciplina != 'sair' and nota != 'sair':
        texto = ('\n' + disciplina + ',' + nota).capitalize()
        arquivo.write(texto)

        disciplina = input('\ndigite o nome da disciplina> ')
        nota = input('digite sua nota> ')

with open('cabecalho2.txt', 'w') as arquivo:
    criar_cabecalho(arquivo)
    print('\n')
    disciplina_nota(arquivo)
  
