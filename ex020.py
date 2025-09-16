from random import randint, random, shuffle
lista = []
for i in range(1, 5):
    nomes = str(input(f'{i}° aluno: '))
    lista.append(nomes)
shuffle(lista)
print('A ordem de apresentação será:', end=' ')
for x in lista:
    print(x, end=', ')

