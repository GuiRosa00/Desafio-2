from classes import *
from comandos import *



dic_turma_menu = {}

def turma_menu():
    print("Menu da turma!")
    return None

dic_main_menu = {"1":adicionar_mat,"2":adicionar_prof,"3":adicionar_aluno,"4":mostra_mat,"5": mostra_prof,"6":mostra_alunos, "7":turma_menu, "8":quit}

def main_menu():
    print("Bem vindo Ao sistema de administração da Universidade!")
    while True:
        print("Qual operação será feita?")
        option = input("(1)Adicionar uma Matéria ao Sistema \n(2)Adicionar um Professor ao Sistema \n(3)Adicionar um Aluno ao Sistema \n(8)Sair do Sistema\n")
        if option in dic_main_menu.keys():
            dic_main_menu[option]()
        else:
            print("Este comando é inválido. Tente Novamente.")
    return None



if __name__ == '__main__':
    main_menu()