def exibir_menu():
    menu = """
    -------------menu-------------
    [1] Depositar
    [2] Sacar
    [3] Extrato
    [4] Nova Conta
    [5] Listar Contas
    [6] Novo usuário
    [0] Sair    
    => """
    return input(menu)

def depositar(saldo, valor, extrato):
    if valor > 0:
        saldo += valor
        extrato += f"Depósito: R$ {valor:.2f}\n"
        print(f"Depósito de {valor} realizado com sucesso!")
    else:
        print("Valor inválido!")

    return saldo, extrato

def sacar(saldo, valor, extrato, limite, numero_saques, limite_saques):
    saldo_insuficiente = valor > saldo
    limite_insuficiente = valor > limite
    saques_insuficientes = numero_saques >= limite_saques
    
    if saldo_insuficiente:
        print("Você não tem saldo suficiente para este saque.")

    elif limite_insuficiente:
        print("Limite indisponível.")
    elif saques_insuficientes:
        print("Limite de saques excedido.")

    elif valor > 0:
        saldo -= valor
        extrato += f"Saque: R$ {valor:.2f}\n"
        numero_saques += 1
        print(f"Saque de {valor} realizado com sucesso!")

    return saldo, extrato

def mostrar_extrato(saldo, extrato):
    print("*********Extrato*********")
    print("-------------------------")
    print(extrato if extrato else "Nenhuma movimentação realizada.")
    print(f"Saldo: R$ {saldo:.2f}")
    print("-------------------------")

def criar_conta(agencia, numero_conta, clientes):
    cpf = input("Informe o CPF do usuário: ")
    cliente = encontrar_cliente(cpf, clientes)

    if cliente:
        print("Conta criada com sucesso!")
        return {"agencia": agencia, "numero_conta": numero_conta, "cliente": cliente}
    
    print("Usuário não encontrado, programa encerrado!")
    return None

def listar_contas(contas):
    for conta in contas:
        registro = f"""
        Agência: {conta['agencia']}
        Conta corrente: {conta['numero_conta']}
        Titular: {conta['cliente']['nome']}
        """
        print(registro)

def criar_cliente(clientes):
    cpf = input("Informe o CPF (somente números): ")
    cliente = encontrar_cliente(cpf, clientes)

    if cliente:
        print("Você já é nosso cliente!")
        return

    nome = input("Informe o nome completo: ")
    data_nascimento = input("Informe a data de nascimento: ")
    endereco = input("Informe o endereço: ")

    clientes.append({"nome": nome, "data_nascimento": data_nascimento, "cpf": cpf, "endereco": endereco})
    print("Cliente cadastrado com sucesso!")

def encontrar_cliente(cpf, clientes):
    clientes_encontrados = [cliente for cliente in clientes if cliente["cpf"] == cpf]
    return clientes_encontrados[0] if clientes_encontrados else None

def main():
    LIMITE_SAQUES = 3
    agencia = "0001"
    saldo = 0
    limite = 500
    extrato = ""
    numero_saques = 0
    clientes = []
    contas = []

    while True:
        opcao = exibir_menu()

        if opcao == "1":
            valor = float(input("Digite o valor do depósito: "))
            saldo, extrato = depositar(saldo, valor, extrato)

        elif opcao == "2":
            valor = float(input("Informe o valor que gostaria de sacar: "))
            saldo, extrato = sacar(
                saldo=saldo,
                valor=valor,
                extrato=extrato,
                limite=limite,
                numero_saques=numero_saques,
                limite_saques=LIMITE_SAQUES,
            )
        
        elif opcao == "3":
            mostrar_extrato(saldo, extrato)

        elif opcao == "4":
            numero_conta = len(contas) + 1
            conta = criar_conta(agencia, numero_conta, clientes)
                
            if conta:
                contas.append(conta)

        elif opcao == "5":
            listar_contas(contas)

        elif opcao == "6":
            criar_cliente(clientes)

        elif opcao == "0":
            break
            
        else:
            print("Por favor, escolha uma opção válida.")

main()
