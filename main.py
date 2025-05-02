import requests

base_url = "https://pokeapi.co/api/v2/"

class pokemon_info:
    def __init__(self, name, id, moves, ability,stats, held_item, type):
        """
        Initialize the pokemon object.
        
        Args:
            name (str): The name of the pokemon.
            id (int): The id of the pokemon.
            moves (list): A list of moves.
            ability (str): The ability of the pokemon.
            stats (dict): A dictionary with the stats of the pokemon.
            held_item (str): The held item of the pokemon.
            type (list): A list of types.
        """
        if not name:
            raise ValueError("Pokemon name cannot be empty.")
        if not id:
            raise ValueError("Pokemon id cannot be empty.")
        if not moves:
            raise ValueError("Pokemon moves cannot be empty.")
        if not ability:
            raise ValueError("Pokemon ability cannot be empty.")
        if not stats:
            raise ValueError("Pokemon stats cannot be empty.")
        if not held_item:
            raise ValueError("Pokemon held item cannot be empty.")
        if not type:
            raise ValueError("Pokemon type cannot be empty.")
        self.name = name
        self.id = id
        self.moves = moves
        self.ability = ability
        self.stats = stats
        self.held_item = held_item
        self.type = type
    
def get_pokemon_info(pokemon_name):
    url = f"{base_url}/pokemon/{pokemon_name}"
    response = requests.get(url)
    print(response)
    
    if response.status_code == 200:
        pokemon_data = response.json()
        return pokemon_data
    else:
        print(f"Failed to retrieve data {response.status_code}")

pokemon_name = "pikachu"
pokemon_info = get_pokemon_info(pokemon_name)

if pokemon_info:
    print(f"{pokemon_info["name"]}")
    print(f"{pokemon_info["id"]}")
    print(f"{pokemon_info["moves"]}")
    print(f"{pokemon_info('ability', 'Not available')}")
    print(f"{pokemon_info('stats')}")
    print(f"{pokemon_info('held_item', 'Not available')}")
    print(f"{pokemon_info('type')}")