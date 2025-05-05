trainers = ['ash', 'brock', 'misty']

def pokemon_trainer(self, name, pokemon):
    self.name = name
    self.pokemon = pokemon
    trainer_team = dict[trainers, pokemon]
    try:
        trainers == self.pokemon
        trainer_team.append(pokemon_trainer(pokemon))
    except:
        pass
    return trainer_team