#! python
#Scraper.py - Lanunches map in browser using address from the command line

import webbrowser, sys, pyperclip
import urllib2
from bs4 import BeautifulSoup

def display_html( html ):
    print html
    return;

UB2 = urllib2
if len(sys.argv) > 1:
    address = ' '.join(sys.argv[1:])
else:
    address = pyperclip.paste()

page = UB2.urlopen(address).read()
soup = BeautifulSoup(page)
pretty_soup = soup.prettify()

display_html(pretty_soup)
