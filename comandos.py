from classes import *
from time import sleep

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
    if len(dic_materias) == 0:
        print("Não há Matérias Cadastradas \n")
        return None
    print("Lista de Matérias:")
    for nome,materia in dic_materias.items():
        codigo = materia.codigo
        print(f'Matéria:{nome} -- Código:{codigo}')
    print()
    sleep(0.5)
    return None

def mostra_prof():
    if len(dic_professores) == 0:
        print("Não há Professores Cadastradas \n")
        return None
    print("Lista de Professores:")
    for nome, prof in dic_professores.items():
        id = prof.id
        print(f'Nome:{nome} -- Identidade:{id}')
    print()
    sleep(0.5)
    return None

def mostra_alunos():
    if len(dic_alunos) == 0:
        print("Não há Alunos Cadastradas \n")
        return None
    print("Lista de Alunos:")
    for nome, aluno in dic_professores.items():
        dre = aluno.dre
        print(f'Nome:{nome} -- DRE:{dre}')
    print()
    sleep(0.5)
    return None