valor = int(input())

c50 = valor // 50
valor %= 50
c10 = valor // 10

print(f'{c50} notas de R$ 50,00')
print(f'{c10} notas de R$ 10,00')