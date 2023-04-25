peso = float(input())
altura = float(input())
imc = peso/(altura**2)

if imc < 20:
  print('Abaixo do peso.')
elif imc >= 20 and imc < 25:
  print('Normal.')
elif imc >= 25 and imc < 30:
  print('Excesso de peso.')
elif imc >= 30 and imc < 35:
  print('Obesidade.')
else:
  print('Obesidade mórbida.')
  