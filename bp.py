# nome e idade do usuário
nome = input('Informe o seu nome:')
idade = int(input('Informe a sua idade:'))

# lista de salas e filmes
print('Lista de filmes:\n')
print('Sala 1 - A Princesa e O Sapo;')
print('Sala 2 - Velozes e Furiosos 1;')
print('Sala 3 - 2012;')
print('Sala 4 - Coraline;')
print('Sala 5 - A Casa Monstro;')

# usuário informa a sala
sala = int(input('Informe a sala desejada:'))

match sala: 
    case 1:
        print(f'Filme escolhido por {nome}: A Princesa e O Sapo.')
    case 2:
        print(f'Filme esolhido por {nome}: Velozes e Furiosos 1.')
    case 3:
        print(f'Filme escolhido por {nome}: 2012.')
    case 4:
        print(f'Filme escolhido por {nome}: Coraline.')
    case 5:
        print(f'Filme escolhido por {nome}: A Casa Monstro.')
    case _:
        print('Sala inexistente')
    
Princesa = print('A Princesa e O Sapo.')
Velozes = print('Velozes e Furiosos 1.')
Doze = print('2012.')
Coraline = print('Coraline')
Casa = print('A Casa Monstro.')

# classificação indicativa
if idade >= 18: 
    print(f'{nome} está liberado para ver {Velozes}.')
    print(f'{nome} está liberado para ver {Doze}.')
    print (f'{nome} está liberado para ver {Princesa}.')
    print(f'{nome} está liberado para ver {Coraline}.')
    print(f'{nome} está liberado para ver {Casa}.')
elif idade >= 16:
    print(f'{nome} não está liberado para ver {Velozes}.')
    print(f'{nome} não está liberado para ver {Doze}.')
    print(f'{nome} está liberado para ver {Coraline}.')
    print(f'{nome} está liberado para ver {Casa}.')
    print(f'{nome} está liberado para ver {Princesa}.')
else:
    print(f'{nome} não está liberado para ver {Velozes}.')
    print(f'{nome} não está liberado para ver {Doze}.')
    print(f'{nome} não está liberado para ver {Coraline}.')
    print(f'{nome} não está liberado para ver {Casa}.')
    print(f'{nome} está liberado para ver {Princesa}.')

    