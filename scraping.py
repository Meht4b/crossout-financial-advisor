from bs4 import BeautifulSoup
import requests

result = requests.get('https://crossoutdb.com/#preset=flipping.category=cabins,weapons,movement.order=18desc.')
