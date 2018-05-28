"""Link between app home route and document package. Process web form data."""
import re

from document import docx
from stop_words import get_stop_words


def process_form_data(form):
    """Unpack url, filename & stopwords from web form. Pass to docx.create_document()."""
    url = form.url.data
    filename = form.filename.data + form.file_extension.data
    stop_words = _stop_words(form.stop_words.data)

    # TODO add functionality to create differnt document types (.odt, .pages etc)
    docx.create_document(filename, url, stop_words)


def _stop_words(form_stop_words):
    """Helper function for process_form_data. 

       Return list of stop_words to be removed from keyword analysis.
    """
    # Pre-existing list of stop words. Full list found at:
    # https://github.com/Alir3z4/stop-words/blob/0e438af98a88812ccc245cf31f93644709e70370/english.txt
    stop_words = get_stop_words('english')
    # Words must be alphanumeric and can include . or ' but not as the last letter
    added_words = re.findall(r"[\w|.|']+[\w]", form_stop_words)
    stop_words.extend(added_words)
    return stop_words
