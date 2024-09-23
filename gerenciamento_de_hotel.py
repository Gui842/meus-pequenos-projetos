class hotel():
    def __init__(self,nome,nome_hospede,idade):
        self.nome=nome #nome do hotel
        self.nome_hospede=nome_hospede #nome do hóspede
        self.quartos=20 #numero de quartos no hotel
        self.reservas=[] #listas de pessoas que estão reservando um quarto
        self.hospedes=[] #lista de pessoa que ja são hóspedes
        self.idade=idade
    def reserva(self):
        self.reservas = []
        if self. quartos >0:
            pergunta1=input("olá bem vindo ao nosso hotel,queres fazer uma reserva?")
            if pergunta1.lower() =="sim":
                self.hospedes.append(self.nome_hospede)
                self.quartos -=1
                print(f"o hóspede {self.nome_hospede} foi adicionado com sucesso a lista de hospede")
                print(f"a quantidade de quartos {self.quartos}")
            else:
                print("reserva não realizada")
        else:
            print("desculpa o hotel está fechado!!")
    def cancelamento(self):
        if self.nome_hospede in self.hospedes:
            self.hospedes.remove(self.nome_hospede)
            self.quartos =+1
            print(f"o hóspede {self.nome_hospede} foi removido com sucesso")
            print(f"quatidade de quartos: {self.quartos}")
        else:
            print(f" o hóspede:{self.nome} não foi encontrado nas reservas" )
    def status(self):
        print(f"nome do hóspede:{self.nome_hospede}")
        print(f"idade do hóspede:{self.idade}")
        print(f"nome do hotel:{self.nome}")
        print(f"lista de hóspedes: {self.hospedes}")
        print(f"quantidade de quartos:{self.quartos}")

user0=hotel("hazbin hotel","gui",19)
bem_vindo=input("olá bem vindo !queres entrar em nosso hotel?")
while bem_vindo.lower()=="sim":
    print("digite 1: para  reserva um quartos")
    print("digite 2:para cancelar uma reserva")
    print("digite 3 para  ver seus status e status do hotel")
    number=int(input("digite aqui:"))
    if number ==1:
        user0.reserva()
    elif number ==2:
        user0.cancelamento()
    elif number ==3:
        user0.status()
    else:
        print("numero invalido!")
        print("carregando...")
        print("saindo..")
        break
