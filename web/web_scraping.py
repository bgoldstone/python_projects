# web_scraping.py
# From freecodecamp.org
from bs4 import BeautifulSoup as bs
import urllib.request, urllib.parse, urllib.error

if __name__ == '__main__':
    url = input('Enter - ')
    html = urllib.request.urlopen(url).read()
    soup = bs(html, 'html.parser')

    # Retrieve all of the anchor tags
    tags = soup('a')
    for tag in tags:
        print(tag.get('href', None))
