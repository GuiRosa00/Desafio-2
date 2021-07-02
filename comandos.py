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
            nome = input("Insira o Nome do Aluno \n")
            dre = input("Insira o DRE do Aluno \n")
            if nome.lower() == "sair" or dre.lower()== "sair": return None
            if nome in inp_inv or dre in inp_inv: raise TypeError
            if dre in dic_alunos.keys():raise KeyError
            if not(str.isalpha(nome)):raise ValueError
            if not(str.isdecimal(dre)):raise NameError
            break
        except KeyError: print("Esse DRE já Existe no Sistema! Tente Novamente\n")
        except TypeError: print("Input Falso Detectado (input vazio)! Tente Novamente\n")
        except ValueError: print("Nome com Caractér Inválido (utilizado números)! Tente Novamente\n")
        except NameError: print("DRE com Caractér Inválido (utilizado letras)! Tente Novamente\n")
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
            nome = input("Insira o Nome do Professor\n")
            id = input("Insira o ID do Professor\n")
            if nome.lower() == "sair" or id.lower()== "sair": return None
            if nome in inp_inv or id in inp_inv: raise TypeError
            if id in dic_professores.keys():raise KeyError
            if not(str.isalpha(nome)):raise ValueError
            if not(str.isdecimal(id)):raise NameError
            break
        except KeyError: print("Esse ID já Existe no Sistema! Tente Novamente\n")
        except TypeError: print("Input Falso Detectado (input vazio)! Tente Novamente\n")
        except ValueError: print("Nome com Caractér Inválido (utilizado números)! Tente Novamente\n")
        except NameError: print("ID com Caractér Inválido (utilizado letras)! Tente Novamente\n")
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
            nome = input("Insira o Nome da Materia\n")
            codigo = input("Insira o Código da Materia\n")
            if nome.lower() == "sair" or codigo.lower()== "sair": return None
            if (nome in inp_inv or codigo in inp_inv): raise TypeError
            if (codigo in dic_materias.keys()): raise ValueError
            break
        except ValueError: print("Código da Matéria já Existente no Sistema! Tente Novamente\n")
        except TypeError: print("Input Falso Detectado (input vazio)! Tente Novamente\n")
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
            nome = input("Insira o nome da Turma\n")
            nome = nome.upper()
            if nome in dic_turmas.keys(): raise KeyError
            mat = input("Insira o código da Matéria da Turma\n")
            if nome.lower() == "sair" or mat.lower()== "sair": return None
            if mat not in dic_materias.keys(): raise ValueError
            if (nome in inp_inv) or (mat in inp_inv): raise TypeError
            break
        except KeyError: print("Nome da Turma já Existente no Sistema. Tente Novamente\n")
        except ValueError: print("Matéria Inexistente no Sistema. Tente Novamente\n")
        except TypeError: print("Input Falso Detectado (input vazio)! Tente Novamente\n")
    #criação do objeto
    dic_turmas[nome]= Turma(nome,dic_materias[mat])
    print(f"Turma Inserida no Sistema! \nNome: {nome} \nMatéria: {dic_materias[mat].nome} \nCódigo da Matéria: {mat}\n")
    return None

def procura_turma():
    """procura_turma(None)-> class
    Encontra caso possível o objeto da turma a partir de seu nome e retorna esse objeto"""
    while True:
        try:
            turma = input("Insira o nome da Turma?\n")
            if turma.lower() == "sair": return None
            if turma in inp_inv: raise TypeError
            if turma not in dic_turmas.keys(): raise ValueError
            break
        except ValueError: print("Nome Inexistente no Sistema! Tente Novamente\n")
        except TypeError: print("Input Falso Detectado (input vazio)! Tente Novamente\n")
    return dic_turmas[turma]

def prof_turma():
    """prof_turma(None)-> None
    Designa um professor à turma"""
    turma = procura_turma()
    if turma == None: return None
    #Verificação de possíveis erros nos inputs do ID do professor
    while True:
        try:
            prof = input("Insira o ID do Professor\n")
            if prof.lower() == "sair": return None
            if prof in inp_inv: raise TypeError
            if prof not in dic_professores.keys(): raise ValueError
            break
        except ValueError: print("ID Inexistente no Sistema! Tente Novamente\n")
        except TypeError: print("Input Falso Detectado (input vazio)! Tente Novamente\n")
    prof = dic_professores[prof]
    turma.add_prof(prof)
    return None

def add_aluno(turma):
    """add_aluno(object)->int
    Adiciona 1 único aluno a uma sala e retorna valores 0 ou 1 caso a adição seja feita do modo certo"""
    #Verificação de possíveis erros nos inputs no número de alunos
    while True:
        try:
            dre = input("Insira o DRE do Aluno\n")
            if dre.lower() == "sair": return None
            if dre in inp_inv: raise TypeError
            if dre not in dic_alunos.keys(): raise ValueError
            break
        except ValueError: print("DRE Inexistente no Sistema! Tente Novamente\n")
        except TypeError: print("Input Falso Detectado (input vazio)! Tente Novamente\n")
    return turma.add_aluno(dic_alunos[dre])

