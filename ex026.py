frase = str(input('Digite uma frase: ')).upper()
print(f'1 - A letra "A" aparece {frase.count("A")} vezes.')
print(f'2 - A primeira vez em que a letra "A" aparece é na posição {frase.find("A")}.')
print(f'3 - A última vez em que a letra "A" aparece é na posição {frase.rfind("A")}.')

