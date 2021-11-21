import requests
from bs4 import BeautifulSoup
import json

a = requests.get("https://www.instagram.com/reel/CV-vKB4vKgX/?__a=1")
tree = BeautifulSoup(a.content, 'html.parser')
print(json.loads(tree.string))


