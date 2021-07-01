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
    dic_turmas[nome]= Turma(nome,dic_materias[mat])
    print(f"Turma Inserida no Sistema! \nNome: {nome} \nMatéria: {dic_materias[mat].nome} \nCódigo da Matéria: {mat}\n")
    return None

def procura_turma():
    while True:
        try:
            turma = input("Qual é o nome da Turma?\n")
            if turma in inp_inv: raise Exception
            if turma not in dic_turmas.keys(): raise ValueError
            break
        except ValueError: print("Nome Inexistente no Sistema! Tente Novamente\n")
        except Exception: print("Nome Inválido! Tente Novamente \n")
    return dic_turmas[turma]

def prof_turma():
    """Designa um professor à sala"""
    turma = procura_turma()
    #Verificação de possíveis erros nos inputs do ID do professor
    while True:
        try:
            prof = input("Qual é o ID do Professor?")
            if prof in inp_inv: raise Exception
            if prof not in dic_professores.keys(): raise ValueError
            break
        except ValueError: print("ID Inexistente no Sistema! Tente Novamente\n")
        except Exception: print("ID Inválido! Tente Novamente \n")
    prof = dic_professores[prof]
    turma.add_prof(prof)
    return None

def add_aluno(turma):
    """Adiciona 1 único aluno a uma sala."""
    #Verificação de possíveis erros nos inputs no número de alunos
    while True:
        try:
            dre = input("Qual é o DRE do Aluno?\n")
            if dre in inp_inv: raise Exception
            if dre not in dic_alunos.keys(): raise ValueError
            break
        except ValueError: print("DRE Inexistente no Sistema! Tente Novamente\n")
        except Exception: print("DRE Inválido! Tente Novamente \n")
    return turma.add_aluno(dic_alunos[dre])

def add_alunos_turma():
    """Adiciona vários alunos a uma sala"""
    turma = procura_turma()
    #Verificação de possíveis erros nos inputs no número de alunos
    while True:
        try:
            num = int(input("Qual é o número de alunos a ser adicionado na Turma?\n"))
            if num<=0: raise ValueError
            if num> len(dic_alunos)-len(turma.alunos):raise ValueError
            break
        except ValueError: print("Número Inválido! Tente Novamente\n")
    i = 0
    while i < num:
        i += add_aluno(turma)
    return None

def remov_aluno(turma):
    """Remove 1 único aluno de uma sala."""
    #Verificação de possíveis erros nos inputs no número de alunos
    while True:
        try:
            dre = input("Qual é o DRE do Aluno?\n")
            if dre in inp_inv: raise Exception
            if dre not in dic_alunos.keys(): raise ValueError
            break
        except ValueError: print("DRE Inexistente no Sistema! Tente Novamente\n")
        except Exception: print("DRE Inválido! Tente Novamente \n")
    return turma.remov_aluno(dic_alunos[dre])

def remov_alunos_turma():
    """Remove vários alunos de uma sala"""
    turma = procura_turma()
    #Verificação de possíveis erros nos inputs no número de alunos
    while True:
        try:
            num = int(input("Qual é o número de alunos a serem retirados da Turma?\n"))
            if num<=0: raise ValueError
            if num> len(turma.alunos): raise ValueError
            break
        except ValueError: print("Número Inválido! Tente Novamente\n")
    i = 0
    while i < num:
        i += remov_aluno(turma)
    return None

def nota_aluno(turma):
    while True:
        try:
            dre = input("Qual é o DRE do Aluno?\n")
            if dre in inp_inv: raise Exception
            if dre not in dic_alunos.keys(): raise ValueError
            break
        except ValueError: print("DRE Inexistente no Sistema! Tente Novamente\n")
        except Exception: print("DRE Inválido! Tente Novamente \n")
    return turma.nota_final(dic_alunos[dre])

def add_notas_turma():
    turma = procura_turma()
    #Verificação de possíveis erros nos inputs no número de alunos
    while True:
        try:
            num = int(input("Qual é o Número de Alunos a Terem suas Notas Lançadas?\n"))
            if num<=0: raise ValueError
            if num> len(turma.alunos): raise ValueError
            break
        except ValueError: print("Número Inválido! Tente Novamente\n")
    i = 0
    while i < num:
        i += nota_aluno(turma)
    return None