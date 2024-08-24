class Conta_bancaria():
    def __init__(self,titular,saldo):
        self.titular=titular
        self.saldo=saldo
    def exibir(self):
        print("senh(a)r", self.titular ,"seu saldo é",self.saldo)
    def adicionar(self,valor):
        self.saldo += valor
        print("$",self.saldo)
    def sacar(self,valor):
        if self.saldo ==0:
            print("saldo insuficiente")
        else:
            self.saldo -= valor
            print("$",self.saldo )
            

cliente=Conta_bancaria("jhon",600)
clientes=input("quer entrar em sua conta bancaria?(sim/não):")
while cliente !="":
    if clientes=="sim":
        opcao=int(input(" digite 1:exibir seu nome e seu saldo, digite 2:para adicionar saldo em sua conta, digite 3 para sacar seu saldo,4 sair da conta:"))
        if opcao==1:
            cliente.exibir()
        elif opcao ==2:
            valor=int(input("digite um valor depositar:$"))
            cliente.adicionar(valor)
        elif opcao==3:
            valor=int(input("digite um valor para sacar:$"))
            cliente.sacar(valor)
            
        else:
            print("carregando...." )
            print("saindo....")
            print ("pronto!")
            break
