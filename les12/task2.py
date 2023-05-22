

import requests


def get_info(o):
    response = requests.get(o)
    return response.json()


def get_starship():
    url = "https://swapi.dev/api/starships/10/"
    response = requests.get(url)

    if response.status_code == 200:
        return response.json()
    else:
        return None


result = get_starship()

if result:
    print("\nStarship: \n")
    print(f"name: {result['name']}")
    print(f"starship_class: {result['starship_class']}")
    print(f"speed: {result['max_atmosphering_speed']}")
    print("\npilots:")
    pilots = result["pilots"]
    for i in pilots:
        person = get_info(i)
        print(f"\nname : {person['name']}")
        print(f"height : {person['height']}")
        print(f"mass : {person['mass']}")
        planet = person['homeworld']
        res = get_info(planet)
        print(f"homeworld: {res['name']} ,{planet}")
else:
    print(f"не найдено")
