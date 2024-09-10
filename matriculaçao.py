lista_alunos=["Ana","Bea","Maria","Anderson","Fernado"]
alunos_novos=[]
opcao=int(input("digite 1: para se matricular , e 2 para um verificação de nome:"))
if opcao ==1:
    alunos_novos=input("digite seu name:")
    alunos_novos=lista_alunos.append(alunos_novos)
    print(lista_alunos)
elif opcao==2:
    if alunos_novos==alunos_novos:
        print("nome matriculado!")
    else:
        print("nome inexistente")
