import requests

BASE_URL = https://httpbin.org
ENDPOINT = '/get'
TOKEN = 'EXAMPLE'

headers = {'Authorization': f'Bearer {TOKEN}'}

payload = {
    'page' : 2,
    'count' : 25,
}

try:
    response = requests.get(f'{BASE_URL}{ENDPOINT}', headers=headers, params=payload)
    response.raise_for_status()  
    
    print(response.json())
    
except requests.exceptions.RequestException as e:
    print(f"An error occurred: {e}")
except ValueError as e:
    print(f"Error parsing JSON: {e}")
