class Aluno():
    def __init__(self,nome,nota1,nota2):
        self.nome=nome
        self.nota1=nota1
        self.nota2=nota2   
    def calcular(self):
       if self.nota1 + self.nota2 /2 >=7:
            print(f"{self.nome},sua primeira nota é {self.nota1} sua segunda é {self.nota2}/////PASSOU!!")
       else:
            print(f"{self.nome},sua primeira nota é {self.nota1} sua segunda é {self.nota2},por tanto REPROVADO!")
   
aluno=Aluno("gui",2,9)
aluno.calcular()
aluno0=Aluno("alice",6,7)
aluno0.calcular()
