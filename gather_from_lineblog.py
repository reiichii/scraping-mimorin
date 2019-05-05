import requests
from bs4 import BeautifulSoup

r = requests.get('https://lineblog.me/mimori_suzuko/')
soup = BeautifulSoup(r.content, 'html.parser')
divs = soup.find_all('div', class_='article-body')
for div in divs:
    img = div.find_all('img', width='600')
    print(img)
