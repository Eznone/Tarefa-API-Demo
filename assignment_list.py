from assignment import Assignment
import requests as req
import json

class AssignmentFunctions:

    def __init__(self):
        self.site = "http://localhost:3000/tarefas"

    def search_ID(self, userInput):
        curr = req.get(self.site)
        if curr.status_code == 200:
            print("Get funcionou!\n")
        else:
            print(f"Erro {curr.status_code}: Get nao funcinou...")
            return [curr, False]
        for el in curr.json():
            if str(el["id"]) == userInput:
                return [el, True]
        print("ID nao existe...")
        return [el, False]

    def create(self):
        tit = input("\nTitulo: ")
        des = input("\nDescricao: ")
        stat = input("\nStatus (feito ou nao): ")
        ent = input("\nData de entrega: ")
        sign = Assignment(tit, des, stat, ent)
        body = {
            "titulo": sign.tit,
            "descricao": sign.des,
            "status": sign.stat,
            "data-entrega": sign.ent
        }

        response = req.post(self.site, json = body)
        if response.status_code == 201:
            print("\nTarefa adicionada com sucesso!\n")
        else:
            print(f"\nErro {response.status_code}: Tarefa não pôde ser adicionada...\n")

    def read(self):
        userInput = input("Qual e o ID da tarefa: ")
        values = AssignmentFunctions.search_ID(self, userInput)
        el = values[0]
        if values[1] == True:
            print("ID - " + str(el["id"]))
            print("Titulo - " + str(el["titulo"]))
            print("Descricao - " + str(el["descricao"]))
            print("Entregado - " + str(el["status"]))
            print("Data de entrga - " + str(el["data-entrega"]))

    def update(self):
        num = input("Qual e o ID da tarefa: ")
        values = AssignmentFunctions.search_ID(self, num)
        if values[0] == False:
            return
        el = values[0]
        userInput = input("Qual parte voce quer atualizar (titulo, descricao, status, data-entrega, id): ")
        if userInput in el:
            novo = input("Digite novo valor: ")
            el[userInput] = novo 
            response = req.put(self.site + "/" + str(num), json = el)
            if response.status_code == 200:
                print("\nTarefa atualizado com sucesso!\n")
            else:
                print(f"\nErro {response.status_code}: Tarefa não pôde ser atualizado...\n")
            return
        else:
            print("Nao existe esse tipo...")
            return

    def remove(self):
        userInput = input("Qual e o ID da tarefa: ")
        values = AssignmentFunctions.search_ID(self, userInput)
        el = values[0]

        check = input("tem certeza? (y/n):")
        if check == "y" and values[1] == True:
            response = req.delete(self.site + "/" + str(userInput))
            if response.status_code == 200:
                print("\nTarefa deletado com sucesso!\n")
            else:
                print(f"\nErro {response.status_code}: Tarefa não pôde ser deletado...\n")
            return
        
    def download(self):
        curr = req.get(self.site)
        if curr.status_code == 200:
            print("Download funcionou!\n")
        else:
            print(f"Erro {curr.status_code}: Download nao funcinou...")
        with open("local.json", "w") as file:
            dic = {"tarefas": curr.json()}
            pretty = json.dumps(dic, indent = 2)
            file.write(pretty)