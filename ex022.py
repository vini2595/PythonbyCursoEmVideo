import time
nome = str(input('Digite o seu nome: '))
print('Analisando...')
time.sleep(3)
print(f'O seu nome maiúsculo fica desta forma: {nome.upper()}.')
print(f'O seu nome minúsculo fica desta forma: {nome.lower()}.')
nome_1 = nome.replace(' ', '')
print(f'O seu nome é composto por {len(nome_1)} letras.')
print(f'O seu primeiro nome é composto por {len(nome.split()[0])} letras.')


