import requests
import json

def one_piece():
    # URL Jikan API untuk daftar karakter anime "One Piece"
    url = "https://api.jikan.moe/v4/anime/21/characters"

    # Mengirim permintaan GET ke API
    response = requests.get(url)

    # Periksa apakah permintaan berhasil
    if response.status_code == 200:
        # Mengonversi data JSON ke Python
        data = response.json()

        # Ambil daftar karakter
        characters = data.get("data", [])

        # Tampilkan nama dan biodata karakter
        for char in characters:
            name = char.get("character", {}).get("name", "Unknown")
            # url = char.get("character", {}).get("url", "No URL")
            role = char.get("role", "No Role")
            print(f"Name: {name}")
            print(f"Role: {role}")
            # print(f"More Info: {url}")
            print("-" * 40)
    else:
        print(f"Error: {response.status_code}")
        
        
import requests

def get_all_pokemon():
    base_url = "https://pokeapi.co/api/v2/pokemon"
    all_pokemon = []
    limit = 100
    offset = 0

    while True:
        url = f"{base_url}?limit={limit}&offset={offset}"
        response = requests.get(url)

        if response.status_code == 200:
            data = response.json()
            results = data.get("results", [])
            all_pokemon.extend(results)  # Tambahkan data Pokémon ke list
            if not data.get("next"):  # Jika tidak ada halaman berikutnya, hentikan
                break
            offset += limit
        else:
            print(f"Failed to fetch data: {response.status_code}")
            break

    return all_pokemon

def get_pokemon_details(url):
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        return None

# Mengambil semua Pokémon
all_pokemon = get_all_pokemon()

print(f"Total Pokémon: {len(all_pokemon)}")
for pokemon in all_pokemon[:10]:  # Contoh hanya mengambil 10 Pokémon pertama
    print("-------------------------------")
    print(f"Name: {pokemon['name']}")
    details = get_pokemon_details(pokemon['url'])
    if details:
        print(f"ID: {details['id']}")
        print(f"Height: {details['height']}")
        print(f"Weight: {details['weight']}")
    else:
        print("Failed to fetch details.")
    print("-------------------------------")
    
get_pokemon_details()
