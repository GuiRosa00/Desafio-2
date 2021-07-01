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
        print(f"Matéria Alterada nessa turma para {materia.nome}")
        return None

    def add_prof(self,professor):
        self.professor = professor
        print(f"Professor {professor.nome} Adicionado à Turma {self.nome}\n")
        return None
    
    #rascunhos
    def add_aluno(self, aluno):
        self.alunos.append(aluno)
        aluno.notas[self.nome] = "N/A"
        print("Aluno Adicionado a essa turma")
        return None

    def remov_aluno(self, aluno):
        if aluno in self.alunos:
            self.alunos.remove(aluno)
            del aluno.notas[self.nome]
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