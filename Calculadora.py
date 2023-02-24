escolha = int(input("Escolha a operação: 1-soma 2-subtração 3-multiplicação 4-divisão"))

v1 = int(input("Digite o primeiro valor: "))
v2 = int(input("Digite o segundo valor: "))

if escolha == 1:
    print(f"{v1} + {v2} = {v1+v2}")
elif escolha == 2:
    print(f"{v1} - {v2} = {v1-v2}")
elif escolha == 3:
    print(f"{v1} * {v2} = {v1*v2}")
elif escolha == 4:
    print(f"{v1} / {v2} = {v1/v2}")
else:
    print("Operador inválido. Rodo o código novamente")
