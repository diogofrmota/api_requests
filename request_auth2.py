import requests

r = requests.get('https://httpbi.org/basic-auth/corey/testing', auth=('user', 'pass'))
print(r.json())
