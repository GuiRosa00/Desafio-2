class Aluno:

    def __init__(self, nome, dre):
        self.nome = nome
        self.notas = []
        self.dre = dre
        return None

    def muda_nota(self,nota,turma):
        for nome,n in self.notas:
            if turma.nome == nome:
                pos = self.notas.index((nome,n))
                n = nota
                self.notas[pos]=(nome,n)
        print(f"Nota do aluno {self.nome} atualizada para {n}")
        return None
    
    def remov_nota(self,turma):
        for sala,nota in self.notas:
            if turma.nome == sala:
                list.remove(self.notas,(sala,nota))
        return None


class Professor:

    def __init__(self,nome,id, turmas = []):
        self.nome = nome
        self.turmas = turmas
        self.id = id
        return None

class Materia:

    def __init__(self,nome,codigo,turmas = []):
        self.nome = nome
        self.turmas = turmas
        self.codigo = codigo
        return None

class Turma:

    def __init__(self,nome,materia,professor = "N/A",alunos = []):
        self.nome = nome #string
        self.materia = materia #objeto
        self.professor = professor #objeto
        self.alunos = alunos #lista de objetos!!!
        return None

    def alt_mat(self,materia):
        self.materia = materia
        print(f"Matéria Alterada na turma {self.nome} para {materia.nome}.")
        return None

    def add_prof(self,professor):
        self.professor = professor
        print(f"Professor {professor.nome} Adicionado à Turma {self.nome}.\n")
        return None
    
    #rascunhos
    def add_aluno(self, aluno):
        if aluno not in self.alunos:
            self.alunos.append(aluno)
            aluno.notas.append((self.nome,"N/A"))
            aluno.notas = aluno.notas[:]
            print(f"Aluno {aluno.nome} Adicionado à {self.nome}.\n")
            return 1
        print("Este aluno já está inserido na turma.\n")
        return 0

    def remov_aluno(self, aluno):
        if aluno in self.alunos:
            self.alunos.remove(aluno)
            aluno.remov_nota(self)
            print(f"Aluno {aluno.nome} removido da turma. \n")
            return 1
        print("Este aluno não está inserido na turma.\n")
        return 0

    def nota_final(self, aluno):
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