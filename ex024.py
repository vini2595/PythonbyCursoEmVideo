cidade = str(input('Digite o nome de uma cidade: '))
cidade_1 = cidade.split()
resposta = 'Santo' in cidade_1
print(f'O nome desta cidade começa com "Santo"? {resposta}')
