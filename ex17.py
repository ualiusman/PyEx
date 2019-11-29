#Exercise 17:

import requests
from bs4 import BeautifulSoup

url = 'https://www.nytimes.com/'
r = requests.get(url)
r_html = r.text
soup = BeautifulSoup(r_html,"html.parser")
titles = soup.find_all('h2')
for title in titles:
    print(title.text)