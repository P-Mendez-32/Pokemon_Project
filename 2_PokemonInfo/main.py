def pokemon(pk, name, types, moves, EVs, health):
    pk.name = name
    pk.types = types
    pk.moves = moves
    pk.attack = EVs["attack"]
    pk.defense = EVs["defense"]
    pk.health = health

