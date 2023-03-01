#!/usr/bin/env python3

import sys
import requests
import bs4
import html2text
from urllib.parse import urlparse

def writemd(url):
 parts = urlparse(url)
 directories = parts.path.strip('/').split('/')
 filename=directories[-1]

 response = requests.get(url).content

 soup = bs4.BeautifulSoup(response, "lxml")
 div = soup.find("div", {"class": "component-solution is-expandable"})

 h = html2text.HTML2Text()
 md=h.handle(str(div))

 f=open(filename+".md","w")
 f.write(md)
 f.close()


response = requests.get("https://portswigger.net/web-security/all-labs").content
soup = bs4.BeautifulSoup(response, "lxml")
divs = soup.find_all("div", {"class": "widgetcontainer-lab-link"})

for div in divs:
 linker = div.find("a", href=True)
 link = linker['href']
 print(link)
 writemd("https://portswigger.net"+link)
