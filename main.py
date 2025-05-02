import requests

base_url = "https://pokeapi.co/api/v2/"

class pokemon:
    def __init__(self, name, id, moves, ability,stats, held_item, type):
        self.name = name
        self.id = id
        self.moves = moves
        self.ability = ability
        self.stats = stats
        self.held_item = held_item
        self.type = type
        
    def get_pokemon_info(name):
        url = f"{base_url}/pokemon/{name}"
        response = requests.get(url)
        print(response)
        
        if response.status_code == 200:
            pokemon_data = response.json()
            return pokemon_data
        else:
            print(f"Failed to retrieve data {response.status_code}")

pokemon_name = "pikachu"
pokemon_info = pokemon.get_pokemon_info(pokemon_name)

if pokemon_info:
    print(f"{pokemon_info["name"]}")
    print(f"{pokemon_info["id"]}")
    print(f"{pokemon_info["moves"]}")
    print(f"{pokemon_info('ability', 'Not available')}")
    print(f"{pokemon_info('stats')}")
    print(f"{pokemon_info('held_item', 'Not available')}")
    print(f"{pokemon_info('type')}")