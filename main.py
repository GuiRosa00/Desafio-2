from classes import *
from comandos import *



dic_turma_menu = {"1":criar_turma,"2":prof_turma}

def turma_menu():
    """turma_menu(None)-> None
    Interface do menu das turmas do sistema"""
    print("\nMenu da turma!")
    while True:
        option = input("(1)Criar uma Nova Turma \n(2)Designar um Professor a uma Turma \n(8)Voltar ao Menu Principal\n")
        if option == "8":
            print() 
            break
        elif option in dic_turma_menu.keys():
            dic_turma_menu[option]()
        else:
            print("Este comando é inválido. Tente Novamente.")
    return None

dic_main_menu = {"1":criar_mat,"2":criar_prof,"3":criar_aluno,
"4":mostra_mat,"5": mostra_prof,"6":mostra_alunos, "7":turma_menu, "8":quit}

def main_menu():
    """main_menu(None)-> None
    Interface do menu principal do sistema da Universidade"""
    print("Bem vindo ao sistema de administração da Universidade!")
    while True:
        print("Qual operação será feita?")
        option = input("(1)Adicionar uma Matéria ao Sistema \n(2)Adicionar um Professor ao Sistema \n(3)Adicionar um Aluno ao Sistema \n(4)Mostrar Todas as Matérias do Sistema \n(5)Mostrar Todos os Professores do Sistema \n(6)Mostrar Todos os Alunos do Sistema \n(7)Entrar no Menu das Turmas \n(8)Sair do Sistema\n")
        if option in dic_main_menu.keys():
            dic_main_menu[option]()
        else:
            print("Este comando é inválido. Tente Novamente.")
    return None



if __name__ == '__main__':
    main_menu()