import requests
from bs4 import BeautifulSoup
import json

data = requests.get("https://www.instagram.com/reel/CV-vKB4vKgX/?__a=1")
tree = BeautifulSoup(data.content, 'html.parser')
json_data = json.loads(tree.string)
video_url = json_data["graphql"]["shortcode_media"]["video_url"]
print(video_url)


