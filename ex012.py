preco = float(input('Qual é o preço do produto? R$ '))
desconto = preco - 0.05 * preco
print(f'O produto que custava R$ {preco}, na promoção, com desconto de 5%, vai custar R$ {desconto:.2f}.')