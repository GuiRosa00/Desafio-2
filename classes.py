class Aluno:

    def __init__(self, nome, dre,notas = {}):
        self.nome = nome
        self.notas = notas
        self.dre = dre
        return None

    def add_nota(self,nota,turma):
        if turma.nome not in self.notas.keys():
            print("Esse aluno não está cadastrado nessa turma!")
            return None
        self.notas[turma.nome] = nota
        print("Nota adicionada Ao currículo do aluno")
        return None

class Professor:

    def __init__(self,nome,id, turmas = {}):
        self.nome = nome
        self.turmas = turmas
        self.id = id
        return None

class Materia:

    def __init__(self,nome,codigo,turmas = {}):
        self.nome = nome
        self.turmas = turmas
        self.codigo = codigo
        return None

class Turma:

    def __init__(self,nome,materia = "N/A",professor = "N/A",alunos = []):
        self.nome = nome
        self.materia = materia
        self.professor = professor
        self.alunos = []
        return None

    def add_mat(self,materia):
        self.materia = materia
        print("Matéria Adicionada a essa turma")
        return None

    def add_prof(self,professor):
        self.professor = professor
        print("Professor Adicionado a essa turma")
        return None

    def add_aluno(self, aluno):
        self.alunos.append(aluno)
        print("Aluno Adicionado a essa turma")
        return None

    def remov_aluno(self, aluno):
        if aluno in self.alunos:
            self.alunos.remove(aluno)
            print("Aluno removido da turma.")
            return None
        print("Este aluno não está inserido na turma")
        return None

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