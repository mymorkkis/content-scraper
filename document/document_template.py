from document.stopwords import stop_words


class DocumentTemplate(object):
    """Document Template Class"""

    def __init__(self, url):
        self.heading = url.upper()
        self.title = ''
        self.description = ''
        self.content = []
        self.top_ten_words = None
        self.words = {}

    def get_title(self, metas):
        '''Retrieve meta title from URL'''
        self.title = self._get_meta('title', metas)

    def get_description(self, metas):
        '''Retrieve meta description from URL'''
        self.description = self._get_meta('description', metas)

    def get_content(self, tag_name, tag_text):
        '''Append tag_name and tag_text provided to content list and store words for keyword analysis'''
        self._store_words(tag_text)
        self.content.append((tag_name, tag_text))

    def get_top_ten_words(self):
        '''Returns a list of tuples (word, count) for the ten most common words
            in this sub-section. Insignificant stop words have been pre-removed.
        '''
        sorted_words = sorted(self.words.items(), key=lambda x: x[1], reverse=True)
        self.top_ten_words = sorted_words[:10]

    def _get_meta(self, meta_type, metas):
        '''Add desired meta type content and store words for keyword analysis'''
        for meta in metas:
            if 'name' in meta.attrs and meta.attrs['name'] == meta_type:
                content = meta.attrs['content']
                self._store_words(content)
                return content

    def _store_words(self, content):
        '''Store words for keyword analyis, removing any insignificant stop words'''
        content = [word.lower() for word in content.split(' ')]
        content = self._remove_stopwords(content)
        for word in content:
            if word in self.words:
                self.words[word] += 1
            else:
                self.words[word] = 1

    def _remove_stopwords(self, words):
        '''Removes pre-determined stop words from a given list and returns list'''
        wanted_words = []
        for index, word in enumerate(words):
            if word not in stop_words:
                wanted_words.append(words[index])
        return(wanted_words)
