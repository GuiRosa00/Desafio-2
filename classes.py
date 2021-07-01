class Aluno:

    def __init__(self, nome, dre):
        self.nome = nome
        self.notas = []
        self.dre = dre
        return None

    def add_nota(self,nota,turma):
        if turma.nome not in self.notas.keys():
            print("Esse aluno não está cadastrado nessa turma!")
            return None
        self.notas[turma.nome] = nota
        print("Nota adicionada Ao currículo do aluno")
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
        while True:
            try:
                nota = eval(input("Qual é a nota final do aluno? \n"))
                if type(nota) != int or type(nota) != float:
                    raise Exception
                break
            except Exception:
                print("Essa nota não é possível de ser adicionada ao sistema.")
        if aluno in self.alunos:
            aluno.notas[self.nome] = nota
            print("Nota adicionada ao sistema do Aluno.")
            return None
        print("Este aluno não está inserido na turma.")