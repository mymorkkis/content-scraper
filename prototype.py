#!/usr/bin/env python3.6

import sys, requests, re
from bs4 import BeautifulSoup
from create_word_document import create_word_document


# Exit with error code 2 if correct arguments not provided
if len(sys.argv) != 3:
    print('ERROR: Need 2 arguments: 1, File name to write to. 2, Url to parse.')
    sys.exit(2)
else:
    filename = sys.argv[1]
    url = sys.argv[2]
    path = url.split('.com')[1]
    authority = url.split(path)[0]

    # Parse website URL provided
    r = requests.get(url)
    soup = BeautifulSoup(r.text, 'html5lib')

    # Find all webpages for this site we want to content scrape
    internal_urls = []
    links = soup.find_all('a')
    for link in links:
        if link.has_attr('href'):
            href = link['href']
            if re.match(path, href):
                internal_urls.append(authority + href)

    unique_urls = []
    for url in internal_urls:
        if url not in unique_urls:
            unique_urls.append(url)

    # Parse scraped content into a word document with given filename
    create_word_document(filename, unique_urls)
