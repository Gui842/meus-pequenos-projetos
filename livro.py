class livro():
    def __init__(self,ano,pagina,autor,nome):
        self.ano=ano                        #atributos da classe
        self.pagina=pagina
        self.autor=autor
        self.nome=nome
    def exibir(self):
        print(f"PG:{self.pagina} ")  #exibir os atributos
        print(f"nome do autor:{self.autor}")
        print(f"ano lançado:{self.ano}")
    def marca_como_concluido(self):
        pergunta1 = input("Você já leu esse livro? (sim/não): ").strip().lower()
        if pergunta1 == "sim":
            self.leitura_concluida = True         
            print("Leitura concluída marcada.")
        else:
            self.leitura_concluida = False
            print("Continue lendo!")

            print("continue lendo!")
    def leitura(self):
        ler=input(f"deseja começa a ler:{self.nome}")
        while ler =="sim":
            ler2=input("deseja continuar lendo?")
            if ler2 =="sim":
                self.pagina -=1
                print(f"pagina Restante {self.pagina}")
                if self.pagina ==0:
                    print("terminou o livro")
                    break
            else:
                print("ok")
    def leitura_concluida(self):
        if self.pagina ==0:
            print("leitura concluida!")
        else:
            print(f"{self.pagina}s restantes")
            
livros=livro(2005,4,"gui","DESAPARECIMENTO DE GUI")
livros.exibir()
livros.leitura()

