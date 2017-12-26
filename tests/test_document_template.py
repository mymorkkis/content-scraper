import unittest
from document.document_template import DocumentTemplate


class TestDocumentTemplate(unittest.TestCase):
    """docstring for TestDocumentTemplate"""

    def setUp(self):
        self.test_template = DocumentTemplate('www.test.com', ['word1', 'word2'])

    def test_initialise_template(self):
        self.assertEqual(self.test_template.heading, 'WWW.TEST.COM')
        self.assertEqual(self.test_template.stop_words, ['word1', 'word2'])

    def test_store_words(self):
        test_content = '''E.ON has; ,dot, in \t name and 99.99 \n
                          £pounds in O'neil word1 test.'''
        test_result = {
            'e.on': 1,
            'has': 1,
            'dot': 1,
            'in': 2,
            'name': 1,
            'and': 1,
            '99.99': 1,
            'pounds': 1,
            "o'neil": 1,
            'test': 1
        }
        self.test_template._store_words(test_content)
        self.assertEqual(self.test_template.words, test_result)
