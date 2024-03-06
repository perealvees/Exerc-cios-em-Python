# Faça um Programa que peça a temperatura em graus Celsius, transforme e mostre em graus Fahrenheit.

fire = float(input('Digite a temperatura em °F \n'))
cel = (fire-32)/1.8

print(f'A temperatura de {fire} °F convertida em Celsius é de {cel:.2f} °C')