import random
lista = []
for i in range(4):
    nome = str(input(f'Nome do {i + 1}° Aluno: '))
    lista.append(nome)
escolhido = random.choice(lista)
print(f'O aluno escolhido foi {escolhido}.')
