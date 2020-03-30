from random import randint
a = (randint(1,20))

contador = 1
sorteio = True

while sorteio and contador <=5:
    numero = int(input('Escolha um número de 1 a 20: '))
    while numero < 1 or numero >20:
        numero = int(input('Escolha um número de 1 a 20: '))
    if numero < a:
        print ('Muito baixo')
        contador += 1
    elif numero > a:
        print ('Muito alto')
        contador += 1
    else:
        sorteio = False
        print ('Acertou em {0} tentativas!'.format(contador))

if contador > 5:
    print('Que pena, você perdeu!')   