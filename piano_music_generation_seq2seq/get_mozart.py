from bs4 import BeautifulSoup as bs
import urllib
import os

# URL = 'http://www.kunstderfuge.com'
URL = 'http://midiworld.com/mozart.htm'
DATA_DIR = 'data/'

soup = bs(urllib.request.urlopen(urllib.request.Request(URL+'/mozart.htm')))
links = soup.find_all('a')

for i, link in enumerate(links):
    try:
        if link['href'].endswith('.mid'):
            file_path = os.path.join(DATA_DIR, '_'.join(link.string.strip().split())+'.mid')
            print(file_path)
            urllib.request.urlretrieve(link['href'], file_path)
    except:
        pass

