import requests

TOKEN = 'EXAMPLE'
BASE_URL = 'https://api.x.com/2/users/by/username/TechWithTimm'

headers = {
  'Authorization': f'Bearer {TOKEN}',
}

response = request.get(BASE_URL, headers=headers)

print(Status code:', response.status_code)
print('URL:', response.url)

try:
  data = response.json()
  print(data)
except ValueError:
  print('Response is not JSON:')
  print(response.text)
