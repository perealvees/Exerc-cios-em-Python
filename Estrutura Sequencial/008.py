# Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. Calcule e mostre o total do seu salário no referido mês.

print('Olá, bom dia! ')
horaspormes = float(input('Quantos que você ganha por hora trabalhada?\n '))
diastrab = int(input('Quantas horas voce trabalhou esse mês?\n '))
totalmes = horaspormes * diastrab

print(f'Esse mês, o total do seu salário foi de R${totalmes:.2f} reais!\n ')