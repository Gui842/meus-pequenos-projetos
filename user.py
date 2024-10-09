class user():
    lista_de_user=[] #lista que armazena usuarios
    def __init__(self,nome,idade): 
        self.nome=nome
        self.idade=idade
        self.senha=int
    def novo_user(self):
        print(f"ok senhor({self.nome}) vamos fazer seu cadrastro")
        senha=int(input("digite uma senha:"))
        confimação=int(input("digite outra vez:"))      #fazer cadastro e verificar se senha de confimação
        if confimação ==senha:                          
            print("está tudo certo") 
            print("agora sim")
            self.lista_de_user.append(self.nome)
            print(f"user:{self.nome} foi adicionado na lista de users :{self.lista_de_user}")
        else:
            print("erro!!") 
            while True:
                print("erro!!") 
                confimação=int(input("digite outra vez!!"))
                if confimação ==senha:
                    print("agora sim")
                    self.lista_de_user.append(self.nome)
                    print(f"user:{self.nome} foi adicionado na lista de users: {self.lista_de_user}")
                    break
                    
    def exibir(self):
        print(f" nome do user:{self.nome} / idade:{self.idade}")  #exibir nome e idade e a lista de user
        print(f"lista de user:{self.lista_de_user}")
    
    
    def remove(self):
        apagar=input("deseja apagar seu perfil?") 
        if apagar.lower() =="sim":                  #remover usuario da lista
            print("ok!")
            if self.nome in self.lista_de_user:
                self.lista_de_user.remove(self.nome)
                print("seu nome foi retirado da lista de user: ")
                print(f"lista de user:{self.lista_de_user}")
            else:
                print("seu nome não foi adicionado")
        else:
            print("que bom que resolveu ficar!")        
username=user("gui",19)
username.novo_user()
username0=user("pamella",19)
username0.novo_user()
