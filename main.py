#Programa que calcula o índice de massa corporal
#Conversão de entrada de dados
print("============CALCULADORA DE IMC==============")
peso = float(input("Digite Seu Peso: "))
altura = float(input("Digite sua altura: "))
imc = peso / (altura**2)
print('Seu índice de massa corporal é {:.2f}'.format(imc)) 

if imc < 18.5:
	print("Classificação: Magreza")
elif imc < 24.9:
	print("Classificação: Saudável")
elif imc < 29.9:
	print("Classificação: Sobrepeso")
elif imc < 34.9:
	print("Classificação: Obesidade de grau I")
elif imc < 39.9:
	print("Classificação: Obesidade grau II")
else:
	print("Classificação: Obesidade Mórbida")
