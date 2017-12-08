import requests, re
from bs4 import BeautifulSoup
from document import docx


# def verify_data(url):
#     pass
# TODO

def process_data(form):
    url = form.url.data
    filename = form.filename.data + form.file_extension.data
    scraping_type = form.scraping_type.data
    # stop_words = [word for word in form.stop_words.data.split(' ')]

    if scraping_type == 'internal_links':
        unique_urls = find_internal_links(url)
        docx.create_document(filename, unique_urls)
    else:
        docx.create_document(filename, [url])


def find_internal_links(url):
    # Parse website URL provided
    r = requests.get(url)
    soup = BeautifulSoup(r.text, 'html5lib')

    # Split url into authority (https://www.example.com) and path (/path/to/page)
    # TODO add re
    path = url.split('.com')[1]
    authority = url.split(path)[0]

    # Find all webpages for this site we want to content scrape
    internal_urls = []
    links = soup.find_all('a')
    for link in links:
        if link.has_attr('href'):
            href = link['href']
            if re.match(path, href):
                internal_urls.append(authority + href)

    # Remove any duplicate URLs
    unique_urls = []
    for url in internal_urls:
        if url not in unique_urls:
            unique_urls.append(url)

    return unique_urls
