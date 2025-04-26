import requests

BASE_URL = "http://localhost:8000"  # Adjust this if your FastAPI is hosted elsewhere

def get_all_pokemon():
    """Fetch all Pokémon from the API."""
    response = requests.get(f"{BASE_URL}/pokemon")
    if response.status_code == 200:
        pokemons = response.json()
        for pokemon in pokemons:
            print(f"{pokemon['id']}: {pokemon['name']} ({pokemon['type1']} {pokemon['type2'] or ''})")
    else:
        print("Error fetching Pokémon.")

def get_pokemon_by_name(name):
    """Fetch a specific Pokémon by name."""
    response = requests.get(f"{BASE_URL}/pokemon/{name}")
    if response.status_code == 200:
        pokemon = response.json()
        print(f"ID: {pokemon['id']}")
        print(f"Name: {pokemon['name']}")
        print(f"Type: {pokemon['type1']} {pokemon['type2'] or ''}")
        print(f"Description: {pokemon['description']}")
        print(f"Image URL: {pokemon['image_url']}")
    else:
        print("Pokémon not found.")

def get_pokemon_by_type(pokemon_type):
    """Fetch Pokémon by type."""
    response = requests.get(f"{BASE_URL}/pokemon/type/{pokemon_type}")
    if response.status_code == 200:
        pokemons = response.json()
        print(f"Pokémon of type {pokemon_type}:")
        for pokemon in pokemons:
            print(f"{pokemon['id']}: {pokemon['name']} ({pokemon['type1']} {pokemon['type2'] or ''})")
    else:
        print(f"No Pokémon found with type {pokemon_type}.")

def main():
    """Simple CLI menu to interact with the API."""
    while True:
        print("\nPokémon CLI")
        print("1. List all Pokémon")
        print("2. Search Pokémon by name")
        print("3. Search Pokémon by type")
        print("4. Exit")

        choice = input("Choose an option: ").strip()

        if choice == "1":
            get_all_pokemon()
        elif choice == "2":
            name = input("Enter Pokémon name: ").strip()
            get_pokemon_by_name(name)
        elif choice == "3":
            pokemon_type = input("Enter Pokémon type: ").strip()
            get_pokemon_by_type(pokemon_type)
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid option. Please try again.")

if __name__ == "__main__":
    main()
