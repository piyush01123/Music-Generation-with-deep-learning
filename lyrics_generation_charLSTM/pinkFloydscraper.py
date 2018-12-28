
from bs4 import BeautifulSoup as bs
import urllib
import re
import os


URL = 'https://www.allthelyrics.com'
f = open('the_beatles_lyrics.txt', 'a+')

soup = bs(urllib.request.urlopen(urllib.request.Request(URL+'/lyrics/the_beatles')))
links = soup.find_all('a')

useful_links = [URL+link['href'] for link in links if '/lyrics/the_beatles' in link['href']]

for i, link in enumerate(useful_links[:50]):
    print('{}-->{}'.format(i, link))
    try:
        soup = bs(urllib.request.urlopen(urllib.request.Request(link)))
        text = soup.find_all('p')
        for text in text[:-4]:
            txt = text.getText()
            f.write(txt)
        f.write('\n\n\n')
    except:
        print('Could not scrape for %dth link %s' %(i, link))
f.close()
