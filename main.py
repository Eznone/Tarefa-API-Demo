from assignment_list import AssignmentFunctions
from activity import Activity
from kanye import ye
import re


#Alterar a primeira atividade, acessando a API do CRUDCRUD (todas os tipos de requisição GET, POST, PUT e DELETE);
run = 1
while run == 1:
    print("---------------------------------------------------")
    print("Digite o numero coorespendante com que quer usar:\n")
    print("1 - Registrar uma nova tarefa")
    print("2 - Acessar os dados de uma tarefa específica (através do id)")
    print("3 - Atualizar uma tarefa (através do id)")
    print("4 - Remover uma tarefa (através do id)")
    print("5 - Kanye Quote")
    print("6 - Obter atividade da dia")
    print("7 - Sair da programa")
    userInput = input(": ")
    userInput = re.sub("[\D]","",userInput)
    if userInput == '':
        print("\nUnkown command\n")
        continue
    
    command = int(userInput)
    print("---------------------------------------------------")

    site = AssignmentFunctions()
    kanye = ye()
    act = Activity()
    if command == 1:
        site.create()
    elif command == 2:
        site.read()
    elif command == 3:
        site.update()
    elif command == 4:
        site.remove()
    elif command == 5:
        kanye.quote()
    elif command == 6:
        act.generate()
    elif command == 7:
        site.download()
        run = 0
    else:
        print("\nUnknown command\n")

#Acessar uma API da sua escolha e extrair alguma informação, botando como uma opção do menu;