numero = int(input('Digite um número entre 0 e 9999: '))
numero_1 = str(numero)
print('=-'*25)
print(f'Unidade: {numero_1[3]}', end='; ')
print(f'Dezena: {numero_1[2]}', end='; ')
print(f'Centena: {numero_1[1]}', end='; e ')
print(f'Milhar: {numero_1[0]}')


