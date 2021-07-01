from classes import *
from time import sleep

#inputs inválidos ao sistema como medida de preucaução
inp_inv = ("", " ")

#dicionários reservados para cada classe para efetuação das funções
dic_turmas={}
dic_materias = {}
dic_professores = {}
dic_alunos = {}

#Bloco de funções do Menu principal
def criar_aluno():
    """criar_aluno(None)-> None
    Cria um objeto do Aluno e adiciona ele no seu respectivo dicionário (dic_alunos)"""
    
    #Verificação de possíveis erros nos inputs
    while True:
        try:
            nome = input("Qual é o Nome do Aluno \n")
            dre = input("Qual é o DRE do Aluno \n")
            if nome in inp_inv or dre in inp_inv: raise Exception
            if dre in dic_alunos.keys():raise ValueError
            break
        except ValueError: print("Esse DRE já Existe no Sistema! Tente Novamente")
        except Exception: print("Nome ou DRE Inválidos! Tente Novamente \n")
    #criação do objeto
    dic_alunos[dre]= Aluno(nome,dre)
    print(f"Aluno Adicionado no Sistema! \n Nome: {nome}\n DRE: {dre} \n")
    return None

def criar_prof():
    """criar_prof(None)-> None
    Cria um objeto do Professor e adiciona ele no seu respectivo dicionário (dic_professores)"""
    
    #Verificação de possíveis erros nos inputs
    while True:
        try:
            nome = input("Qual é o Nome do Professor\n")
            id = input("Qual é o ID do Professor\n")
            if nome in inp_inv or id in inp_inv: raise Exception
            if id in dic_professores.keys():raise ValueError
            break
        except ValueError: print("Esse ID já Existe no Sistema! Tente Novamente")
        except Exception: print("Nome ou Identidade Inválidos! Tente Novamente")
    #criação do objeto
    dic_professores[id]= Professor(nome,id)
    print(f"Professor Adicionado no Sistema! \n Nome: {nome}\n ID: {id} \n")
    return None
          
def criar_mat():
    """criar_mat(None)-> None
    Cria um objeto da Matéria e adiciona ela no seu respectivo dicionário (dic_materias_n e dic_materias)"""
    
    #Verificação de possíveis erros nos inputs
    while True:
        try:
            nome = input("Qual é o Nome da Materia\n")
            codigo = input("Qual é o Código da Materia\n")
            if (nome in inp_inv or codigo in inp_inv): raise Exception
            if (codigo in dic_materias.keys()): raise ValueError
            break
        except ValueError: print("Código da Matéria já Existente no Sistema! Tente Novamente")
        except Exception: print("Nome ou Código Inválidos! Tente Novamente")
    #criação do objeto
    dic_materias[codigo]= Materia(nome,codigo)
    print(f"Matéria Adicionada no Sistema! \n Nome da Matéria: {nome} \n Código da Matéria: {codigo} \n")
    return None

def mostra_mat():
    """mostra_mat(None)-> None
    Mostra todas as matérias cadastradas no sistema e oferece uma pausa de 0.5 segundos para facilitar a
    vizualização da lista."""

    #Caso não esteja cadastrada nenhuma Matéria no sistema
    if len(dic_materias) == 0:
        print("Não há Matérias Cadastradas \n")
        return None
    print("Lista de Matérias:")
    for codigo,materia in dic_materias.items():
        nome = materia.nome
        print(f'Matéria:{nome} -- Código:{codigo}')
    print()
    sleep(0.5)
    return None

def mostra_prof():
    """mostra_prof(None)-> None
    Mostra todas as matérias cadastradas no sistema e oferece uma pausa de 0.5 segundos para facilitar a
    vizualização da lista."""

    #Caso não esteja cadastrado nenhum Professor no sistema
    if len(dic_professores) == 0:
        print("Não há Professores Cadastrados \n")
        return None
    print("Lista de Professores:")
    for id, prof in dic_professores.items():
        nome = prof.nome
        print(f'Nome:{nome} -- Identidade:{id}')
    print()
    sleep(0.5)
    return None

def mostra_alunos():
    """mostra_alunos(None)-> None
    Mostra todas as matérias cadastradas no sistema e oferece uma pausa de 0.5 segundos para facilitar a
    vizualização da lista."""

    #Caso não esteja cadastrado nenhum Aluno no sistema
    if len(dic_alunos) == 0:
        print("Não há Alunos Cadastrados \n")
        return None
    print("Lista de Alunos:")
    for dre, aluno in dic_alunos.items():
        nome = aluno.nome
        print(f'Nome:{nome} -- DRE:{dre}')
    print()
    sleep(0.5)
    return None

#Bloco de funções do Menu das Turmas
def criar_turma():
    """criar_turma(None)-> None
    Cria um objeto da Turma e adiciona ela no seu respectivo dicionário (dic_turmas)"""
    
    #Verificação de possíveis erros nos inputs do nome e da matéria da turma
    while True:
        try:
            nome = input("Qual é o nome da Turma\n")
            mat = input("Qual é o código da Matéria da Turma\n")
            if mat not in dic_materias.keys(): raise TypeError
            if (nome in inp_inv) or (mat in inp_inv): raise Exception
            break
        except TypeError: print("Matéria Inexistente no Sistema. Tente Novamente\n")
        except Exception: print("Nome ou Matéria Inválidos. Tente Novamente\n")
    #criação do objeto
    dic_turmas[nome]= Turma(nome,mat)
    print(f"Turma Inserida no Sistema! \nNome: {nome} \nMatéria: {dic_materias[mat].nome} \nCódigo da Matéria: {mat}\n")
    return None


def prof_turma():

    #Verificação de possíveis erros nos inputs do ID do professor
    while True:
        try:
            prof = input("Qual é o ID do Professor?")
            if prof in inp_inv: raise Exception
            if prof not in dic_professores.keys(): raise ValueError
            break
        except ValueError: print("Nome Inexistente no Sistema! Tente Novamente\n")
        except Exception: print("Nome Inválido! Tente Novamente \n")

    #Verificação de possíveis erros nos inputs do nome da turma
    while True:
        try:
            turma = input("Qual é o nome da Turma?")
            if turma in inp_inv: raise Exception
            if turma not in dic_turmas.keys(): raise ValueError
            break
        except ValueError: print("Nome Inexistente no Sistema! Tente Novamente\n")
        except Exception: print("Nome Inválido! Tente Novamente \n")
    prof = dic_professores[prof]
    dic_turmas[turma].add_prof(prof)
    return None