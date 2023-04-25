# Menu
print("{:^45}".format("OPERAÇÕES MATEMÁTICAS"))
print("Menu:")
print("1 - soma")
print("2 - subtração")
print("3 - multiplicação")
print("4 - divisão", end="\n\n")
print("="*40)

# Entrada da operação 
operacao = input("Digite o número da operação desejada: ")

# Validação da operação 
while not operacao.isdecimal() or int(operacao) < 0 or int(operacao) > 4:
    print("!ERRO: OPÇÃO INVÁLIDA!", end="\n\n")
    operacao = input("Digite o número da operação desejada: ")

# Função para verificação de número
def isNumber(n):
    try:
        float(n)
    except ValueError:
        return False
    return True

# Entrada do primeiro operando
n1 = input("Digite o primeiro operando: ")

# Validação do primeiro operando
while not isNumber(n1):
    print("!ERRO: OPERANDO INVÁLIDO!", end="\n\n")
    n1 = input("Digite o primeiro operando: ")

n1 = int(n1) if n1.isdigit() else float(n1)

# Entrada do segundo operando
n2 = input("Digite o segundo operando: ")

# Validacao do segundo operando 
while not isNumber(n2):
    print("!ERRO: OPERANDO INVÁLIDO!", end="\n\n")
    n2 = input("Digite o segundo operando: ")

n2 = int(n2) if n2.isdigit() else float(n2)

print("="*40, end="\n\n")


# Operações 
if operacao == '1':
    print("SOMA:")
    print("{} + {} = {}".format(n1, n2, (n1 + n2)))
elif operacao == '2':
    print("SUBTRAÇÃO:")
    print("{} - {} = {}".format(n1, n2, (n1 - n2)))
elif operacao == '3':
    print("MULTIPLICAÇÃO:")


    # Formata o resultado, caso seja de ponto flutuante
    resultado = n1*n2 if str(n1).isdigit() and str(n2).isdigit() else '{:.2f}'.format(n1*n2)


    print("{} * {} = {}".format(n1, n2, resultado))
else:
    print("DIVISÃO:")

    # Formata o resultado, caso seja de ponto flutuante
    resultado = int(n1/n2) if not n1%n2 else '{:.2f}'.format(n1/n2)
    igualdade = "="

    if len(str(n1/n2).split('.')[1]) > 2:
        igualdade = "≈"
    
    print("{} / {} {} {}".format(n1, n2, igualdade, resultado))

print()