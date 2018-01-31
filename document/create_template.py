"""Parse URL into BeautifulSoup object and extract info into a DocumentTemplate."""
import re
import collections
import requests
from bs4 import BeautifulSoup


DocumentTemplate = collections.namedtuple(
    'DocumentTemplate', 'heading title description content top_ten_words'
)


def create_template(url, stop_words):
    """Create a DocumentTemplate namedtuple and return."""
    soup = parse_url(url)
    metas = soup.find_all('meta')

    heading = url.upper()
    title = _extract_meta('title', metas)
    description = _extract_meta('description', metas)
    content = _extract_content(soup)
    top_ten_words = _calculate_top_ten_words(content, stop_words)

    return DocumentTemplate(
        heading, title, description, content, top_ten_words
    )


def parse_url(url):
    """Create a BeautifulSoup object from provided url and return."""
    request = requests.get(url)
    soup = BeautifulSoup(request.text, 'lxml')
    return soup


def _extract_meta(meta_type, metas):
    """Helper function for create_template. Return extracted meta content."""
    for meta in metas:
        if 'name' in meta.attrs and meta.attrs['name'] == meta_type:
            content = meta.attrs['content'].strip()
            return content
    return f'No meta {meta_type} available for this page.'


def _extract_content(soup):
    """Helper function for create_template. Return a list of tuples (tag.name, tag.text)."""
    content = []
    p_divs = []
    wanted_tags = ['h1', 'h2', 'h3', 'h4', 'p', 'li']
    # Find all divs that contain paragraph text
    p_tags = soup.find_all('p')
    for p_tag in p_tags:
        if p_tag.parent not in p_divs:
            p_divs.append(p_tag.parent)
    # Extract all wanted tags and their text 
    for div in p_divs:
        for tag in div.descendants:
            if tag.name in wanted_tags:
                content.append((tag.name, tag.text.strip()))
    return content


def _calculate_top_ten_words(all_content, stop_words):
    """Helper function for create_template.

       Remove insignifcant stop words and return a list of tuples (word, count) 
       for top 10 most common words in page content.
    """
    content_text = [content[1] for content in all_content]
    text = ' '.join(content_text).lower()
    # Words must be alphanumeric and can include . or ' but not as the last letter
    word_list = re.findall(r"[\w|.|']+[\w]", text)
    wanted_words = [word for word in word_list if word not in stop_words]
    counted_words = collections.Counter(wanted_words)
    return counted_words.most_common(10)
