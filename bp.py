# importa biblioteca
import os

# nome e idade do usuário
nome = input('Informe o seu nome:')
idade = int(input('Informe a sua idade:'))

# limpa console
os.system('cls')

# inicia o loop
while True:
    # lista de salas e filmes
    print(f'{'='*20}CINE COBRA{'='*20}\n')
    print(f'{'-'*20}Lista de filmes:{'-'*20}\n')
    print('Sala 1 - A Princesa e O Sapo - Livre;')
    print('Sala 2 - Velozes e Furiosos 1 - 18 anos;')
    print('Sala 3 - 2012 - 18 anos;')
    print('Sala 4 - Coraline - 16 anos;')
    print('Sala 5 - A Casa Monstro - 16 anos;')

    # usuário informa a sala
    sala = input('Informe a sala desejada:')

    # limpa console
    os.system('cls')

    # verifica a sala e a idade
    match sala:
        case '1':
            idade_minima = 0
        case '2':
            idade_minima = 18
        case '3':
            idade_minima = 18
        case '4':
            idade_minima = 16
        case '5':
            idade_minima = 16
        case _:
            print('Sala inexistente.')
            continue

    if idade >= idade_minima:
        print(f'Ingresso liberado para {nome}. Bom filme!')
        break
    else:
        print(f'Entrada não permitida para {nome}. Favor escolher outro filme!')
        continue

