from bs4 import BeautifulSoup as bs
import urllib
import re
import os

def get_sentences(*kwargs):
    if isinstance(kwargs[0], list):
        kwargs = kwargs[0]
    words = kwargs
    good_paras=[]
    for word in words:
        url = 'https://sentence.yourdictionary.com/' + word
        soup = bs(urllib.request.urlopen(urllib.request.Request(url)))
        paras = soup.find_all('div', {"class": "li_content"})
        paras = iter(paras)
        good_para = None
        while good_para is None:
            para = next(paras)
            pstr = para.contents
            pstr = ''.join(p.string for p in pstr)
            if ' '+word+' ' in pstr:
                good_para = pstr
                good_paras.append(good_para)
            else:
                pass
    return good_paras

if __name__=='__main__':
    get_sentences('sad', 'sky', 'stomach', 'cube', 'lighter')
    get_sentences(['sad', 'sky', 'stomach', 'cube', 'lighter'])
