import requests

class Pokemon:
    def __init__(self, name):
        self.name = name
        self.base_url = "https://pokeapi.co/api/v2/"
        
    
    def get_pokemon_data(self):
        url = f"{self.base_url}/pokemon/{self.name}"
        response = requests.get(url)
        print(response)
        
        if response.status_code == 200:
            pokemon_data = response.json()
            return pokemon_data
        else:
            print(f"Failed to retrieve data {response.status_code}")
        
    def get_pokemon_info(self):
        pokemon_data = self.get_pokemon_data()
        if pokemon_data:
            return pokemon_data

    def get_pokemon_type(self):
        pokemon_data = self.get_pokemon_data()
        if pokemon_data:
            return pokemon_data["types"]

#    def get_pokemon_type(self):
#        url = f"{base_url}/pokemon/{name}"
#        response = requests.get(url)
#        print(response)
#
#        if response.status_code == 200:
#            pokemon_data = response.json()
#            return pokemon_data
#        else:
#            print(f"Failed to retrieve data {response.status_code}")


pokemon_name = "gengar"
pokemon = Pokemon(pokemon_name)
pokemon_info = pokemon.get_pokemon_info()
pokemon_type = pokemon.get_pokemon_type()

#print(pokemon_info)
#print(pokemon_type)