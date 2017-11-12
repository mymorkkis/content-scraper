#!/usr/bin/env python3.6

import sys, requests, html5lib
from bs4 import BeautifulSoup
from docx import Document

# Exit with error code 2 if correct arguments not provided
if len(sys.argv) != 3:
    print('ERROR: Need 2 arguments: 1, File name to write to. 2, Url to parse.')
    sys.exit(2)
else:
    filename = sys.argv[1]
    url = sys.argv[2]
    
    # Parse website URL provided
    r = requests.get(url)
    soup = BeautifulSoup(r.text, 'html5lib')

    # Create document and add heading
    document = Document()
    document.add_heading(url, 0)

    # Find page meta name and meta description
    # TODO Is there a more performant or succinct way
    metas = soup.find_all('meta')

    # TODO Add ':' after title and description
    for meta in metas:
        if 'name' in meta.attrs and meta.attrs['name'] == 'title':
                name = document.add_paragraph()
                name.add_run(meta.attrs['name']).bold = True
                document.add_paragraph(meta.attrs['content'])
                break

    for meta in metas:
        if 'name' in meta.attrs and meta.attrs['name'] == 'description':
                description = document.add_paragraph()
                description.add_run(meta.attrs['name']).bold = True
                document.add_paragraph(meta.attrs['content'])
                break

    # TODO add 'Content:'' text here

    # Stipulate all the body text we are interestd in 
    wanted_tags = ['h1', 'h2', 'h3', 'h4', 'h5', 'h6', 'p', 'li']

    # Find all divs that contain paragraph text
    p_divs = []
    p_tags = soup.find_all('p')
    for p in p_tags:
        p_divs.append(p.parent)

    # Add all info from the div to the document
    for div in p_divs:
        for tag in div.descendants:
            if tag.name in wanted_tags:
                # If header tag add heading and type
                if tag.name[0] == 'h':
                    header = f'{tag.text} - ({tag.name})'
                    document.add_heading(header, level=1)
                # If ordered list item add number
                # TODO will this increment number
                elif tag.name == 'li' and tag.parent.name == 'ol':
                    document.add_paragraph(tag.text, style='List Number')
                # If unordered list item add bullet point
                elif tag.name == 'li' and tag.parent.name == 'ul':
                    document.add_paragraph(tag.text, style='List Bullet')
                # Else paragraph, no formatting needed
                else:
                    document.add_paragraph(tag.text)


    document.save(filename)