def add_alunos_turma():
    """add_alunos_turma(None)-> None
    Adiciona vários alunos a uma turma"""
    turma = procura_turma()
    if turma == None: return None
    #Verificação de possíveis erros nos inputs no número de alunos
    while True:
        try:
            num = input("Insira o número de alunos a ser adicionado na Turma\n")
            if num.lower() == "sair": return None
            if num in inp_inv: raise TypeError
            num = int(num)
            if num<=0: raise ValueError
            if num> len(dic_alunos)-len(turma.alunos):raise ValueError
            break
        except TypeError: print("Input Falso Detectado (input vazio)! Tente Novamente\n")
        except ValueError: print("Número Inválido! Tente Novamente\n")
    i = 0
    while i < num: #caso ocorra erros nos inputs da adição do aluno
        try:
            i += add_aluno(turma)
        #caso o comando sair seja ativado no código
        except Exception:
            return None
    return None

def remov_aluno(turma):
    """remov_aluno(object)->int
    Remove 1 único aluno a uma sala e retorna valores 0 ou 1 caso a adição seja feita do modo certo"""
    #Verificação de possíveis erros nos inputs no número de alunos
    while True:
        try:
            dre = input("Insira o DRE do Aluno\n")
            if dre.lower() == "sair": return None
            if dre in inp_inv: raise TypeError
            if dre not in dic_alunos.keys(): raise ValueError
            break
        except TypeError: print("Input Falso Detectado (input vazio)! Tente Novamente\n")
        except ValueError: print("DRE Inexistente no Sistema! Tente Novamente\n")
    return turma.remov_aluno(dic_alunos[dre])

def remov_alunos_turma():
    """remov_alunos_turma(None)-> None
    Remove vários alunos de uma sala"""
    turma = procura_turma()
    if turma == None: return None
    #Verificação de possíveis erros nos inputs no número de alunos
    while True:
        try:
            num = input("Insira o número de alunos a serem retirados da Turma\n")
            if num.lower() == "sair": return None
            if num in inp_inv: raise TypeError
            num = int(num)
            if num<=0: raise ValueError
            if num> len(turma.alunos): raise ValueError
            break
        except TypeError: print("Input Falso Detectado (input vazio)! Tente Novamente\n")
        except ValueError: print("Número Inválido! Tente Novamente\n")
    i = 0
    while i < num:#caso ocorra erros nos inputs da remoção do aluno
        try:
            i += remov_aluno(turma)
        #caso o comando sair seja ativado no código
        except Exception:
            return None
    return None

def nota_aluno(turma):
    """nota_aluno(object)-> int
    Redefine a nota de um aluno da turma e retorna 0 ou 1 caso a operação tenha ocorrido sem problemas"""
    while True:
        try:
            dre = input("Insira o DRE do Aluno\n")
            if dre.lower() == "sair": return None
            if dre in inp_inv: raise TypeError
            if dre not in dic_alunos.keys(): raise ValueError
            break
        except ValueError: print("DRE Inexistente no Sistema! Tente Novamente\n")
        except TypeError: print("Input Falso Detectado (input vazio)! Tente Novamente\n")
    return turma.nota_final(dic_alunos[dre])

def add_notas_turma():
    """add_notas_turma(None)-> None
    Adiciona no sistema da turma a nota de vários alunos nessa turma"""
    turma = procura_turma()
    if turma == None: return None
    #Verificação de possíveis erros nos inputs no número de alunos
    while True:
        try:
            num = input("Insira o Número de Alunos a Terem suas Notas Lançadas\n")
            if num.lower == "sair": return None
            if num in inp_inv: raise TypeError
            num = int(num)
            if num<=0: raise ValueError
            if num> len(turma.alunos): raise ValueError
            break
        except TypeError: print("Input Falso Detectado (input vazio)! Tente Novamente\n")
        except ValueError: print("Número Inválido! Tente Novamente\n")
    i = 0
    while i < num: #caso ocorra erros nos inputs da adição da nota
        try:
            i += nota_aluno(turma)
        #caso o comando sair seja ativado no código
        except Exception:
            return None
    return None

def mostra_alunos_turma():
    """mostra_alunos_turma(None)->None
    Mostra todos os alunos de uma turma em ordem alfabética"""
    turma = procura_turma()
    if turma == None: return None
    lista_nome = []
    for aluno in turma.alunos:
        lista_nome.append((aluno.nome,aluno.dre, aluno.pega_nota(turma)))
    lista_nome.sort(key=lambda tup: tup[0])
    print(f"Lista de Alunos da turma {turma.nome}:")
    for aluno in lista_nome:
        print(f'Nome: {aluno[0]} -- DRE: {aluno[1]} -- Nota: {aluno[2]}')
    sleep(0.5)
    print()
    return None

def mostra_turmas():
    """mostra_turmas(None)-> None
    Mostra todas as turmas cadastradas em ordem decrescente do número de alunos inseridos em cada turma"""
    #Caso não esteja cadastrado nenhuma Turma no sistema
    if len(dic_turmas) == 0:
        print("Não há Turmas Cadastradas \n")
        return None
    lista_turmas = []
    for nome,turma in dic_turmas.items():
        lista_turmas.append((nome,turma.materia.codigo,len(turma.alunos)))
    lista_turmas.sort(key=lambda tup: tup[2], reverse=True)
    print("Lista das Turmas:")
    for nome,codigo,alunos in lista_turmas:
        print(f"Nome da Turma: {nome} -- Código da Matéria: {codigo} -- Número de Alunos: {alunos}")
    print()
    return None