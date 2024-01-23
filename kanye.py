import requests as req

class ye:

    def __init__(self):
        self.site = "https://api.kanye.rest"

    def quote(self):
        response = req.get(self.site)
        if response.status_code == 200:
            print("Get funcionou!\n")
        else:
            print(f"Erro {response.status_code}: Get nao funcinou...")
        
        el = response.json()
        print(f'Kanye says "{el["quote"]}"')
