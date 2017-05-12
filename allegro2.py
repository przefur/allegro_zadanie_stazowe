import requests
url = "https://api.github.com/users/Allegro/repos"
parameters = "sort=pushed"
resp = requests.get(url, params=parameters)
x = resp.json()
print((x[0])["name"])