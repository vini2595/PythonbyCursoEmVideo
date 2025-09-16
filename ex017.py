from math import hypot
cateto_1 = float(input('Digite o valor do cateto adjacente da hipotenusa: '))
cateto_2 = float(input('Digite o valor do segundo cateto oposto da hipotenusa: '))
print(f'A hipotenusa entre {cateto_1:.0f} e {cateto_2:.0f} é {hypot(cateto_1, cateto_2):.0f}.')


