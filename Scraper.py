#! python
#Scraper.py - Lanunches map in browser using address from the command line

import webbrowser, sys, pyperclip

if len(sys.argv) > 1:
    address = ' '.join(sys.argv[1:])
else:
    address = pyperclip.paste()

#TODO: Get address from clipboard

webbrowser.open('https://www.google.com/maps/place/' + address)
