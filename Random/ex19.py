#Exercise 17:

import requests
from bs4 import BeautifulSoup

url = 'https://www.vanityfair.com/style/society/2014/06/monica-lewinsky-humiliation-culture'
r = requests.get(url)
r_html = r.text
soup = BeautifulSoup(r.text)
all_p_cn_text_body = soup.select("div.parbase.cn_text > div.body > p")
for elem in all_p_cn_text_body[7:]:
  print(elem.text)