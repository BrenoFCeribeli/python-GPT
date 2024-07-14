print("Calculadora Simples")
print("Operações disponíveis:")
print("+ para Adição")
print("- para Subtração")
print("* para Multiplicação")
print("/ para Divisão")

operacao = input("Escolha a operação (+, -, *, /): ")

num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))

if operacao == '+':
    resultado = num1 + num2
    print(f"{num1} + {num2} = {resultado}")
elif operacao == '-':
    resultado = num1 - num2
    print(f"{num1} - {num2} = {resultado}")
elif operacao == '*':
    resultado = num1 * num2
    print(f"{num1} * {num2} = {resultado}")
elif operacao == '/':
    if num2 != 0:
        resultado = num1 / num2
        print(f"{num1} / {num2} = {resultado}")
    else:
        print("Erro: divisão por zero")
else:
    print("Operação inválida. Por favor, escolha uma operação válida.")
