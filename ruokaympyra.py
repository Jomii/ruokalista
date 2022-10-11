from random import randint
import sys
from traceback import print_exc

# Ruokaympyrä-ohjelma, jolle annetaan parametrinä teksitiedosto, jossa on lista ruuista.
# Listasta valitaan satunnaisesti yksi ruokalaji ja tulostetaan se käyttäjälle.

if len(sys.argv) < 2:
    print("Anna ohjelman parametrina lista ruuista esim. python ruokalista.py <ruoat.txt>")
    exit()

file_path = sys.argv[1]
foods = []

# Yritä lukea tiedostosta rivi kerrallaan ruokalajeja
try:
    file = open(file_path)

    for line in file:
        foods.append(line.rstrip()) # Lisää ruokalaji listalle, poistaen rivinvaihdon '\n' ruokalajin perästä.
    
    print(f"Luettu {len(foods)} kpl ruokavaihtoehtoja tiedostosta {file_path}")
    file.close()
except:
    print("Tiedostoa ei voitu avata")
    print_exc() # Virheen sattuessa tulosta tarkempi virheen kuvaus.

random_index = randint(0, len(foods) - 1) # Valitse satunnainen luku 0 ja listan pituuden (-1) väliltä.
selected_food = foods[random_index] # Käytä satunnaista lukua indeksinä valitsemaan yksi listan alkio.
print("Arvottu ruokanne on: ", selected_food)