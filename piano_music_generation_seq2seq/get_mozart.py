from bs4 import BeautifulSoup as bs
import urllib
import os

# URL = 'http://www.kunstderfuge.com'
URL = 'http://midiworld.com/'
DATA_DIR = 'data/'

soup = bs(urllib.request.urlopen(urllib.request.Request(URL+'mozart.htm')))
links = soup.find_all('a')

for i, link in enumerate(links):
    try:
        if link['href'].endswith('.mid'):
            file_path = os.path.join(DATA_DIR, '_'.join(link.string.strip().split())+'.mid')
            print('Saving %s from %s' %(file_path, link['href']))
            urllib.request.urlretrieve(link['href'], file_path)
    except:
        pass
