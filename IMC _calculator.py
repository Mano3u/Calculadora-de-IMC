#O calculo é executado dividindo o peso (em Kg) pela altura elevada ao quadrado (em metros.)

peso = float(input('informe o seu peso: '))
altura = float(input('informe sua altura: '))
imc = peso / (pow(altura, 2))

print(f'seu imc é {imc:.2f}')

if imc < 18.5:
    print('Abaixo do peso')
elif 18.5 <= imc < 24.9:
    print('Peso normal')
elif  25 <= imc < 29.9:
    print('Sobrepeso')
elif 30 <= imc < 34.9:
    print('Obesidade grau I')
elif 35 <= imc < 39.9:
    print('Obsidade grau II')
else:
    print('Obesidade grau III ou mórbida')