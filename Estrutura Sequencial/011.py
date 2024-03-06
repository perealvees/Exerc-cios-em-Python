# Faça um Programa que peça 2 números inteiros e um número real. Calcule e mostre:
# o produto do dobro do primeiro com metade do segundo .
# a soma do triplo do primeiro com o terceiro.
# o terceiro elevado ao cubo.

print('Ola, tudo bem?')
int1 = int(input('Digite um número inteiro: \n'))
int2 = int(input('Digite outro número inteiro: \n'))
real = float(input('Digite um número real: \n'))

dobprime = (int1 * 2) + int2/2
somatriplo = (real * 3) + real
realcubo = real ** 3


print(f'O produto do dobro do primeiro com metade do segundo é {dobprime} \n')
print(f'A soma do triplo do primeiro com o terceiro {somatriplo} \n')
print(f'O terceiro elevado ao cubo é {realcubo}. \n')