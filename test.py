#!/usr/bin/env python3.6

import sys, requests, re
from bs4 import BeautifulSoup
from docx import Document

# Parse website URL provided
url = 'https://www.movenpick.com/en/asia/philippines/boracay/resort-spa-boracay/'
r = requests.get(url)
soup = BeautifulSoup(r.text, 'html.parser')
path = url.split('.com')[1]
# print(tree)
path = url.split('.com')[1]
authority = url.split(path)[0]

# reg = re.compile(r"^{}".format(tree))

# print(reg)

# Find all webpages for this site we want to content scrape
internal_links = []
links = soup.find_all('a')
for link in links:
    if link.has_attr('href'):
        href = link['href']
        if re.match(path, href) and href not in internal_links:
            internal_links.append(authority + href)


print(internal_links)
# new_list = []
# [new_list.append(item) for item in internal_links if item not in new_list]
# for link in new_list:
#     print(link)
