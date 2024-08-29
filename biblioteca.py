class Biblioteca():
    def __init__(self):
        self.livro=["Duna: de Frank Herbert,Sapiens: Uma Breve História da Humanidade de Yuval Noah Harari,"  #nome dos livro
                    "Autoajuda: Autoajuda: Hábitos Atômicos de James Clear"]
    def add(self):
        livro=[]
        livro=input("digite o nome do livro e o autor:")    #adicionar novos livros
        livro=self.livro.append(livro)
        print(f"{self.livro} foi adicionado com sucesso")
    def Remover(self):
       livro_remover=input("digite um livro que queira remover")
       if livro_remover in self.livro:                          #remover livros usando estrutura de controle if/else(condicionais)
           self.livro.remove(livro_remover)
           print("removido com sucesso!")
           len(self.livro)
       else:
           print("não encontrado")      #caso o nome não seja encontrado
    def exibir(self):
        len(self.livro)               #livros no estoque
      print(self.livro)
pergunta_usuario=input("deseja entra na biblioteca?")     #pergunta se o usuario quer entrar na biblioteca
 
while pergunta_usuario =="sim": #inicar o laço se a pergunta for igual a sim
    fazer=int(input("oque queres fazer ? digite 1 para adicionar novos livros, 2 para remover um livro e 3 para exibir os livros,mais de 3:sai da biblioteca" )) #quais são as opção que o usuario pode fazer na biblioteca
    livro=Biblioteca()   # a Classe com uma variavel
    if fazer==1:
        
        livro.add()
    elif fazer  ==2:           #estrutura de controle condicionais(if/elif/else)
        livro.Remover()
    elif fazer ==3:
       livro.exibir()
    else:
        print("carregando...)
        print("saindo...")
        print("pronto)
        break # cancelar o laço de repetição
