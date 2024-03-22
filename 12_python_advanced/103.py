# In this file we are using the requests library to make a request to the website/api.
# For monkey Patching, check 103b.py
import requests

# data = requests.get("https://api.github.com/users/s2sharpit").json()
# data = requests.get("https://s2sharpit.me/api/skills").json()

data = requests.get("https://www.apple.com")
print(data)
