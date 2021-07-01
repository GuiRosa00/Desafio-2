from classes import *
dic_turmas={}
dic_materias = {}
dic_professores = {}
dic_alunos = {}

def adicionar_aluno():
    nome = input("Qual é o nome do aluno \n")
    dre = input("Qual é o DRE do aluno \n")
    dic_alunos[nome]= Aluno(nome,dre)
    print(f"Professor adicionado no sistema! \n Nome: {nome}\n")
    return None


def adicionar_prof():
    nome = input("Qual é o nome do professor\n")
    id = input("Qual é a identidade do professor\n")
    dic_professores[nome]= Professor(nome,id)
    print(f"Professor adicionado no sistema! \n Nome: {nome}\n")
    return None
          

def adicionar_mat():
    nome = input("Qual é o nome da materia\n")
    codigo = input("Qual é o código da materia\n")
    dic_materias[nome]= Materia(nome,codigo)
    print(f"Matéria Adicionada no sistema! \n Nome da matéria: {nome} \n Código da matéria: {codigo} \n")
    return None

def mostra_mat():
    print("Lista de Matérias:")
    for nome,materia in dic_materias.items():
        codigo = materia.codigo
        print(f'{nome} -- {codigo}')
    return None

def mostra_prof():
    print("Lista de Professores:")
    for nome, prof in dic_professores.items():
        id = prof.id
        print(f'{nome} -- {id}')
    return None

def mostra_alunos():
    print("Lista de Alunos:")
    for nome, aluno in dic_professores.items():
        dre = aluno.dre
        print(f'{nome} -- {dre}')
    return None