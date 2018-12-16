import os.path
import os

def criarConta():
    cpf = raw_input('Digite o CPF do cliente: \n')
    try:
         with open('%s.txt' %cpf, 'r') as f:
            print "Esse CPF ja possui uma conta! \n"
            printMenu()
    except IOError:
         saldoInicial = raw_input('Digite o saldo inicial da conta: \n')
         arq = open('%s.txt' %cpf, 'w')
         arq.write(str(saldoInicial+'\n'))
         arq.close()
         print "Conta criada com Sucesso! \n"
         printMenu()

def encerrarConta():
    cpf = raw_input('Digite o CPF do cliente que deseja Encerrar a conta: \n')
    try:
        with open('%s.txt' %cpf, 'r') as f:
            print 'Ok'
        os.remove('%s.txt' %cpf)
        print "Conta Encerrada! \n"
        printMenu()
    except IOError:
        print 'Conta nao Encontrada! \n'
        printMenu()

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
                medD = valor
                i += 1
            elif str(operacao)=='C':
                valor = float(linha[2:len(linha)-1])
                saldo += valor
                medC = valor
                j += 1
    arq.close()
    return saldo

def deposito():
    print 'Digite o valor a ser depositado: \n'
    valor = float(raw_input())
    arq = open('%s.txt' %cpf, 'a')
    arq.write(str('d ' +str(valor)+'\n'))
    arq.close()
    subMenu()

def saque():
    print 'Digite o valor do saque: \n'
    valor = float(raw_input())
    escreverValor('s ' +str(valor)+'\n')
    subMenu()

def transferencia():
    arq = open('%s.txt' %cpf, 'a')
    valor = raw_input('Digite o valor a ser transferido: \n')
    arq.write(str('D ' +str(valor)+'\n'))
    arq.close()
    cpf2 = raw_input('Digite o CPF do cliente que recebera a transferencia: \n')
    if cpf == cpf2:
        print "Nao e permitido fazer transferencia para a mesma Conta! \n"
        printMenu()
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
            printMenu()

def extrato():
    n = int(raw_input("Digite a partir de quantos lancamentos deseja ter o extrato: \n"))
    with open('%s.txt' %cpf, 'r') as arq:
        for linha in arq:
            print linha

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
    opcao2 = int(raw_input())
    return opcao2

medD = 0
medC = 0
j = 0
i = 0
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
             printMenu()

op2 = subMenu()
while(op2 != 9):
    if op2 == 1:
        deposito()
    if op2 == 2:
        saque()
    if op2 == 3:
        saldo = lerSaldo()
        print 'O saldo da conta : '+str(saldo)
    if op2 == 4:
        transferencia()
    if op2 == 5:
        extrato()
    if op2 == 6:
        o = medC/j
        if o != 0:
            print "Media dos Creditos: ", o
        else:
            print "Nao existe creditos na conta! "
    if op2 == 7:
        m = medD/i
        if m != 0:
            print "Media de Debitos: ", m
        else:
            print "Nao existe debitos na conta! "
    if op2 == 8:
        printMenu()

print ('Volte Sempre')
