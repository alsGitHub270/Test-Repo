import requests

#added stuff
r = requests.get("https://coreyms.com")

print(r.status_code)
