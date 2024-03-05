# Faça um Programa que peça as 4 notas bimestrais e mostre a média.

nota1 = int(input('Digite a nota do primeiro bimestre: \n'))
nota2 = int(input('Digite a nota do segundo bimestre: \n'))
nota3 = int(input('Digite a nota do terceiro bimestre: \n'))
nota4 = int(input('Digite a nota do quarto bimestre: \n'))

res = (nota1 + nota2 + nota3 + nota4)/4

print(f'A média das 4 notas informadas, foi de: {res}')