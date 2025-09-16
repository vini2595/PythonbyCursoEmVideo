dias = int(input('Quantos dias alugados? '))
k = int(input('Quantos kms rodados? '))
total_a_pagar = 60 * dias + 0.15 * k
print(f'O total a pagar é de R$ {total_a_pagar:.2f}.')
