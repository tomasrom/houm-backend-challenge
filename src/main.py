from typing import List

from connectors.pokeapi import PokeAPI


def question_1() -> int:
    # PokeAPI connector instance and result variable
    pk = PokeAPI()
    res = list()

    # Get all pokemons
    pokemons = pk.get_pokemons()

    # Process each pokemon name
    for pokemon in pokemons:
        name: str = pokemon["name"]
        if name.count("a") == 2 and name.count("at") >= 1:
            res.append(name)

    # Return answer
    return len(res)


def question_2() -> int:
    # PokeAPI connector instance and result variable
    pk = PokeAPI()
    res = list()

    # Obtain given pokemon data
    raichu = pk.get_pokemon("raichu")

    # Get pokemon specie and egg groups
    specie_name = raichu["species"]["name"]
    specie = pk.get_pokemon_specie(specie_name)
    egg_groups = specie["egg_groups"]

    # Iterate through each egg grup species list and add them to result
    for egg_group in egg_groups:
        egg_group_name = egg_group["name"]
        egg_group_data = pk.get_egg_group(egg_group_name)
        egg_group_data_species = egg_group_data["pokemon_species"]

        for egg_group_specie_data in egg_group_data_species:
            egg_group_specie_name = egg_group_specie_data["name"]
            if egg_group_specie_name not in res:
                res.append(egg_group_specie_name)

    # Return answer
    return len(res)


def question_3() -> List[int]:
    # PokeAPI connector instance and result variable
    pk = PokeAPI()
    filtered_pokemons = list()
    res = list()

    # Get first gen pokemons list (with id <= 151)
    first_gen_pokemons = set()
    pokemons = pk.get_pokemons(limit=151)
    for pokemon in pokemons:
        first_gen_pokemons.add(pokemon["name"])

    # Get fighting type pokemons 
    pokemon_type = pk.get_pokemon_type("fighting")
    fighting_pokemons = pokemon_type["pokemon"]

    # Iterate through fighting_pokemons and look for 1st gen pokemons
    for pokemon_context in fighting_pokemons:
        pokemon_name = pokemon_context["pokemon"]["name"]
        if pokemon_name in first_gen_pokemons:
            filtered_pokemons.append(pk.get_pokemon(pokemon_name))
    
    # Get weights and extremes
    weights = list()
    for pokemon in filtered_pokemons:
        weights.append(pokemon["weight"])
    res.append(max(weights))
    res.append(min(weights))

    # Return answer
    return res


def check_answers():
    questions = (
        question_1,
        question_2,
        question_3,
    )

    for question in questions:
        n = questions.index(question) + 1
        print(f"Answer to question number {n}: {question()}")

check_answers()