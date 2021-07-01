class Aluno:

    def __init__(self, nome, dre):
        """__init__(self,string,string)-> None
        Inicializa a classe Aluno definindo nome e dre do objeto"""
        self.nome = nome
        self.notas = []
        self.dre = dre
        return None

    def muda_nota(self,nota,turma):
        """muda_nota(self,float,object)-> None
        Altera a nota cadastrada de um aluno em uma certa turma a partir de uma nota (float)"""
        for nome,n in self.notas:
            if turma.nome == nome:
                pos = self.notas.index((nome,n))
                n = nota
                self.notas[pos]=(nome,n)
                break
        print(f"Nota do aluno {self.nome} atualizada para {n}")
        return None
    
    def remov_nota(self,turma):
        """remov_nota(self,object)-> None
        Remove o cadastro da turma na lista de notas do Aluno"""
        for sala,nota in self.notas:
            if turma.nome == sala:
                list.remove(self.notas,(sala,nota))
                return None
        return None
    
    def pega_nota(self,turma):
        """pega_nota(self,object)-> None
        Retorna a nota do Aluno em uma certa turma"""
        for sala,nota in self.notas:
            if turma.nome == sala:
                return nota 
        return None

class Professor:
    def __init__(self,nome,id):
        """__init__(self,string,string) -> None
        Inicializa a classe Professor definindo nome e id do objeto"""
        self.nome = nome
        self.id = id
        return None

class Materia:

    def __init__(self,nome,codigo):
        """__init__(self,string,string) -> None
        Inicializa a classe Materia definindo nome e codigo do objeto"""
        self.nome = nome
        self.codigo = codigo
        return None

class Turma:

    def __init__(self,nome,materia,professor = "N/A"):
        """__init__(self,string,object,object) -> None
        Inicializa a classe Turma definindo nome, materia e professor (é possível omitir esse dado) do objeto"""
        self.nome = nome #string
        self.materia = materia #objeto
        self.professor = professor #objeto
        self.alunos = [] #lista de objetos!!!
        return None

    def alt_mat(self,materia):
        """alt_mat(self,object)-> None
        Altera a Materia cadastrada em uma Turma para uma nova materia"""
        self.materia = materia
        print(f"Matéria Alterada na turma {self.nome} para {materia.nome}.")
        return None

    def add_prof(self,professor):
        """add_prof(self,object)-> None
        Adiciona um Professor em uma Turma"""
        self.professor = professor
        print(f"Professor {professor.nome} Adicionado à Turma {self.nome}.\n")
        return None

    def add_aluno(self, aluno):
        """add_aluno(self,object)->int
        Caso o aluno não esteja na turma, a função adiciona o aluno na lista self.alunos, adiciona os dados da turma
        na classe do aluno e retorna um valor inteiro 1. Caso o aluno exista na Turma, a função retorna 0"""
        if aluno not in self.alunos:
            self.alunos.append(aluno)
            aluno.notas.append((self.nome,"N/A"))
            aluno.notas = aluno.notas[:]
            print(f"Aluno {aluno.nome} Adicionado à {self.nome}.\n")
            return 1
        print("Este aluno já está inserido na turma.\n")
        return 0

    def remov_aluno(self, aluno):
        """remov_aluno(self,object)->int
        Caso o aluno esteja na turma, a função retira o aluno na lista self.alunos, retira os dados da turma
        na classe do aluno e retorna um valor inteiro 1. Caso o aluno não esteja na Turma, a função retorna 0"""
        if aluno in self.alunos:
            self.alunos.remove(aluno)
            aluno.remov_nota(self)
            print(f"Aluno {aluno.nome} removido da turma. \n")
            return 1
        print("Este aluno não está inserido na turma.\n")
        return 0

    def nota_final(self, aluno):
        """nota_final(self,object)->int
        Caso o aluno esteja na turma, a função pede um valor real para a nota, adiciona a nota na classe do aluno
        caso seja possível e retorna um valor inteiro 1. Caso o aluno não esteja na Turma, a função retorna 0"""
        if aluno not in self.alunos:
            print("Este Aluno não Está Inserido na Turma.")
            return 0
        while True:
            try:
                nota = float(input("Qual é a nota final do aluno? \n"))
                if nota>10 or nota<0: raise Exception
                break
            except Exception:
                print("Não é Possível Adicionar essa Nota no Sistema. Tente Novamente.")
        aluno.muda_nota(nota,self)
        return 1