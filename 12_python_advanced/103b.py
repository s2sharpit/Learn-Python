# Monkey Patching
import requests


def get(url: str):
    return "<TEST RESPONSE>"


requests.get = get  # This is a monkey patch, it replaces the original function with a new one

data = requests.get("https://www.apple.com")
print(data)
