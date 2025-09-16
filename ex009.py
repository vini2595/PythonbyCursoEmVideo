import time
n = int(input('Digite um número para ver sua tabuada: '))
print('-'*20)
c = 1
while c <= 10:
    print(f'{n:>4} x {c:2} = {n * c}')
    c += 1
    time.sleep(0.5)
print('-'*20)
