import os
import random
import requests
from bs4 import BeautifulSoup

blog_url = 'https://lineblog.me/mimori_suzuko/'
download_file_name = str(os.environ['HOME']+'/Desktop/tmp/')+str(random.randint(10000,99999))+'.jpeg'

re = requests.get(blog_url)
soup = BeautifulSoup(re.content, 'html.parser')
divs = soup.find_all('div', class_='article-body')
for div in divs:
    img = div.find_all('img', width='600')
    for i in img:
        print(i['src'])
        r = requests.get(i['src'])
        with open(download_file_name,'wb') as f:
            f.write(r.content)
