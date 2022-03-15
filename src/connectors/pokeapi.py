import requests
from typing import Dict, Union

from config import POKEAPI_URL, POKEAPI_TIMEOUT


class PokeAPI:
    def __init__(self) -> None:
        self.url = POKEAPI_URL
        self.timeout = POKEAPI_TIMEOUT
        self.actions = {
            "get_pokemons": "pokemon/",
            "get_egg_groups": "egg-group/",
            "get_pokemon_species": "pokemon-species/",
            "get_pokemon_types": "type/",
        }


    def __request(self, action: str, params: Dict[str, str] = None, name_or_id: Union[str, int] = None) -> Dict:
        if not isinstance(action, str) or action not in self.actions:
            raise ValueError("Invalid endpoint!")
        
        endpoint = self.url + self.actions[action]
        if name_or_id is not None:
            endpoint += str(name_or_id)

        r = requests.get(
            url=endpoint,
            params=params,
            timeout=self.timeout
        )

        if r.status_code != 200:
            raise Exception(f"Request failed. Reason: ({r.status_code}) {r.text}")
        
        return r.json()


    def __get_total_count(self, action: str) -> int:
        params = dict(limit="1")
        res = self.__request(action, params)
        return res["count"]


    def get_pokemons(self, limit: int = None) -> list:
        if not limit:
            limit = self.__get_total_count("get_pokemons")
        params = {
            "limit": limit
        }
        return self.__request("get_pokemons", params)["results"]

    
    def get_pokemon(self, name_or_id: Union[str, int]) -> list:
        if name_or_id is None:
            raise ValueError("You must provide name_or_id!")
        return self.__request("get_pokemons", name_or_id=name_or_id)

    
    def get_pokemon_specie(self, name_or_id: Union[str, int]) -> list:
        if name_or_id is None:
            raise ValueError("You must provide name_or_id!")
        return self.__request("get_pokemon_species", name_or_id=name_or_id)


    def get_egg_group(self, name_or_id: Union[str, int]) -> list:
        if name_or_id is None:
            raise ValueError("You must provide name_or_id!")
        return self.__request("get_egg_groups", name_or_id=name_or_id)
        

    def get_pokemon_type(self, name_or_id: Union[str, int]) -> list:
        if name_or_id is None:
            raise ValueError("You must provide name_or_id!")
        return self.__request("get_pokemon_types", name_or_id=name_or_id)