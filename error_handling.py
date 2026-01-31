import requests

try:
  # httpbin /delay/3 waits 3 seconds before responding
  response = requests.get("https://httpbin.org/delay/3", timout=1)
  reponse.raise_for_status()
  print("Success:", response.json())
except requests.exceptions.Timeout:
  print("Request timed out")
except requests.exceptions.RequestException as e:
  print("Request failed:", e)
