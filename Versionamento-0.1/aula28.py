nome = input('Digite seu nome:')

idade = input('Digite sua idade:')

if nome and idade:
    print(f'seu nome é {nome}')
    print(f'Seu nome de trás pra frente fica :{nome[-1:-10:-1]}')

    if ' ' in nome:
        print('Seu nome contém espaços')
    else:
        print('Seu nome não contém espaços')

    print(f'Seu tel {len(nome)} letras') 

    print(f'Primeira letra do seu nome é:"{nome[0]}"')

    print(f'ultima letra do seu nome é:"{nome[8]}"')
else:
    print('Desculpe, você deixou campos vazios.')    


