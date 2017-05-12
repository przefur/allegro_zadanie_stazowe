import requests
parameters = "updated"
url = "https://api.github.com/users/Allegro/repos"


resp = requests.get(url, params = parameters)
x = resp.json()
score = x[1]
print (score["name"])