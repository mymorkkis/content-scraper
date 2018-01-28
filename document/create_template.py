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
    words = _store_words(content, stop_words)
    top_ten_words = _calculate_top_ten_words(words)

    template = DocumentTemplate(
        heading,
        title,
        description,
        content,
        top_ten_words
    )
    return template


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


def _store_words(all_content, stop_words):
    """Helper function for create_template. Return dictionary of word counts."""
    words = {}
    content_text = [content[1] for content in all_content]
    text = ' '.join(content_text).lower()
    # Words must be alphanumeric and can include . or ' but not the last letter
    word_list = re.findall(r"[\w|.|']+[\w]", text)
    wanted_words = [word for word in word_list if word not in stop_words]
    for word in wanted_words:
        if word in words:
            words[word] += 1
        else:
            words[word] = 1
    return words


def _calculate_top_ten_words(words):
    """Helper function for create_template.

       Return a list of tuples (word, count) for the ten most common words in the URL. 
       Insignificant stop words have been pre-removed.
    """
    # Sort dictionary of words: word_count by word_count descending
    sorted_words = sorted(words.items(), key=lambda x: x[1], reverse=True)
    return sorted_words[:10]

