import requests as req

class Activity():

    def __init__(self):
        self.site = "https://www.boredapi.com/api/activity"

    def generate(self):
        response = req.get(self.site)
        if response.status_code == 200:
            print("Get funcionou!\n")
        else:
            print(f"Erro {response.status_code}: Get nao funcinou...")
        
        el = response.json()
        print("For today you will:")
        print(f'{el["activity"]} que e do tipo {el["type"]}')
        print(f'The activity requires {el["participants"]} people and has an accessibility rating of {el["accessibility"]}"')