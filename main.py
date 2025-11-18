import time 
def menu():
    menu = """

    [1] Criar usuario
    [2] criar conta
    [3] Listar clientes
    [4] Listar contas
    [5] Depositar
    [6] Sacar
    [7] Extrato
    [8] Excluir conta
    [0] Sair

    
    => """   
    print(menu)

def criar_cliente(Clientes):
    
    while True:
        nome = input('Digite seu nome: ')
        data_nascimento = input('Data de nascimento: ')
        cpf = input('Digite seu cpf(xxx.xxx.xxx-xx):')
        esconder_cpf = cpf[:3]
        esconder_cpf2 = '.***.***-xx'
        endereco = input('Endereço: logadouro, nro - bairro - cidade/sigla: ')
        Clientes.append({'nome': nome, 'data de nascimento': data_nascimento, 'cpf': cpf, 'endereco': endereco})
    
        print(f'Cliente: {nome}, com cpf: {esconder_cpf + esconder_cpf2} criado com sucesso!')
        
        criar_novo_user = input("Deseja cadastrar outro usuário? (s/n): ")
        if criar_novo_user.lower() != "s":
            break
    
def verificar_clientes(Clientes):
    print('Procurando clientes...')
    time.sleep(2)
    if Clientes:
        print('clientes:')
        for cliente in Clientes:
            print(cliente)
    else:
        print('Nenhum cliente cadastrato ')

def listar_contas(contas):
    print('Acessando contas...')
    time.sleep(2)
    if contas:
        print('contas:')
        for conta in contas:
            print(conta)
    else:
        print('Nenhuma conta encontrada!')

def criar_conta(Clientes, contas, agencia):
    
    numero_conta = 0
    while True:
        cpf = input('Digite o cpf que deseja criar a conta: ')
        cliente = next((c for c in Clientes if c["cpf"] == cpf), None)
        
        if cliente is None:
            print('cpf nao encontrado! Verifique o cpf, ou crie um usuario')
            break
        else:
            numero_conta +=1 
            nome_cliente = cliente["nome"]
            contas.append({'cliente': nome_cliente, 'agencia': agencia, 'numero_conta': numero_conta})
            print(f'Conta criado com sucesso: Usuario: {nome_cliente}, Agencia: {agencia}, numero da conta: {numero_conta} ')
           
    
        
        criar_nova_conta = input("Deseja criar outra conta? (s/n): ")
        if criar_nova_conta.lower() != "s":
            break

def excluir_conta(contas):
    number_conta = input('Digite o numero da conta que deseja excluir: ')
    conta = next((c for c in contas if c['numero_conta'] == int(number_conta)), None)
    
    if conta is None:
        print('Conta não encontrada, Tente novamente! ')
        return
    
    print(f'Conta encontrada: {conta}')
    confirmacao = input('Deseja excluir ? (s/n)')
    
    if confirmacao != 's':
        print('Operação cancelada...')
        return
       
    contas.remove(conta)
    print('Conta excluida com sucesso.')

def depositar(saldo, extrato):
    
    valor = float(input("Informe o valor do depósito: "))

    if valor > 0:
        saldo += valor
        extrato += f"Depósito: R$ {valor:.2f}\n"
        print(f'======== DEPOSITO De {valor} REALIZADO COM SUCESSO! ==================')
    else:
        print("Operação falhou! O valor informado é inválido.")
    return saldo, extrato

def saque(saldo, extrato, valor, limite, numero_saques, limite_saques):


   

    excedeu_saldo = valor > saldo

    excedeu_limite = valor > limite

    excedeu_saques = numero_saques >= limite_saques

    if excedeu_saldo:
        print("Operação falhou! Você não tem saldo suficiente.")

    elif excedeu_limite:
        print("Operação falhou! O valor do saque excede o limite.")

    elif excedeu_saques:
        print("Operação falhou! Número máximo de saques excedido.")

    elif valor > 0:
        saldo -= valor
        extrato += f"Saque: R$ {valor:.2f}\n"
        numero_saques += 1
        print(f'Saque no valor de {valor} bem sucedido')

    else:
        print("Operação falhou! O valor informado é inválido.")
    return saldo, extrato

def Extrato(extrato,  saldo):

    print("\n================ EXTRATO ================")
    print("Não foram realizadas movimentações." if not extrato else extrato)
    print(f"\nSaldo: R$ {saldo:.2f}")
    print("==========================================")
    
def main():
    numero_saques = 0
    LIMITE_SAQUES = 3


    agencia = '0001'
    Clientes = []
    contas = []
    saldo = 0
    limite = 500
    extrato = ""

    while True:
        menu()
        opcao = input('Esolha uma opção: ') 
        if opcao == '1':
            criar_cliente(Clientes)
        elif opcao == '2':
            criar_conta(Clientes, contas, agencia)
        elif opcao == '3':
            verificar_clientes(Clientes)      
        elif opcao == '4':
            listar_contas(contas)      
        elif opcao == '5':
            saldo, extrato = depositar(saldo, extrato)      
        elif opcao == '6':
            valor = float(input("Informe o valor do saque: "))

            saldo, extrato = saque(
                saldo=saldo,
                valor=valor,
                extrato=extrato,
                limite=limite,
                numero_saques=numero_saques,
                limite_saques=LIMITE_SAQUES,
            )           
        elif opcao == '7':
            Extrato(extrato, saldo)
        elif opcao == '8':
            excluir_conta(contas)
        elif opcao == '0':
            print("Saindo...")
            break

main()