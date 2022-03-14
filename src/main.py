import json
from subprocess import call

from connectors.pokeapi import PokeAPI




def question_1():
    pk = PokeAPI()
    names = list()

    pokemons = pk.get_pokemons()

    for pokemon in pokemons:
        name: str = pokemon["name"]
        if name.count("a") == 2 and name.count("at") >= 1:
            names.append(name)

    return len(names)


def question_2():
    pk = PokeAPI()
    res = list()

    raichu = pk.get_pokemon("raichu")
    specie_name = raichu["species"]["name"]

    specie = pk.get_pokemon_specie(specie_name)
    egg_groups = specie["egg_groups"]

    for egg_group in egg_groups:
        egg_group_name = egg_group["name"]
        egg_group_data = pk.get_egg_group(egg_group_name)
        egg_group_data_species = egg_group_data["pokemon_species"]

        for egg_group_specie_data in egg_group_data_species:
            egg_group_specie_name = egg_group_specie_data["name"]
            if egg_group_specie_name not in res:
                res.append(egg_group_specie_name)

    #print(json.dumps(res, indent=2))
    #print(len(pokemons))

    return len(res)


def question_3():
    raise NotImplementedError

questions = (
    question_1,
    question_2,
    #question_3,
)

for question in questions:
    n = questions.index(question) + 1
    print(f"Answer to question number {n}: {question()}")