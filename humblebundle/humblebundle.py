import os
import sys
import requests
import bs4

# ../mylib.py
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from mylib import print_console

soup  = bs4.BeautifulSoup(requests.get("http://humblebundle.com").text)
games = [img["alt"] for img in soup.select("ul.game-boxes li img.game-box")]

print_console(", ".join(games))
