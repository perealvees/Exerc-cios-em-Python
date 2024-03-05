# Faça um Programa que calcule a área de um quadrado, em seguida mostre o dobro desta área para o usuário.
# Para termos uma area em quadrado, multiplicamos o comprimento da sua base pela sua altura

base = float(input('Digite o valor da base do quadrado: \n'))
comp = float(input('Digite a altura do quadrado: \n'))

areaq = (base*comp) * 2
print(f'O valor da area calculado é de {areaq}')