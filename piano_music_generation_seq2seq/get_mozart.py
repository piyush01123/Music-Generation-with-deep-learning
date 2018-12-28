from bs4 import BeautifulSoup as bs
import urllib
import re
import os
import requests

# URL = 'http://www.kunstderfuge.com'
URL = 'http://midiworld.com/mozart.htm'
DATA_DIR = 'data/'

soup = bs(urllib.request.urlopen(urllib.request.Request(URL+'/mozart.htm')))
links = soup.find_all('a')

for i, link in enumerate(links):
    try:
        print(link['href'])
        if link['href'].endswith('.mid'):
            # r = requests.get(URL+link['href'])
            # redirected_url = r.url
            # midi_links.append(redirected_url)
            file_path = os.path.join(DATA_DIR, '_'.join(link.string.strip().split())+'.mid')
            urllib.request.urlretrieve(midi_link, file_path)
    except:
        pass
