preco = float(input('Qual o preço do produto? R$ '))
pgto_vista = preco - 0.32 * preco
pgto_prazo = 1.15 * preco
print(f'O pagamento deste produto que custa R$ {preco} à vista sai, com 32% de desconto, por R$ {pgto_vista:.2f}\ne a prazo, com juros de 15%, R$ {pgto_prazo:.2f}.')
