from classes import *
from time import sleep

#dicionários reservados para cada classe para efetuação das funções
dic_turmas={}
dic_materias = {}
dic_professores = {}
dic_alunos = {}


#Bloco de funções do Menu principal
def criar_aluno():
    """criar_aluno(None)-> None
    Cria um objeto do Aluno e adiciona ele no seu respectivo dicionário (dic_alunos)"""
    nome = input("Qual é o nome do aluno \n")
    dre = input("Qual é o DRE do aluno \n")
    dic_alunos[nome]= Aluno(nome,dre)
    print(f"Professor adicionado no sistema! \n Nome: {nome}\n")
    return None

def criar_prof():
    """criar_prof(None)-> None
    Cria um objeto do Professor e adiciona ele no seu respectivo dicionário (dic_professores)"""
    nome = input("Qual é o nome do professor\n")
    id = input("Qual é a identidade do professor\n")
    dic_professores[nome]= Professor(nome,id)
    print(f"Professor adicionado no sistema! \n Nome: {nome}\n")
    return None
          

def criar_mat():
    """criar_mat(None)-> None
    Cria um objeto da Matéria e adiciona ela no seu respectivo dicionário (dic_materias)"""
    nome = input("Qual é o nome da materia\n")
    codigo = input("Qual é o código da materia\n")
    dic_materias[nome]= Materia(nome,codigo)
    print(f"Matéria Adicionada no sistema! \n Nome da matéria: {nome} \n Código da matéria: {codigo} \n")
    return None

def mostra_mat():
    """mostra_mat(None)-> None
    Mostra todas as matérias cadastradas no sistema e oferece uma pausa de 0.5 segundos para facilitar a
    vizualização da lista."""
    if len(dic_materias) == 0:#Caso não esteja cadastrada nenhuma Matéria no sistema
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
    """mostra_prof(None)-> None
    Mostra todas as matérias cadastradas no sistema e oferece uma pausa de 0.5 segundos para facilitar a
    vizualização da lista."""
    if len(dic_professores) == 0:#Caso não esteja cadastrada nenhum Professor no sistema
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
    """mostra_alunos(None)-> None
    Mostra todas as matérias cadastradas no sistema e oferece uma pausa de 0.5 segundos para facilitar a
    vizualização da lista."""
    if len(dic_alunos) == 0:#Caso não esteja cadastrada nenhum Aluno no sistema
        print("Não há Alunos Cadastradas \n")
        return None
    print("Lista de Alunos:")
    for nome, aluno in dic_professores.items():
        dre = aluno.dre
        print(f'Nome:{nome} -- DRE:{dre}')
    print()
    sleep(0.5)
    return None

#Bloco de funções do Menu das Turmas