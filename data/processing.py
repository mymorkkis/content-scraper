import requests, re
from bs4 import BeautifulSoup
from document import docx


# def verify_url(url):
#     print('calling verify_url')
#     r = requests.head(url)
#     return r

def process_data(form):
    url = form.url.data
    print(url)
    print('cowabunga')
    filename = form.file_name.data
    extension = form.file_extension.data
    scraping_type = form.scraping_type.data
    # stop_words = [word for word in form.stop_words.data.split(' ')]

    # Parse website URL provided
    r = requests.get(url)
    soup = BeautifulSoup(r.text, 'html5lib')

    if scraping_type == 'internal_links':
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

        unique_urls = []
        for url in internal_urls:
            if url not in unique_urls:
                unique_urls.append(url)

        docx.create_multipart_document(filename, extension, unique_urls)

    else:
        docx.create_document(filename, extension, url)
