import requests
resp = requests.get("https://api.github.com/users/Allegro/repos?sort=pushed")
x = resp.json()
print((x[0])["name"])