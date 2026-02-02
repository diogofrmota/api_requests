import requests
import pandas as pd

url = 'https://rickandmortyapi.com/api/'

def fetch_data(endpoint):
    all_data = []
    api_url = f'{url}{endpoint}'

    while api_url:
        r = requests.get(api_url)
        data = r.json()
        all_data.extend(data['results'])
        api_url = data['info']['next']
    
    return all_data

def char_type(num_episodes):
    if num_episodes > 40:
        return 'Main Character'
    elif num_episodes > 10:
        return 'Normal Character'
    else:
        return 'Rare Character'

def process_character():
    character_list = []
    char_data = fetch_data('character')

    for char in char_data:
        num_episodes = len(char['episode'])
        character_list.append({
            'id' : char['id'],
            'name' : char['name'],
            'location' : char['location']['name'],
            'num_episodes' : num_episodes,
            'char_type' : char_type(num_episodes)
        })

    df = pd.DataFrame(character_list)
    df.loc[df['name'].str.len() >= 10, 'name_type'] = 'BIG'
    df.loc[df['name'].str.len() < 10, 'name_type'] = 'SMALL'
    df.loc[df['num_episodes'] < 3, 'name'] = 'IRRELEVANT'
    df = df.sort_values('num_episodes', ascending=False)
    df.to_csv('character.csv', index=False)
    return character_list

def location_count():
    locations_data = fetch_data('location')
    return len(locations_data)

def episodes_count():
    episodes_data = fetch_data('episode')
    return len(episodes_data)

if __name__ == '__main__':
    char_data = process_character()
    char_count = len(char_data)
    loc_count = location_count()
    epi_count = episodes_count()

    print(f'Number of Characters: {char_count}')
    print(f'Number of Locations: {loc_count}')
    print(f'Number of Episodes: {epi_count}')
