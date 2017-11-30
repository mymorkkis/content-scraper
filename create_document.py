import requests
from bs4 import BeautifulSoup
from url_document import UrlDocument


def create_url_document(url):
    # Parse website URL provided
    r = requests.get(url)
    soup = BeautifulSoup(r.text, 'html5lib')
    document = UrlDocument(url)

    # Find meta name and meta description
    metas = soup.find_all('meta')
    document.get_title(metas)
    document.get_description(metas)

    # Stipulate all the body text we are interestd in
    wanted_tags = ['h1', 'h2', 'h3', 'h4', 'h5', 'h6', 'p', 'li']

    # Find all divs that contain paragraph text
    p_divs = []
    p_tags = soup.find_all('p')
    for p in p_tags:
        p_divs.append(p.parent)

    # Add all the text inside the div to the document
    for div in p_divs:
        for tag in div.descendants:
            if tag.name in wanted_tags:
                document.get_content(tag.name, tag.text)

    document.get_top_ten_words()

    return document
