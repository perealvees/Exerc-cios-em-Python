# João Papo-de-Pescador, homem de bem, comprou um microcomputador para controlar o rendimento diário de seu trabalho. Toda vez que ele traz um peso de peixes maior que o estabelecido pelo regulamento de pesca do estado de São Paulo (50 quilos) deve pagar uma multa de R$ 4,00 por quilo excedente. João precisa que você faça um programa que leia a variável peso (peso de peixes) e calcule o excesso. Gravar na variável excesso a quantidade de quilos além do limite e na variável multa o valor da multa que João deverá pagar. Imprima os dados do programa com as mensagens adequadas.

pesopermi = 50 
multa = 4
exce = 0


totalkg = float(input('Olá, João! Quantos kg de peixes você pescou? \n'))

if (totalkg <= pesopermi):
    print(f'Você pescou {totalkg}. Dentro do permitido! \n')
elif (totalkg > pesopermi):
    exce = totalkg - pesopermi
    multa = exce * multa
    print(f'Você pescou {exce} kg a mais do permitido. Sua multa será de {multa} R$. \n')

    

