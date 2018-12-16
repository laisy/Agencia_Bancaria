import os.path
import os
def criarConta():
    cpf = raw_input('Digite o CPF do cliente: \n')
    try:
         with open('%s.txt' %cpf, 'r') as f:
            print "Esse CPF ja possui uma conta! \n"
    except IOError:
         saldoInicial = raw_input('Digite o saldo inicial da conta: \n')
         arq = open('%s.txt' %cpf, 'w')
         arq.write(str(saldoInicial+'\n'))
         arq.close()
         print "Conta criada com Sucesso! \n"

def encerrarConta():
    cpf = raw_input('Digite o CPF do cliente que deseja Encerrar a conta: \n')
    try:
        with open('%s.txt' %cpf, 'r') as f:
            print 'Ok'
        os.remove('%s.txt' %cpf)
        print "Conta Encerrada! \n"
    except IOError:
        print 'Conta nao Encontrada! \n'

def escreverValor(valor):
    arq = open('%s.txt' %cpf, 'a')
    arq.write(str(valor))
    arq.close()

def lerSaldo():
    arq = open('%s.txt' %cpf, 'r')
    saldo = 0
    firstLine = True
    for linha in arq:
        if firstLine:
            saldo = float(linha)
            firstLine = False
        else:
            operacao = linha[0:1]
            if str(operacao)=='s':
                valor = float(linha[2:len(linha)-1])
                saldo -= valor
            elif str(operacao)=='d':
                valor = float(linha[2:len(linha)-1])
                saldo += valor
            if str(operacao)=='D':
                valor = float(linha[2:len(linha)-1])
                saldo -= valor
            elif str(operacao)=='C':
                valor = float(linha[2:len(linha)-1])
                saldo += valor
    arq.close()
    return saldo

def saldo():
    saldo = lerSaldo()
    print 'O saldo da conta : '+str(saldo)

def deposito():
    print 'Digite o valor a ser depositado: \n'
    valor = float(raw_input())
    arq = open('%s.txt' %cpf, 'a')
    arq.write(str('d ' +str(valor)+'\n'))
    arq.close()

def saque():
    print 'Digite o valor do saque: \n'
    valor = float(raw_input())
    escreverValor('s ' +str(valor)+'\n')

def transferencia():
    arq = open('%s.txt' %cpf, 'a')
    valor = raw_input('Digite o valor a ser transferido: \n')
    arq.write(str('D ' +str(valor)+'\n'))
    arq.close()
    cpf2 = raw_input('Digite o CPF do cliente que recebera a transferencia: \n')
    if cpf == cpf2:
        print "Nao e permitido fazer transferencia para a mesma Conta! \n"
    else:
        try:
            with open('%s.txt' %cpf2, 'r') as f:
                f.close()
                arq = open('%s.txt' %cpf2, 'a')
                arq.write(str('C ' +str(valor)+'\n'))
                arq.close()
                print "Trasnferencia ocorreu com sucesso! \n"
        except IOError:
            print "Esse CPF ainda nao possui Conta! \n"

def extrato():
    n = int(raw_input("Digite a partir de quantos lancamentos deseja ter o extrato: \n"))
    with open('%s.txt' %cpf, 'r') as arq:
        for linha in arq:
            print linha

def mediaC():
    medC = i = 0.0
    arq = open('%s.txt' %cpf, 'r')
    firstLine = True
    for linha in arq:
        if firstLine:
            firstLine = False
        else:
            operacao = linha[0:1]
            if str(operacao)=='C':
                valor = float(linha[2:len(linha)-1])
                medC += valor
                i += 1
    arq.close()
    if i == 0:
        print "Nao existe Creditos na Conta! "
    else:
        mediC = medC/i
        print "Media dos Creditos: ", mediC

def mediaD():
    medD = j = 0.0
    arq = open('%s.txt' %cpf, 'r')
    firstLine = True
    for linha in arq:
        if firstLine:
            firstLine = False
        else:
            operacao = linha[0:1]
            if str(operacao)=='D':
                valor = float(linha[2:len(linha)-1])
                medD += valor
                j += 1
    arq.close()
    if j == 0:
        print "Nao existe Debitos na Conta!"
    else:
        mediD = medD/j
        print "Media dos Debitos: ", mediD

def printMenu():
    print ('Digite 1 Para Criar Nova Conta\n')
    print ('Digite 2 Para Encerrar Conta\n')
    print ('Digite 3 Para Operacoes em Conta\n')
    print ('Digite 4 Para Encerrar\n')
    opcao = int(raw_input())
    return opcao

def subMenu():
    print ('Digite 1 Para Efetuar um Deposito\n')
    print ('Digite 2 Para Efetuar um Saque\n')
    print ('Digite 3 Para Saber o Saldo\n')
    print ('Digite 4 Para Fazer uma Transferencia\n')
    print ('Digite 5 Para Ver o Extrato da Conta\n')
    print ('Digite 6 Para Ver a Media dos Creditos\n')
    print ('Digite 7 Para Ver a Media dos Debitos\n')
    print ('Digite 8 Para Retornar Menu\n')
    print ('Digite 9 Para Encerrar\n')
    op2 = int(raw_input())
    while(op2 != 9):
        if op2 == 1:
            deposito()
        if op2 == 2:
            saque()
        if op2 == 3:
            saldo()
        if op2 == 4:
            transferencia()
        if op2 == 5:
            extrato()
        if op2 == 6:
            mediaC()
        if op2 == 7:
            mediaD()
        if op2 == 8:
            return
        op2 = int(raw_input('Digite uma opcao do subMenu: '))
    print ('Volte Sempre')
    exit(0)

print ('Bem Vindo ao Banco UAG \n')
op = printMenu()
while (op != 4):
    if op == 1:
        criarConta()
    if op == 2:
        encerrarConta()
    if op == 3:
        cpf = raw_input('Digite o CPF do cliente: \n')
        try:
            with open('%s.txt' %cpf, 'r') as f:
                subMenu()
        except IOError:
             print "Esse CPF ainda nao possui Conta! \n"

    op = printMenu()

print ('Volte Sempre')
