import requests
from bs4 import BeautifulSoup
from document.document_template import DocumentTemplate


def create_template(url):
    # Parse website URL provided
    r = requests.get(url)
    soup = BeautifulSoup(r.text, 'html5lib')
    template = DocumentTemplate(url)

    # Find meta name and meta description
    metas = soup.find_all('meta')
    template.get_title(metas)
    template.get_description(metas)

    # Stipulate all the body text we are interestd in
    wanted_tags = ['h1', 'h2', 'h3', 'h4', 'p', 'li']

    # Find all divs that contain paragraph text
    p_divs = []
    p_tags = soup.find_all('p')
    for p in p_tags:
        if p.parent not in p_divs:
            p_divs.append(p.parent)

    # Add all the text inside the div to the template
    for div in p_divs:
        for tag in div.descendants:
            if tag.name in wanted_tags:
                template.get_content(tag.name, tag.text)

    # Find ten most common keywords
    template.get_top_ten_words()

    return template
