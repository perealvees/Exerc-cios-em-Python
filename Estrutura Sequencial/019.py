
'''
O desafio consiste em criar um programa em Python para calcular a multa a ser paga por um usuário de biblioteca que devolveu um livro com atraso.

Para isso, o programa deve solicitar ao usuário o número de dias que o livro foi devolvido após a data de vencimento e calcular a multa com base na seguinte tabela:

Até 3 dias de atraso: multa de R$ 0,50 por dia de atraso

De 4 a 7 dias de atraso: multa de R$ 1,00 por dia de atraso

Mais de 7 dias de atraso: multa de R$ 2,00 por dia de atraso

Ao final, o programa deverá exibir a mensagem “O valor da sua multa é R$ X”, em que X é o valor da multa calculada.'''

dia_atraso = int(input('Quantos dias esta atrasado essa entrega? \n'))
multa = 0

if dia_atraso <= 3:
    multa = dia_atraso * 0.5
elif dia_atraso <= 7:
    multa = dia_atraso * 1
else:
    multa = dia_atraso * 2

print(f'O valor da sa multa é de {multa:.2f} \n')