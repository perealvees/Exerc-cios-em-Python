''' Tendo como dado de entrada a altura (h) de uma pessoa, construa um algoritmo que calcule seu peso ideal, utilizando as seguintes fórmulas:
Para homens: (72.7*h) - 58
Para mulheres: (62.1*h) - 44.7 '''

altura = int(input('Digite sua altura em centimetros: \n'))
sexo = str(input('Digite seu sexo: F ou M \n'))

pesoh = (72.7 * altura) - 58
pesom = (62.1 * altura) - 44.7

if (sexo == 'F'):
    print(f'Seu peso ideal é de {pesom}kg. \n')
else:
    print(f'Seu peso ideal é de {pesoh}kg. \n')