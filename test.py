#!/usr/bin/env python3.6

import sys, requests
from bs4 import BeautifulSoup
from docx import Document

# Parse website URL provided
r = requests.get('https://www.movenpick.com/en/asia/philippines/boracay/resort-spa-boracay/wellness/')
soup = BeautifulSoup(r.text, 'html.parser')

head = soup.head

body = soup.body

ps = soup.find_all('p')

ul = soup.find_all('ul')

ps = soup.find_all('p')

divs = soup.find_all('div')

#TODO do all internal links start with '/'?
# a = soup.find_all('a')

# for z in a:
#     if 'href' in z.attrs:
#         print(z['href'])

wanted_tags = ['h1', 'h2', 'h3', 'h4', 'h5', 'h6', 'p', 'li']
# fetched_tags = soup.find_all(tags)

p_divs = []
p_tags = soup.find_all('p')
for p in p_tags:
    p_divs.append(p.parent)

for div in p_divs:
    for tag in div.descendants:
        if tag.name in wanted_tags:
            # If header tag add heading and type
            if tag.name[0] == 'h':
                header = f'{tag.text} - ({tag.name})'
                print(header)
            # If ordered list item add number
            # TODO will this increment number
            elif tag.name == 'li' and tag.parent.name == 'ol':
                print(tag.text)
            # If unordered list item add bullet point
            elif tag.name == 'li' and tag.parent.name == 'ul':
                print(tag.text)
            # Else paragraph, no formatting needed
            else:
                print(tag.text)
#------------------------------------------
# for div in divs:
#     print(div.contents)
#     print()

# p1 = body.find_next('p')
# p2 = soup.find_next('p')
# print(p1)
# print(':')

# # print(p1.find_parent)
# for p in ps:
#     print(p.find_next_sibling)

# print(body.prettify())
# print(dir(ul[0]))
# print()
# print(ul[0].find_parent())

# for p in ps:
#     print(p.next_sibling)
#     print(p.previous_sibling)
#     print()