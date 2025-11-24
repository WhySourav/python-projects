#how to connect to a api using python


#trying too learn about api and stuff 


import requests

baseurl = "https://pokeapi.co/api/v2/"

input_name = input("Name of the pokimon: ")

def get_pokemon_data(name):
    url = f"{baseurl}pokemon/{name.lower()}"
    response = requests.get(url)
    
    if response.status_code == 200:
        pokemon_data=response.json()
        return pokemon_data
    else:
        print("failed to retrieve data")

pokemoninfo= get_pokemon_data(input_name)


if pokemoninfo:
    print(f"Name: {pokemoninfo["name"]}")
    print(f"ID: {pokemoninfo["id"]}")
    print(f"pokwmon type : {pokemoninfo["types"][0]["type"]["name"]}")
    print(f"height: {pokemoninfo["height"]}")
    print(f"weight: {pokemoninfo["weight"]}")
    print("Abilities:")
    for abilities in pokemoninfo["abilities"]:
        print(f"- {abilities['ability']['name']}")
else:
    print("soomething went wrong.")