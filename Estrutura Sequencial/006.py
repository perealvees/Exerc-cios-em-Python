# Faça um Programa que peça o raio de um círculo, calcule e mostre sua área.
# De acordo com o Google, para saber a área de um círculo, é pi vezes o raio elevado ao quadrado

PI = 3.14
raio = float(input('Digite o valor do raio a ser calculado: \n'))

area = PI * (raio ** 2)

print('A área do círculo é {:.2f}'.format(area))