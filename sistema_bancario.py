menu = """
[1] Depositar
[2] Sacar
[3] Extrato
[4] Sair
=> """

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3


while True:

    opcao = input(menu)

    if opcao == "1":
        valor = (float(input("Digite o valor do depósito: ")))

        if valor > 0:
            saldo += valor
            extrato += f"Depósito: R$ {valor:.2f}\n"
    
        else:
            print("Valor inválido, digite um valor positivo.")

    elif opcao == "2":
        valor = (float(input("Digite o valor do saque: ")))
        saldo_insuficiente = valor > saldo
        limite_insuficiente = valor > limite
        saques_insuficientes = numero_saques > LIMITE_SAQUES

        if saldo_insuficiente:
            print("Você não tem saldo suficiente para este saque.")

        elif limite_insuficiente:
            print("Limite indisponível.")
        elif saques_insuficientes:
            print("Limite de saques excedido.")

        elif valor > 0:
            saldo -= valor
            extrato += f"Saque: R$ {valor:.2f}"
            numero_saques +=1
    

    
    elif opcao == "3":
        print("*********Extrato*********")
        print("-------------------------")
        print(extrato)
        print(f"Saldo: {saldo:.2f}")
        print("-------------------------")
       

    elif opcao == "4":
        break

    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")