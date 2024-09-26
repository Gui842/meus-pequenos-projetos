class Gerenciamento_de_produto:
    def __init__(self,nome,quantidade,preco):
        self.nome=nome #nome do produto
        self.preco=preco #preço do produto
        self.quantidade=quantidade #quantidade
    def adiciobar_estoque(self):
        quantidade=int(input("deseja adicionar quantos ao estoque?:"))
        self.quantidade +=quantidade
        print(f"quantidade que foi adicionada:{quantidade}")
        print(f"a quantidade em estoque:{self.quantidade}")
    def remover_estoque(self):
        quantidade=int(input("deseja retirar quantos ?:"))
        self.quantidade -=quantidade
        print(f"quantidade tirada:{quantidade}")
        print(f"quantidade em estoque:{self.quantidade}")
    def exibir(self):
        print(f" nome do produto:{self.nome}")
        print(f"preço do produto:${self.preco}")
        print(f"quantidade em estoque:{self.quantidade}")
produto1=Gerenciamento_de_produto("sabao liquido",63,4.2) #nome,quantidade,valor
enter_loja=input("desja gerenciar os produtos?")

while enter_loja.lower()=="sim":
    print("digite 1:adicionar quantidade no estoque")
    print("digite 2: para remover uma certa quantidade no estoque")
    print("digite 3: para saber o nome,quantidade,e preço do produto")
    number=int(input("digite aqui:"))
    if number ==1:
        produto1.adiciobar_estoque()
    elif number ==2:
        produto1.remover_estoque()
    elif number ==3:
        produto1.exibir()
    else:
        print("error!")
        break
    
