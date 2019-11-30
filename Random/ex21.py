#Exercise 20:

import requests
from bs4 import BeautifulSoup

def retrive_text():
  text = ""
  url = 'https://www.nytimes.com/'
  r = requests.get(url)
  r_html = r.text
  soup = BeautifulSoup(r_html,"html.parser")
  titles = soup.find_all('h2')
  for title in titles:
    text += title.text + "\n"
  return text

def write_to_file(text,file_name):
  with open( file_name+'.txt', 'w') as open_file:
    open_file.write(text)

if __name__ == "__main__":
    file_name = input("enter file name:")
    text = retrive_text()
    write_to_file(text,file_name)
    