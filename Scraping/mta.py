import requests
import urllib.request
import time
from bs4 import BeautifulSoup
# cherry pick Test
url = 'http://web.mta.info/developers/turnstile.html'
response = requests.get(url)

soup = BeautifulSoup(response.text, "html.parser")

anchors = soup.findAll('a')

for i in range(36,len(anchors)):
    anchor = anchors[i]
    link = anchor['href']
    download_url = 'http://web.mta.info/developers/'+ link
    fileName = link[link.find('/turnstile_')+1:]
    urllib.request.urlretrieve(download_url,fileName) 
    time.sleep(2)