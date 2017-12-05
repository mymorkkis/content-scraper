from document.stopwords import stop_words


class UrlDocument(object):
    """TODO"""

    def __init__(self, url):
        self.heading = url
        self.title = ''
        self.description = ''
        self.content = []
        self.top_ten_words = None
        self.words = {}

    def get_title(self, metas):
        self.title = self.get_meta('title', metas)

    def get_description(self, metas):
        self.description = self.get_meta('description', metas)

    def get_meta(self, meta_type, metas):
        '''Add desired meta type content and store words for keyword analysis'''
        for meta in metas:
            if 'name' in meta.attrs and meta.attrs['name'] == meta_type:
                content = meta.attrs['content']
                self.store_words(content)
                return content

    def get_content(self, tag_name, tag_text):
        self.store_words(tag_text)
        self.content.append((tag_name, tag_text))

    def get_top_ten_words(self):
        '''Returns a list of tuples (word, count) for the ten most common words
            in this sub-section. Insignificant stop words have been pre-removed.
        '''
        sorted_words = sorted(self.words.items(), key=lambda x: x[1], reverse=True)
        self.top_ten_words = sorted_words[:10]

    def store_words(self, content):
        '''Store words for keyword analyis, removing any insignificant stop words'''
        content = [word.lower() for word in content.split(' ')]
        content = self.remove_stopwords(content)
        for word in content:
            if word in self.words:
                self.words[word] += 1
            else:
                self.words[word] = 1

    def remove_stopwords(self, words):
        '''Removes pre-determined stop words from a given list'''
        wanted_words = []
        for index, word in enumerate(words):
            if word not in stop_words:
                wanted_words.append(words[index])
        return(wanted_words)
